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

2. Create a Virtual Environment
   ```bash
   python -m venv venv
   ```

3. Activate the Virtual Environment
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install
   ```bash
   pip install -r requirements.txt
   ```

5. Token:
   Open `bot.py` and replace `'YOUT_BOT_TOKEN'` with your actual bot token from discord.dev

6. Run:
   ```bash
   python bot.py
   ```