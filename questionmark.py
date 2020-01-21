import discord
import random
from discord.ext import commands

#bots name and command prefix
client = commands.Bot(command_prefix = '.')

#events that the bot will react to

#bot ready confirmation to terminal upon launch
@client.event
async def on_ready():
    print('Bot is ready.')

#invalid command error message
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command')

#message upon member join on the server   
@client.event
async def on_member_join(member):
    print(f'```{member} has joined the server.```')

#message upon member remove from the server
@client.event
async def on_member_remove(member):
    print(f'```{member} has left the server.```')
    
#commands that the bot will react to

#wowprog        
@client.command()
async def wowprog(ctx):
    await ctx.send('https://www.wowprogress.com/guild/eu/kazzak/Project+Questionmark')

#youtube
@client.command()
async def youtube(ctx):
    await ctx.send('https://www.youtube.com/channel/UC2xDXOpNdGCeTeuoT6wCBVg?view_as=subscriber')


#dm  
@client.command()
async def dm(ctx):
    await ctx.author.send('```This is a DM command```')

#ping
@client.command()
async def ping(ctx):
    await ctx.send(f'```Pong! {round(client.latency * 1000)}ms```')

#command list
@client.command(aliases=['commands'])
async def command(ctx):
    await ctx.send(f'```--- Command List ---\n .youtube Links our kill videos youtube channel\n .wowprog Links our wowprogress page\n .ping Shows the bots current ping\n .8ball + Question will get you a sure answer to put your faith on.\n .author Information about my creator.```')
    
    

#8 ball of fortune
@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
    responses = [   'As I see it, yes.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Don’t count on it.',
                    'It is certain.',
                    'It is decidedly so.',
                    'Most likely.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Outlook good.',
                    'Reply hazy, try again.',
                    'Signs point to yes.',
                    'Very doubtful.',
                    'Without a doubt.',
                    'Yes.',
                    'Yes – definitely.',
                    'You may rely on it.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    
#Reaction based roling - add role upon reaction to message
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    #Change the message ID here to the one u want the bot to take the reactions from.
    if message_id == 667051027933167650:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        #use this part only if the role and emoji name's are different, replace "emojiname" and "rolename"
        if payload.emoji.name == 'emojiname':
            role = discord.utils.get(guild.roles, name='rolename')
        
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
                print("done")
            else:
                print("Member not found")
        else:
            print("Role not found")
                                 
        
#Reaction based roling - Delete role upon reaction delete
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 667051027933167650:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        #use this part only if the role and emoji name's are different, replace "emojiname" and "rolename"
        if payload.emoji.name == 'emojiname':
            role = discord.utils.get(guild.roles, name='rolename')
        
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                print("done")
            else:
                print("Memb not found")
        else:
            print("Role not found")
    

#Runs the client. This part always be at the VERY end of the code
client.run('***')
