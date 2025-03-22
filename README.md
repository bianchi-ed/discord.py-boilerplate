# Discord.py Boilerplate

A boilerplate project for creating Discord bots using the `discord.py` library. 

## Project Structure

```
discord.py-boilerplate/
├── cogs/             # Cogs
│   ├── server.py     # example cog with server info commands
│   ├── events.py     # Event handling cog
├── README.md         # You are reading this
├── requirements.txt  # Dependencies
├── bot.py            # Main bot file

```
## Setup Instructions
1. Clone
   ```bash
   git clone https://github.com/bianchi-ed/discord.py-boilerplate.git
   cd discord.py-boilerplate
   ```

2. Install
   ```bash
   pip install -r requirements.txt
   ```

3. Token:
   - Open `bot.py` and replace `'YOUT_BOT_TOKEN'` with your actual bot token.

4. Run:
   ```bash
   python bot.py
   ```