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
    if payload.emoji.name == '🥶':
      role = discord.utils.get(guild.roles, name = ':cold_face:')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '😹':
      role = discord.utils.get(guild.roles, name = ':joy_cat:')
      await payload.member.add_roles(role)
    elif payload.emoji.name == '😭':
      role = discord.utils.get(guild.roles, name = ':sob:')
      await payload.member.add_roles(role)

  async def on_raw_reaction_remove(self, payload):
    target_message_id = 999348282117603520
    if payload.message_id != target_message_id:
      return
      
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    if payload.emoji.name == '🥶':
      role = discord.utils.get(guild.roles, name = ':cold_face:')
      await member.remove_roles(role)
    elif payload.emoji.name == '😹':
      role = discord.utils.get(guild.roles, name = ':joy_cat:')
      await member.remove_roles(role)
    elif payload.emoji.name == '😭':
      role = discord.utils.get(guild.roles, name = ':sob:')
      await member.remove_roles(role)
      
    
intents = discord.Intents.default()
intents.members = True
    
client = MyClient(intents=intents)
keep_alive()
client.run(os.getenv('bot_token'))
