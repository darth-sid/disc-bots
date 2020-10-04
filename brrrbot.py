import os, random, discord, time
import json, requests, base64, gzip, io, nbt
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISC_TOKEN3')

client = discord.Client()

url = 'https://api.hypixel.net/Skyblock/profile?key=bb68c806-f390-42d1-863b-e465fccd5223&profile={uuid}'

global profiles

rarities = {'c':'f','u':'a','r':'9','e':'5'}
color = {'f':':white_circle:','a':':green_circle:','9':':blue_circle:','5':':purple_circle:'}

with open('ids.txt', 'r') as ids:
    content = ids.read()
    profiles = eval(content)

def get_UUID(name):
    data = requests.get('https://api.mojang.com/users/profiles/minecraft/'+name).json()
    UUID = data['id']
    return UUID

def decode_inventory_data(raw):
   inv_data = nbt.nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(raw)))
   return inv_data

def get_skyblock(stat, msg):
    api = url.format(key=profiles[msg.author.id][1],uuid=profiles[msg.author.id][2])
    print(api)
    api_data = requests.get(api)
    skyblock_data = api_data.json()['profile']['members'][profiles[msg.author.id][2]][stat]
    return skyblock_data

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content[0:5] == '!link':
        text = message.content[6:len(message.content)]
        usr, api_key = text.split(',')
        uuid = get_UUID(usr)
        profiles[message.author.id] = [usr,api_key,uuid]
        with open('ids.txt','w') as ids:
            ids.write(str(profiles))
    if message.content == '!acct':
        try:
            await message.channel.send(profiles[message.author.id])
        except KeyError:
            await message.channel.send('No account linked yet')
    if message.content[0:6] == '!stats':
        data = get_skyblock('stats',message)
        try:
            await message.channel.send(data[message.content[7:len(message.content)]])
        except KeyError:
            await message.channel.send('invalid stat')
    if message.content[0:10] == '!talismans':
        data = get_skyblock('talisman_bag',message)
        talismans = decode_inventory_data(data['data'])
        rarity = None
        
        try:
            rarity = message.content[11]  
        except IndexError:
            pass
        if rarity:
            msg = ""
            for i in range(len(talismans[0])-1):
                print(talismans[0][1])
                if talismans[0][i]['tag']['display']['Name'][1] == rarities[rarity]:
                    try:
                        talisman = talismans[0][i]['tag']['display']['Name']
                        msg += color[talisman[1]] + talisman[2:len(talisman)]
                        msg += '\n'
                    except KeyError:
                        break


        else:
            msg = ""
            for i in range(len(talismans[0])-1):
                try:
                    talisman = talismans[0][i]['tag']['display']['Name']
                    msg += color[talisman[1]] + talisman[2:len(talisman)]
                    msg += '\n'
                except KeyError:
                    break
            print(msg)
            await message.channel.send(msg)

client.run(TOKEN)
