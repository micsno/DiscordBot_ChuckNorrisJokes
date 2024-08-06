import discord
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

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
        return "Could not retrieve a joke for this category. Make sure the category is valid."

# Function to search for jokes with a specific query
def search_jokes(query):
    response = requests.get(f'https://api.chucknorris.io/jokes/search?query={query}')
    if response.status_code == 200:
        jokes = response.json().get('result')
        if jokes:
            return '\n'.join([joke.get('value') for joke in jokes])
        else:
            return "No jokes found for this query."
    else:
        return "Could not perform search at this time."

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == '!chucknorris':
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
