import discord
import os
from keep_alive import keep_alive

class MyClient(discord.Client):
  def __innit__(self, *args, **kwargs):
    super().__innit__(*args, **kwargs)
    
    
  async def on_ready(self):
    print('Ready')

  async def on_raw_reaction_add(self, payload):
    target_message_id = 999348282117603520
    if payload.message_id != target_message_id:
      return

    guild = client.get_guild(payload.guild_id)
    if payload.emoji.name == '🍏':
      role = discord.utils.get(guild.roles, name = 'senior')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '📘':
      role = discord.utils.get(guild.roles, name = 'junior')
      await payload.mem0ber.add_roles(role)
    elif payload.emoji.name == '💖':
      role = discord.utils.get(guild.roles, name = 'sophomore')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '🐠':
      role = discord.utils.get(guild.roles, name = 'freshmen')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '🐯':
      role = discord.utils.get(guild.roles, name = 'consol')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '🐱':
      role = discord.utils.get(guild.roles, name = 'purple school')
      await payload.member.add_roles(role)

  async def on_raw_reaction_remove(self, payload):
    target_message_id = 999348282117603520
    if payload.message_id != target_message_id:
      return
      
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if payload.emoji.name == '🍏':
      role = discord.utils.get(guild.roles, name = 'senior')
      await member.remove_roles(role)
    elif payload.emoji.name == '📘':
      role = discord.utils.get(guild.roles, name = 'junior')
      await member.remove_roles(role)
    elif payload.emoji.name == '💖':
      role = discord.utils.get(guild.roles, name = 'sophomore')
      await member.remove_roles(role)
    elif payload.emoji.name == '🐠':
      role = discord.utils.get(guild.roles, name = 'freshmen')
      await member.remove_roles(role)
    elif payload.emoji.name == '🐯':
      role = discord.utils.get(guild.roles, name = 'consol')
      await member.remove_roles(role)
    elif payload.emoji.name == '🐱':
      role = discord.utils.get(guild.roles, name = 'purple school')
      await member.remove_roles(role)

  async def on_message(self, message):
    if message.author == client.user:
      return
    channel = message.channel
    await channel.send("**" + "React to recieve your roles:" + "**" + "\n🍏senior\n📘junior\n💖sophomore\n🐠freshmen\n🐯consol\n🐱purple school")
      
    
intents = discord.Intents.default()
intents.members = True
    
client = MyClient(intents=intents)
keep_alive()
client.run(os.getenv('bot_token'))
