import discord
import requests
import os
import urllib.parse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable receiving message content

# Create the client with intents
client = discord.Client(intents=intents)

# Function to get a random Chuck Norris joke
def get_random_joke():
    response = requests.get('https://api.chucknorris.io/jokes/random')
    if response.status_code == 200:
        joke = response.json().get('value')
        return joke
    else:
        return "Could not retrieve a joke at this time."

# Function to get a list of available categories
def get_categories():
    response = requests.get('https://api.chucknorris.io/jokes/categories')
    if response.status_code == 200:
        categories = response.json()
        return ', '.join(categories)
    else:
        return "Could not retrieve categories at this time."

# Function to get a joke from a specific category
def get_joke_by_category(category):
    response = requests.get(f'https://api.chucknorris.io/jokes/random?category={category}')
    if response.status_code == 200:
        joke = response.json().get('value')
        return joke
    else:
        return f"Could not retrieve a joke for category '{category}'. Make sure the category is valid."

# Function to search for jokes with a specific query
def search_jokes(query):
    # URL-enkoodaa hakusana
    encoded_query = urllib.parse.quote(query)
    
    try:
        response = requests.get(f'https://api.chucknorris.io/jokes/search?query={encoded_query}')
        response.raise_for_status()  # Raises an exception for HTTP errors
        data = response.json()
        jokes = data.get('result')
        if jokes:
            return '\n'.join([joke.get('value') for joke in jokes])
        else:
            return f"No jokes found for '{query}'. Try a different query!"
    except requests.RequestException as e:
        return f"An error occurred: {e}"

# Command help message
help_message = """
**Chuck Norris Jokes Bot Help**

Here are the commands you can use:

- `!chucknorris` - Get a random Chuck Norris joke.
- `!chucknorris category` - Get a list of available joke categories.
- `!chucknorris category [category]` - Get a joke from a specific category. Replace `[category]` with the desired category.
- `!chucknorris search [query]` - Search for jokes that match the query. Replace `[query]` with your search term.

Enjoy the laughs!
"""

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == '!help':
        await message.channel.send(help_message)

    elif message.content.lower() == '!chucknorris':
        joke = get_random_joke()
        await message.channel.send(joke)
    
    elif message.content.lower() == '!chucknorris category':
        categories = get_categories()
        await message.channel.send(f'Available categories: {categories}')
    
    elif message.content.lower().startswith('!chucknorris category '):
        category = message.content[len('!chucknorris category '):].strip()
        joke = get_joke_by_category(category)
        await message.channel.send(joke)
    
    elif message.content.lower().startswith('!chucknorris search '):
        query = message.content[len('!chucknorris search '):].strip()
        jokes = search_jokes(query)
        await message.channel.send(jokes)

client.run(TOKEN)
