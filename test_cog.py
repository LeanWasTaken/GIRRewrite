import discord
from discord.ext import commands
from discord import app_commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @app_commands.guilds(846383887973482516)
    @app_commands.command(description="Says hello to the user")
    @app_commands.describe(message="The message to send back")
    async def say(self, interaction: discord.Interaction, message: str):
            await interaction.response.send_message(message)

def setup(bot: commands.Bot):
    bot.add_cog(Greetings(bot))