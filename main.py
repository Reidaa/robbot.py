import os
import re
import asyncio

import discord
from dotenv import load_dotenv

load_dotenv()

from src.reddit.manga import search_manga
from src.disc.Bot import MyBot

FEATURES = ["weeb"]
WEEB_CHANNEL = [

]

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.presences = True
intents.members = True
bot = MyBot(gintents=intents)


@bot.tree.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hi, {interaction.user.mention}")

@bot.tree.command()
@discord.app_commands.describe(
    title="Title of the manga"
)
async def manga(interaction: discord.Interaction, title: str):
    result = await search_manga(title)

    if result:
        await interaction.response.send_message(f"{result['title']}: {result['link']}")
    else:
        await interaction.response.send_message(f"Did not found the manga {interaction.user.mention}")

@bot.tree.command()
@discord.app_commands.describe(
    feature=f"Try to to enable a feature on this channel"
)
async def enable(interaction: discord.Interaction, feature: str):
    channel = interaction.channel
    channel_id = interaction.channel_id
    if feature not in FEATURES:
        return await interaction.response.send_message(f"Features not found")
    else:
        WEEB_CHANNEL.append(channel_id)
        return await interaction.response.send_message(f"Feature recognized, enabling **{feature}** on __{channel}__")

bot.run(os.getenv("TOKEN"))
