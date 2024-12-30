import os
import json
import logging
from notion_client import Client
from apify_client import ApifyClient
from dotenv import load_dotenv
import datetime
import openai
import tempfile

# Configure logging for Lambda
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize clients outside the handler for better performance
def initialize_clients():
    # Load environment variables (for local testing)
    if os.path.exists('.env'):
        load_dotenv()
    
    # Initialize the clients
    notion = Client(auth=os.environ.get('NOTION_API_KEY'))
    apify_client = ApifyClient(os.environ.get('APIFY_API_TOKEN'))
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    
    return notion, apify_client

notion, apify_client = initialize_clients()

def get_temp_directory():
    """Get a temporary directory for Lambda execution"""
    return tempfile.gettempdir()

def save_to_temp(content, filename):
    """Save content to a temporary file"""
    temp_dir = get_temp_directory()
    file_path = os.path.join(temp_dir, filename)
    with open(file_path, 'w') as f:
        f.write(content)
    return file_path

# Function to fetch all blocks from a Notion page
def fetch_page_blocks(page_id):
    blocks = []
    cursor = None
    while True:
        response = notion.blocks.children.list(block_id=page_id, start_cursor=cursor)
        blocks.extend(response['results'])
        if not response['has_more']:
            break
        cursor = response['next_cursor']
    return blocks

# Function to process the fetched data
def process_notion_data(blocks):
    output = {
        'profile': '',
        'interests': [],
        'accounts_to_follow': []
    }

    current_section = ''

    for block in blocks:
        block_type = block['type']
        content = ' '.join(text['plain_text'] for text in block.get(block_type, {}).get('rich_text', []))

        if block_type == 'heading_2':
            if content.lower() == 'profile':
                current_section = 'profile'
            elif content.lower() == 'interests':
                current_section = 'interests'
            elif content.lower() == 'accounts to follow':
                current_section = 'accounts_to_follow'
        elif block_type == 'paragraph' and current_section:
            if current_section == 'profile':
                output['profile'] += content + ' '
            else:
                output[current_section].append(content)

    return output

# Function to transform the processed data into the Apify input format
def transform_to_apify_input(output):
    # Calculate the start date as 3 days from the current date
    start_date = (datetime.datetime.now() + datetime.timedelta(days=5)).strftime('%Y-%m-%d')

    apify_input = {
        "customMapFunction": "(object) => { return {...object} }",
        "includeSearchTerms": True,
        "maxItems": 120,
        "minimumRetweets": 30,
        "onlyImage": False,
        "onlyQuote": False,
        "onlyTwitterBlue": False,
        "onlyVerifiedUsers": True,
        "onlyVideo": False,
        "searchTerms": output['interests'],
        "sort": "Top",
        "start": start_date,
        "startUrls": output['accounts_to_follow'],
        "tweetLanguage": "en"
    }
    return apify_input

def get_output_directory():
    """Get the appropriate directory for outputs based on environment"""
    if os.environ.get('AWS_LAMBDA_FUNCTION_NAME'):  # Check if running in Lambda
        return tempfile.gettempdir()
    else:
        # Local environment - use jsons/outputs
        output_dir = 'jsons/outputs'
        os.makedirs(output_dir, exist_ok=True)
        return output_dir

def save_file(content, filename, is_json=False):
    """Save content to a file in the appropriate directory"""
    output_dir = get_output_directory()
    file_path = os.path.join(output_dir, filename)
    
    mode = 'w'
    if is_json:
        with open(file_path, mode) as f:
            json.dump(content, f, indent=4)
    else:
        with open(file_path, mode) as f:
            f.write(content)
            
    return file_path

# Function to run the Apify actor task using the Apify client
def run_apify_actor(apify_input, output):
    logging.info('Starting Apify actor task run...')
    start_time = datetime.datetime.now()
    try:
        # Run the Actor task and wait for it to finish
        logging.info('Calling Apify task...')
        run = apify_client.task("gksWpvaHUIAV3fIBa").call(task_input=apify_input)

        # Fetch Actor task results
        logging.info('Fetching results from Apify...')
        results = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
        num_results = len(results)
        logging.info(f'Retrieved {num_results} tweets from Apify')
        
        # Generate timestamp for files
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')
        
        # Sort the results
        sorted_results = sorted(results, key=lambda x: x.get('likeCount', 0), reverse=True)
        logging.info('Sorted tweets by like count')

        # Generate summary
        logging.info('Generating summary with OpenAI...')
        summary = summarize_tweets(sorted_results, output['profile'], output['interests'])
        logging.info('Summary generated successfully')

        # Save files
        json_filename = f'{timestamp}_{num_results}.json'
        md_filename = f'{timestamp}_{num_results}.md'
        
        # Save markdown file
        md_path = save_file(summary.replace('```markdown', '').replace('```', '').strip(), md_filename)
        logging.info(f'Saved markdown file: {md_path}')
        
        # Save JSON file
        output_data = {"summary": "Summary saved to markdown file", "tweets": sorted_results}
        json_path = save_file(output_data, json_filename, is_json=True)
        logging.info(f'Saved JSON file: {json_path}')
            
        return summary

    except Exception as e:
        logging.error(f'Error running Apify actor task: {e}')
        return None
    finally:
        end_time = datetime.datetime.now()
        duration = end_time - start_time
        logging.info(f'Apify actor task completed in {duration}')

