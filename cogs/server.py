import discord
from discord import app_commands
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # server info
    @app_commands.command(name="serverinfo", description="Get information about the server.")
    async def server_info(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(title=f"Server Info: {guild.name}", color=discord.Color.blue())
        embed.add_field(name="Owner", value=guild.owner, inline=False)
        embed.add_field(name="Member Count", value=guild.member_count, inline=False)
        embed.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
        await interaction.response.send_message(embed=embed)

    # new invite link
    @app_commands.command(name="invite", description="Generate an invite link for the server.")
    async def invite(self, interaction: discord.Interaction):
        guild = interaction.guild
        if interaction.user.guild_permissions.create_instant_invite:
            for channel in guild.text_channels:
                if channel.permissions_for(guild.me).create_instant_invite:
                    invite = await channel.create_invite(max_age=3600, max_uses=1)
                    await interaction.response.send_message(f"Here is your single use invite: {invite.url}")
                    return
            await interaction.response.send_message("I couldn't create an invite link.")
        else:
            await interaction.response.send_message("You do not have permission to create an invite link.")

async def setup(bot):
    await bot.add_cog(Server(bot))