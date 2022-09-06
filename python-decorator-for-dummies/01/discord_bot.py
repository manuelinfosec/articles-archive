import discord
client = discord.Client(intents=intents)

@client.event # take note of this line
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event # take note of this line
async def on_message(msg):
    if msg.content == "":
        pass
# ... SOME MORE CODE ...