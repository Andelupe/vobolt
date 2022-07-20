import discord
import os
import asyncio
from replit import db
from keep_alive import keep_alive

client = discord.Client()
db["responding"] = [True]

def update_events(event_idea):
  events = db["events"]
  events.append(event_idea)
  db["events"] = events

def delete_event(index):
  if "events" in db.keys():
    events = db["events"]
    if len(events) > index:
      del events[index]
      db["events"] = events

# !v commands
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith('$thumb'):
    channel = message.channel
    await channel.send('Send me that 👍 reaction, mate')

    def check(reaction, user):
      return user == message.author and str(reaction.emoji) == '👍'

    try:
      reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
    except asyncio.TimeoutError:
      await channel.send('👎')
    else:
      await channel.send('👍')
  
  if db["responding"]:
    if msg.startswith("!v newidea"):
      event_idea = msg.split("!v newidea ", 1)[1]
      update_events(event_idea)
      await message.channel.send("New volunteering suggestion added.")
  
    if msg.startswith("!v eventideas"):
      list = "``` "
      events = db["events"]
      for x in events:
        list = list + str(events.index(x) + 1) + ". " + x + "  "
      await message.channel.send(list + "```")
      
  # $ admin site
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]
    if value.lower() == "true" or value.lower() == "on":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    elif value.lower() == "status":
      if db["responding"] == True:
        await message.channel.send("Responding is on.")
      else:
        await message.channel.send("Responding is off.")
    else: 
      db["responding"] = False
      await message.channel.send("Responding is off.")

  if msg.startswith("$del event"):
    events = []
    list = ""
    if "events" in db.keys():
      index = int(msg.split("$del event",1)[1])
      delete_event(index - 1)
      events = db["events"]
    for x in events:
      list = list + str(events.index(x) + 1) + ". " + x + "_ _"
    await message.channel.send(list)

  if msg.startswith("$clearlist"):
    db["events"] = ["Food Bank"]
    await message.channel.send("Event list has been cleared.")

keep_alive()
client.run(os.getenv('bot_token'))
