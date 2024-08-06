# Chuck Norris Joke Bot

This is a simple Discord bot that fetches Chuck Norris jokes from the [Chuck Norris API](https://api.chucknorris.io/). The bot can send random jokes, fetch jokes by category, and perform text search for jokes.

![Screenshot_1](https://github.com/micsno/DiscordBot_ChuckNorrisJokes/blob/main/chucknorris.png)

## Features

- Get a random Chuck Norris joke
- Retrieve available joke categories
- Fetch jokes by a specific category
- Search for jokes using a text query

## Prerequisites

1. **Python**: Ensure Python is installed on your system.
2. **pip**: Python package installer.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/micsno/DiscordBot_ChuckNorrisJokes
    cd ChuckNorrisJokes
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file** in the root of the project and add your Discord bot token:

    ```plaintext
    DISCORD_TOKEN=your_discord_bot_token
    ```

    Replace `your_discord_bot_token` with your actual bot token obtained from the Discord Developer Portal.

5. **Add `.env` to `.gitignore`** to ensure it is not tracked by version control:

    ```plaintext
    .env
    ```

## Configuration

1. **Bot Token**: The bot token should be placed in the `.env` file. 

2. **Permissions**: Ensure that the bot has the required permissions (e.g., Send Messages, Read Message History) to function correctly.

## Running the Bot

1. **Run the bot**:

    ```bash
    python chucknorris.py
    ```

2. **Test the bot**:
    - Add the bot to your server using the OAuth2 URL below.
    - Use the following commands in your Discord server:
        - `!chucknorris` - Get a random Chuck Norris joke.
        - `!chucknorris category` - Retrieve available joke categories.
        - `!chucknorris category [category]` - Fetch a joke from a specific category.
        - `!chucknorris search [query]` - Search for jokes containing the specified query.

## Adding the Bot to a Server

Use the following OAuth2 URL to invite the bot to your Discord server:

[Add Chuck Norris Joke Bot to Your Server](https://discord.com/oauth2/authorize?client_id=1270310213639082058&permissions=67584&integration_type=0&scope=bot)

Replace `1270310213639082058` with your bot's client ID if necessary.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [micsno@pm.me](mailto:micsno@pm.me).
