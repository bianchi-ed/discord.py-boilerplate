import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        added = [emoji for emoji in after if emoji not in before]
        removed = [emoji for emoji in before if emoji not in after]
        updated = [emoji for emoji in after if emoji in before and emoji.name != next(e.name for e in before if e.id == emoji.id)]

        for emoji in added:
            print(f"Emoji added: {emoji.name} ({emoji.id}) in guild {guild.name}")

        for emoji in removed:
            print(f"Emoji removed: {emoji.name} ({emoji.id}) in guild {guild.name}")

        for emoji in updated:
            print(f"Emoji updated: {emoji.name} ({emoji.id}) in guild {guild.name}")    

async def setup(bot):
    await bot.add_cog(Events(bot))