import discord
import pytz
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

cities = [
    ("New York", "America/New_York"),
    ("London", "Europe/London"),
    ("Tokyo", "Asia/Tokyo"),
    ("Sydney", "Australia/Sydney")
]

@client.event
async def on_ready():
    print('Bot giriş yaptı: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!saat'):
        response = ""
        for city in cities:
            city_name = city[0]
            timezone = pytz.timezone(city[1])
            now = datetime.now()
            localized_time = now.astimezone(timezone)
            time_str = localized_time.strftime('%Y-%m-%d %H:%M:%S')
            response += f"{city_name}: {time_str}\n"
        
        await message.channel.send(response)

client.run('MTExODIzMTk1NjY2MDk1MzA5OA.Gn1kva.Nqxlv8GlHFmQvsUdjwtHEpVWtM0u_kcY9HbbbU')



