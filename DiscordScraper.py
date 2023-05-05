import discord
import asyncio
from datetime import datetime
import pytz

file_path = "{file path}"

client = discord.Client(intents=discord.Intents.all())
channel_id =  # Replace with the channel ID must be integer
user_id =  # Replace with the user ID must be integer
timezone = 'US/Eastern' # Replace with Timezone
cutoff_date = pytz.timezone(timezone).localize(datetime(2021, 1, 1)) # Replace with cutoff date Format (YYYY, M, D)

@client.event
async def on_ready():
    print('Ready to Log'.format(client))

    channel = client.get_channel(channel_id)
    messages = []
    async for message in channel.history(limit=1000):
        messages.append(message)

    with open('log.txt', 'a', encoding='utf-8') as f:
        for message in messages:
            if message.channel.id == channel_id and message.author.id == user_id and message.created_at >= cutoff_date:
                f.write(f'{message.created_at}: {message.content}\n')
        print('Logging Done')
        exit()

client.run('Token') #Enter your discord bot token here