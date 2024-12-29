import os
import json
import logging
from notion_client import Client
from apify_client import ApifyClient
from dotenv import load_dotenv
import datetime
import openai

# Load environment variables from .env file
load_dotenv()

# Configure logging to focus on Apify-related messages
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Notion client
notion = Client(auth=os.getenv('NOTION_API_KEY'))

# Initialize the Apify client with your API token
apify_client = ApifyClient(os.getenv('APIFY_API_TOKEN'))

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
    start_date = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime('%Y-%m-%d')

    apify_input = {
        "customMapFunction": "(object) => { return {...object} }",
        "includeSearchTerms": True,
        "maxItems": 200,
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

# Function to run the Apify actor task using the Apify client
def run_apify_actor(apify_input, output):
    logging.info('Starting Apify actor task run...')
    start_time = datetime.datetime.now()  # Record the start time
    try:
        # Run the Actor task and wait for it to finish
        run = apify_client.task("gksWpvaHUIAV3fIBa").call(task_input=apify_input)

        # Create the jsons/outputs directory if it doesn't exist
        os.makedirs('jsons/outputs', exist_ok=True)

        # Generate the filename with the format 'yyyymmdd_hhmm_{numb. of results}.json'
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y%m%d_%H%M')

        # Fetch Actor task results from the run's dataset (if there are any)
        results = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
        num_results = len(results)
        filename = f'jsons/outputs/{timestamp}_{num_results}.json'

        # Sort the results by likeCount in descending order
        sorted_results = sorted(results, key=lambda x: x.get('likeCount', 0), reverse=True)

        # Extract profile information from Notion data
        profile = output['profile']

        # Extract interests information from Notion data
        interests = output['interests']

        # Summarize the tweets with profile and interests information
        summary = summarize_tweets(sorted_results, profile, interests)
        logging.info(f'Summary of tweets: {summary}')

        # Generate the filename for the markdown file
        md_filename = f'jsons/outputs/{timestamp}_{num_results}.md'

        # Save the markdown summary to a .md file without code block markers
        with open(md_filename, 'w') as md_file:
            md_file.write(summary.replace('```markdown', '').replace('```', '').strip())

        # Create a dictionary with the summary and tweets
        output_data = {
            "summary": summary,
            "tweets": sorted_results
        }

        # Save the output data to a JSON file
        with open(filename, 'w') as f:
            json.dump(output_data, f, indent=4)

    except Exception as e:
        logging.error(f'Error running Apify actor task: {e}')
    finally:
        end_time = datetime.datetime.now()  # Record the end time
        duration = end_time - start_time  # Calculate the duration
        logging.info(f'Apify actor task completed in {duration}')  # Print the duration

def summarize_tweets(tweets, profile, interests):
    # Prepare the text to be summarized
    tweet_texts = [tweet['text'] for tweet in tweets if 'text' in tweet]
    combined_text = "\n".join(tweet_texts)

    # Create the prompt with profile and interests information
    assistant_prompt = (
        f"You are a skilled research assistant tasked with generating tweet summaries tailored to a specific persona. "
        f"The persona is identified as {profile}, with expressed interests including: {interests}.\n\n"
        "Your goal is to curate the most insightful, relevant, and engaging information from the provided tweets, "
        "ensuring the content aligns with the persona's stated interests.\n"
        "Important: Do not write as if you are the persona. Instead, focus on covering the topics and themes "
        "that align with their interests.\n\n"
        "Each summary should include:\n"
        "- A clear and concise overview of the key points.\n"
        "- Citations for the most impactful or referenced tweets.\n"
        "- A cohesive narrative tying the tweets together, emphasizing the topics of interest.\n\n"
        "The final output must be structured as an article in markdown format, "
        "with appropriate headings, bullet points, and citations.\n\n"
        "Do not include any code block markers in the output.\n\n"
        "At the beginning you shold include something like this: Information taken from analysis of X ammount of tweets\n"
        f"Tweets:\n{combined_text}"
    )


    user_prompt = (
        f"Summarize the tweets for the persona {profile}.\n\n"
        f"Tweets:\n{combined_text}"
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

# Main function to execute the process
def main(event, context):
    # Your Lambda function code here
    print("Event:", event)
    print("Context:", context)
    # Add your logic here

if __name__ == "__main__":
    # This part won't be used in Lambda, but can be useful for local testing
    main({}, {}) 