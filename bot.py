import discord
import keep_alive
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
load_dotenv()
BOT_TOKEN = os.environ['BOT_TOKEN']
SERVER_ID = int(os.environ['SERVER_ID'])
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)
user_message_counts = {}
keep_alive.keep_alive()  
@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="Aaryav")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'')
    print('')
@bot.event
async def on_member_join(member):
    if member.guild.id == SERVER_ID:
        welcome_message = f""
        welcome_embed = discord.Embed(
            title=f"",
            description=welcome_message,
            color=0x000000 
        )
        welcome_embed.set_image(url='')
        await member.send(embed=welcome_embed)
@bot.event
async def on_message(message):
    if message.guild is not None:
        if message.guild.id == SERVER_ID:
            user_id = message.author.id
            if user_id not in user_message_counts:
                user_message_counts[user_id] = 1
                welcome_message = f""
                welcome_embed = discord.Embed(
                    title=f"",
                    description=welcome_message,
                    color=0x000000
                )
                welcome_embed.set_image(url='')
                await message.author.send(embed=welcome_embed)
            else:
                user_message_counts[user_id] += 1
            if user_message_counts[user_id] == 10:
                congrats_embed_10 = discord.Embed(
                    title="",
                    description= f"",
                    color=0x000000
                )
                congrats_embed_10.set_image(url='')
                await message.author.send(embed=congrats_embed_10)
                last_message_time = message.created_at - timedelta(hours=24)
                if message.created_at < last_message_time:
                    user_message_counts[user_id] = 0
            if user_message_counts[user_id] == 30:
                congrats_embed_30 = discord.Embed(
                    title="",
                    description= f"",
                    color=0x000000
                )
                congrats_embed_30.set_image(url='')
                await message.author.send(embed=congrats_embed_30)
                last_message_time = message.created_at - timedelta(hours=24)
                if message.created_at < last_message_time:
                    user_message_counts[user_id] = 0
            if user_message_counts[user_id] == 100:
                congrats_embed_100 = discord.Embed(
                    title="",
                    description= f"",
                    color=0x000000  # You can customize the color here
                )
                congrats_embed_100.set_image(url='')  # Replace with your 100 message image URL

                # Send the congratulations embed with the 100 message image
                await message.author.send(embed=congrats_embed_100)

                # Reset the message count for the user after 24 hours from their last message
                last_message_time = message.created_at - timedelta(hours=24)
                if message.created_at < last_message_time:
                    user_message_counts[user_id] = 0

    await bot.process_commands(message)

bot.run(BOT_TOKEN)
