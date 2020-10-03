import os, random, discord
import dotenv

dotenv.load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN2')

client = discord.Client()

blue = ':blue_square:'
red = ':red_square:'
inno = ':black_large_square:'
deth = ':skull:'
fiftyfifty = random.randrange(1,2)
if fiftyfifty == 1:
    redblue = red
elif fiftyfifty == 2:
    redblue = blue

@client.event
async def on_ready():
    print('ready')


board = []
spymaster_board = [blue,red,inno,blue,red,inno,blue,red,inno,blue,red,inno,blue,red,inno,blue,red,inno,blue,red,inno,blue,red,deth,redblue]
random.shuffle(spymaster_board)
@client.event
async def on_message(message):
    global board
    global spymaster_board
    if message.author == client.user:
        return

    if message.content == '!first':
        await message.channel.send(redblue)

    if message.content[0:5] == '!word':
        end = len(message.content)
        board.append(message.content[6:end])

    if message.content == '!board':
        if len(board) == 25:
            msg = '[**'+board[0]+'**][**'+board[1]+'**][**'+board[2]+'**][**'+board[3]+'**][**'+board[4]+'**]\n[**'+board[5]+'**][**'+board[6]+'**][**'+board[7]+'**][**'+board[8]+'**][**'+board[9]+'**]\n[**'+board[10]+'**][**'+board[11]+'**][**'+board[12]+'**][**'+board[13]+'**][**'+board[14]+'**]\n[**'+board[15]+'**][**'+board[16]+'**][**'+board[17]+'**][**'+board[18]+'**][**'+board[19]+'**]\n[**'+board[20]+'**][**'+board[21]+'**][**'+board[22]+'**][**'+board[23]+'**][**'+board[24]+'**]'

        else:
            diff = 25 - len(board)
            msg = 'add ' + str(diff) + ' more words'
        await message.channel.send(msg)
    
    if message.content == '!spyboard':
        spyboard = spymaster_board[0]+spymaster_board[1]+spymaster_board[2]+spymaster_board[3]+spymaster_board[4]+'\n'+spymaster_board[5]+spymaster_board[6]+spymaster_board[7]+spymaster_board[8]+spymaster_board[9]+'\n'+spymaster_board[10]+spymaster_board[11]+spymaster_board[12]+spymaster_board[13]+spymaster_board[14]+'\n'+spymaster_board[15]+spymaster_board[16]+spymaster_board[17]+spymaster_board[18]+spymaster_board[19]+'\n'+spymaster_board[20]+spymaster_board[21]+spymaster_board[22]+spymaster_board[23]+spymaster_board[24]
        await message.channel.send(spyboard)

    if message.content[0:6] == '!guess':
        l = len(message.content)
        gess = message.content[7:l]
        for i in (range(25)):
            if gess == board[i]:
                board[i] = spymaster_board[i]
                await message.channel.send(spymaster_board[i])

    if message.content == '!reset':
        board = []
        random.shuffle(spymaster_board)

    if message.content == '!timer':
        pass

                
client.run(TOKEN)
