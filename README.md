# Discord.py Boilerplate

A modular starter template for building Discord bots with the `discord.py` library.

## Project Structure

```
discord.py-boilerplate/
├── cogs/             # Modular bot commands and events
│   ├── server.py     # Server-related commands
│   ├── events.py     # Event listeners
├── bot.py            # Main bot file
├── requirements.txt  # Dependencies
├── README.md         # Project documentation
```

## Setup

1. **Clone**
   ```bash
   git clone https://github.com/bianchi-ed/discord.py-template
   cd discord.py-template
   ```

2. **Create and Activate a Virtual Environment**

   Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   macOS/Linux:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Token**

   Open `bot.py` and replace `'YOUT_BOT_TOKEN'` with your bot token from [Discord Developer Portal](https://discord.com/developers/applications).

5. **Run**
   ```bash
   python bot.py
   ```