def summarize_tweets(tweets, profile, interests):
    # Prepare the text to be summarized with URLs
    tweet_texts_with_urls = []
    for tweet in tweets:
        if 'text' in tweet:
            # Get the tweet URL
            tweet_url = tweet.get('url', '')
            username = tweet.get('username', '')
            
            # Add the tweet text with its URL for reference
            tweet_info = {
                'text': tweet['text'],
                'url': tweet_url,
                'username': username
            }
            tweet_texts_with_urls.append(tweet_info)
    
    # Combine tweets into a format that includes URLs
    combined_text = "\n\n".join([
        f"Tweet by @{t['username']}:\n{t['text']}\nURL: {t['url']}"
        for t in tweet_texts_with_urls
    ])

    # Create the prompt with profile and interests information
    assistant_prompt = (
        f"You are a skilled research analyst tasked with creating comprehensive tweet summaries. "
        f"The analysis is tailored for {profile}, with interests in: {interests}.\n\n"
        "Follow these strict guidelines for the summary:\n\n"
        "1. STRUCTURE:\n"
        "   - Start with a clear title (H1)\n"
        "   - Include exact count: 'Information taken from analysis of X tweets'\n"
        "   - Use H2 headers for main sections\n"
        "   - Use bullet points for listing related information\n"
        "   - Each section should be 2-3 paragraphs maximum\n\n"
        "2. SOURCING:\n"
        "   - Every major claim must have a source link\n"
        "   - Format sources as [Source: @username](actual_tweet_url)\n"
        "   - Include the source immediately after the claim\n"
        "   - Multiple sources should be numbered: [Source 1: @username](url1), [Source 2: @username](url2)\n"
        "   - IMPORTANT: Use the actual tweet URLs provided in the text, don't use placeholder URLs\n\n"
        "3. CONTENT REQUIREMENTS:\n"
        "   - Separate factual information (from tweets) from analysis\n"
        "   - Use bullet points for key takeaways\n"
        "   - Include specific numbers, data, or examples when available\n"
        "   - Avoid repetition of ideas\n"
        "   - For each major topic, include:\n"
        "     * What was stated (fact)\n"
        "     * Why it matters (analysis)\n"
        "     * Potential implications (insight)\n\n"
        "4. FORMATTING:\n"
        "   - Use bold (**) for key terms\n"
        "   - Use bullet points (-) for lists\n"
        "   - Keep paragraphs short (2-3 sentences)\n"
        "   - Use horizontal rules (---) to separate major sections\n\n"
        f"Tweets to analyze:\n{combined_text}"
    )

    user_prompt = (
        f"Create a structured, well-sourced analysis of these tweets for {profile}, "
        f"focusing on {interests}. Follow the formatting and structure guidelines exactly. "
        "Make sure to use the actual tweet URLs provided in the source citations."
    )

    # Call OpenAI API to summarize the tweets
    response = openai.chat.completions.create(
        model="gpt-4o",
        max_tokens=5000,
        temperature=0.5,
        response_format={"type": "text"},
        messages=[
            {"role": "system", "content": assistant_prompt},
            {"role": "user", "content": user_prompt}
        ],
    )

    # Extract the summary from the response
    summary = response.choices[0].message.content.strip()
    return summary

