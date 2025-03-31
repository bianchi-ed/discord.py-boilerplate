import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from bot itself
        if message.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after):
        added = [emoji for emoji in after if emoji not in before]
        removed = [emoji for emoji in before if emoji not in after]
        updated = [emoji for emoji in after if emoji in before and emoji.name != next(e.name for e in before if e.id == emoji.id)]

        for emoji in added:
            print(f"Emoji added: {emoji.name} (id: {emoji.id}) in guild {guild.name}")

        for emoji in removed:
            print(f"Emoji removed: {emoji.name} (id: {emoji.id}) in guild {guild.name}")

        for emoji in updated:
            print(f"Emoji updated: {emoji.name} (id: {emoji.id}) in guild {guild.name}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member.name} has joined the server {member.guild.name}.")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member.name} has left the server {member.guild.name}.")

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        print(f"Role created: {role.name} in guild {role.guild.name}.")

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        print(f"Role deleted: {role.name} in guild {role.guild.name}.")

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        print(f"Role updated: {before.name} -> {after.name} in guild {before.guild.name}.")

async def setup(bot):
    await bot.add_cog(Events(bot))