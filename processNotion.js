require('dotenv').config();
const { Client } = require('@notionhq/client');
const fs = require('fs');

// Initialize the Notion client
const notion = new Client({ auth: process.env.NOTION_API_KEY });

// Function to fetch data from Notion
async function fetchNotionData(databaseId) {
    try {
        const response = await notion.databases.query({ database_id: databaseId });
        return response.results;
    } catch (error) {
        console.error('Error fetching data from Notion:', error);
        return [];
    }
}

// Function to process the fetched data
function processNotionData(blocks) {
    const output = {
        profile: '',
        interests: [],
        accounts_to_follow: []
    };

    let currentSection = '';

    blocks.forEach(block => {
        const type = block.type;
        const content = block[type]?.rich_text?.map(text => text.plain_text).join(' ') || '';

        if (type === 'heading_2') {
            if (content.toLowerCase() === 'profile') {
                currentSection = 'profile';
            } else if (content.toLowerCase() === 'interests') {
                currentSection = 'interests';
            } else if (content.toLowerCase() === 'accounts to follow') {
                currentSection = 'accounts_to_follow';
            }
        } else if (type === 'paragraph' && currentSection) {
            if (currentSection === 'profile') {
                output.profile += content + ' ';
            } else {
                output[currentSection].push(content);
            }
        }
    });

    return output;
}

// Main function to execute the process
async function main() {
    const databaseId = process.env.NOTION_DATABASE_ID; // Ensure this is set in your .env file
    const blocks = await fetchNotionData(databaseId);
    const output = processNotionData(blocks);

    fs.writeFile('output.json', JSON.stringify(output, null, 4), err => {
        if (err) {
            console.error('Error writing file:', err);
            return;
        }
        console.log('Output written to output.json');
    });
}

main();