def create_notion_entry(markdown_content):
    # Get database ID from environment variables
    database_id = os.getenv('NOTION_DATABASE_ID')
    
    # Get current timestamp for the title
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    
    def parse_markdown_text(text, block_type="paragraph"):
        """Parse markdown text and return list of rich_text objects with proper formatting"""
        rich_text_blocks = []
        
        # Regular expression to find markdown links and bold text
        import re
        from urllib.parse import urlparse
        
        def is_valid_url(url):
            """Validate URL format and common schemes"""
            try:
                result = urlparse(url)
                return all([result.scheme in ['http', 'https'], result.netloc])
            except:
                return False
        
        def clean_url(url):
            """Clean and validate URL"""
            # Remove any whitespace
            url = url.strip()
            
            # Ensure URL has a scheme
            if not url.startswith(('http://', 'https://')):
                url = 'https://' + url
                
            return url if is_valid_url(url) else None
        
        def process_text(text):
            # For bullet points and paragraphs, convert bold markdown to plain text
            if block_type in ["bulleted_list_item", "paragraph"]:
                # Remove bold markdown but keep the text
                text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
            
            return [{
                "type": "text",
                "text": {
                    "content": text
                }
            }]
        
        def process_links(text_blocks):
            final_blocks = []
            for block in text_blocks:
                if block["type"] == "text":
                    text = block["text"]["content"]
                    # Modified regex to better handle markdown links
                    parts = re.split(r'\[([^\]]+)\]\(([^)\s]+)[^)]*\)', text)
                    
                    for i in range(0, len(parts), 3):
                        # Add regular text
                        if parts[i]:
                            final_blocks.append({
                                "type": "text",
                                "text": {
                                    "content": parts[i].strip()
                                }
                            })
                        
                        # Add link if there is one and URL is valid
                        if i + 2 < len(parts):
                            link_text = parts[i + 1]
                            url = clean_url(parts[i + 2])
                            
                            if url:  # Only add link if URL is valid
                                final_blocks.append({
                                    "type": "text",
                                    "text": {
                                        "content": link_text,
                                        "link": {
                                            "url": url
                                        }
                                    }
                                })
                            else:  # If URL is invalid, just add the text without link
                                final_blocks.append({
                                    "type": "text",
                                    "text": {
                                        "content": link_text
                                    }
                                })
                else:
                    final_blocks.append(block)
            return final_blocks
        
        # Process text first, then links
        text_processed = process_text(text)
        rich_text_blocks = process_links(text_processed)
        
        return rich_text_blocks

    def create_paragraph_block(text):
        # Split text if it's too long
        if len(text) > 1900:
            text = text[:1900]
        
        return {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": parse_markdown_text(text.strip())
            }
        }
    
    def convert_to_notion_blocks(markdown_text):
        blocks = []
        # Split content into lines for processing
        lines = markdown_text.split('\n')
        current_text = ""
        
        for line in lines:
            # Skip horizontal rules
            if line.strip() == '---':
                continue
            
            # Handle headers (remove 'H2:' prefix if present)
            if line.startswith('# '):
                if current_text:
                    blocks.append(create_paragraph_block(current_text))
                    current_text = ""
                header_text = line[2:].strip()
                if header_text.startswith('H2: '):
                    header_text = header_text[4:]
                blocks.append({
                    "object": "block",
                    "type": "heading_1",
                    "heading_1": {
                        "rich_text": parse_markdown_text(header_text, "heading_1")
                    }
                })
            elif line.startswith('## '):
                if current_text:
                    blocks.append(create_paragraph_block(current_text))
                    current_text = ""
                header_text = line[3:].strip()
                if header_text.startswith('H2: '):
                    header_text = header_text[4:]
                blocks.append({
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": parse_markdown_text(header_text, "heading_2")
                    }
                })
            # Handle bullet points
            elif line.strip().startswith('- '):
                if current_text:
                    blocks.append(create_paragraph_block(current_text))
                    current_text = ""
                blocks.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        "rich_text": parse_markdown_text(line[2:].strip(), "bulleted_list_item")
                    }
                })
            # Handle empty lines
            elif not line.strip():
                if current_text:
                    blocks.append(create_paragraph_block(current_text))
                    current_text = ""
            # Regular text
            else:
                if current_text:
                    current_text += "\n"
                current_text += line
        
        # Add any remaining text
        if current_text:
            blocks.append(create_paragraph_block(current_text))
        
        return blocks
    
    # Convert markdown to Notion blocks
    children_blocks = convert_to_notion_blocks(markdown_content)
    
    # Define the data structure for the new page
    new_page_data = {
        "parent": {"database_id": database_id},
        "icon": {
            "emoji": "📊"
        },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": f"Tweet Analysis - {timestamp}"
                        }
                    }
                ]
            }
        },
        "children": children_blocks
    }

    # Use the Notion client to create a new page
    try:
        response = notion.pages.create(**new_page_data)
        logging.info(f"Successfully created a new page in Notion: {response['url']}")
        return response['url']
    except Exception as e:
        logging.error(f"Failed to create a new page in Notion: {e}")
        return None

def lambda_handler(event, context):
    """AWS Lambda handler function"""
    try:
        # Get the Notion page ID from environment variables
        page_id = os.environ.get('NOTION_PAGE_ID')
        if not page_id:
            raise ValueError("NOTION_PAGE_ID environment variable is not set")
        
        # Fetch and process data
        blocks = fetch_page_blocks(page_id)
        output = process_notion_data(blocks)
        apify_input = transform_to_apify_input(output)
        
        # Run Apify and get content
        markdown_content = run_apify_actor(apify_input, output)
        if not markdown_content:
            raise ValueError("No markdown content generated from Apify actor")
        
        # Create Notion entry
        notion_url = create_notion_entry(markdown_content)
        if not notion_url:
            raise Exception("Failed to create Notion entry")
            
        # Return success response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Success',
                'notion_url': notion_url
            })
        }
            
    except Exception as e:
        logger.error(f"Error in lambda_handler: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error: {str(e)}'
            })
        }

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# For local testing
if __name__ == "__main__":
    logging.info("Starting local execution...")
    try:
        result = lambda_handler({}, None)
        if result['statusCode'] == 200:
            logging.info("Execution completed successfully")
        else:
            logging.error(f"Execution failed with status code {result['statusCode']}")
    except Exception as e:
        logging.error(f"Execution failed with error: {str(e)}")
    logging.info("Local execution finished")  