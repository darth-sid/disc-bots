import os, random, discord, dotenv

dotenv.load_dotenv()
TOKEN = os.getenv('POG_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('gaymer')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[0:1] == '$':
        pass
        if message.content[1:10]=='tictactoe':
            player1 = message.author.id
            player2 = message.mentions[0].id
            msg = await message.channel.send(":black_large_square::black_large_square::black_large_square:\n:black_large_square::black_large_square::black_large_square:\n:black_large_square::black_large_square::black_large_square:\n")
            await message.channel.add_reaction(':one:')



client.run(TOKEN)
