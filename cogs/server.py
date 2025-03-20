import discord
from discord import app_commands
from discord.ext import commands

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="serverinfo", description="Get information about the server.")
    async def server_info(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild:
            embed = discord.Embed(title=f"Server Info: {guild.name}", color=discord.Color.blue())
            embed.add_field(name="Owner", value=guild.owner, inline=False)
            embed.add_field(name="Member Count", value=guild.member_count, inline=False)
            embed.add_field(name="Created At", value=guild.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
            embed.set_thumbnail(url=guild.icon.url if guild.icon else None)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("This command can only be used in a server.")

    @app_commands.command(name="roles", description="List all roles in the server.")
    async def roles(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild:
            roles = [role.name for role in guild.roles if role.name != "@everyone"]
            roles_list = ", ".join(roles) if roles else "No roles available."
            await interaction.response.send_message(f"Roles in this server: {roles_list}")
        else:
            await interaction.response.send_message("This command can only be used in a server.")

    @app_commands.command(name="boosts", description="Get the number of server boosts and boost level.")
    async def boosts(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild:
            await interaction.response.send_message(
                f"This server has {guild.premium_subscription_count} boosts and is at level {guild.premium_tier}."
            )
        else:
            await interaction.response.send_message("This command can only be used in a server.")

    @app_commands.command(name="channels", description="Get the number of text and voice channels in the server.")
    async def channels(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild:
            text_channels = len([channel for channel in guild.channels if isinstance(channel, discord.TextChannel)])
            voice_channels = len([channel for channel in guild.channels if isinstance(channel, discord.VoiceChannel)])
            await interaction.response.send_message(
                f"This server has {text_channels} text channels and {voice_channels} voice channels."
            )
        else:
            await interaction.response.send_message("This command can only be used in a server.")

    @app_commands.command(name="invite", description="Generate an invite link for the server.")
    async def invite(self, interaction: discord.Interaction):
        guild = interaction.guild
        if guild:
            if interaction.user.guild_permissions.create_instant_invite:
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).create_instant_invite:
                        invite = await channel.create_invite(max_age=3600, max_uses=1)
                        await interaction.response.send_message(f"Here is your invite link: {invite.url}")
                        return
                await interaction.response.send_message("I couldn't create an invite link.")
            else:
                await interaction.response.send_message("You do not have permission to create an invite link.")
        else:
            await interaction.response.send_message("This command can only be used in a server.")

async def setup(bot):
    await bot.add_cog(Server(bot))