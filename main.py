#Import Packages
import discord
import os
import json
import asyncio
from webserver import keep_alive
from discord.ext import commands

#Put Your Token In A Secret File
TOKEN = os.getenv("token")

#Read Json
with open('config.json') as f:
	config = json.load(f)

#Define Activity
activitys = config.get("activity")
PLAYTXT = config.get("PLAYING")
LISTXT = config.get("LISTENING")
WATXT = config.get("WATCHING")
STRTXT = config.get("STREAMING")
STRURL = config.get("url")
secs = config.get("second")

#Define Status
STATUSz = config.get("status")
if STATUSz == "online":
	"discord.Status.online"
elif STATUSz == "idle":
	"discord.Status.idle"
elif STATUSz == "dnd":
	"discord.Status.dnd"

#Define Client
client = commands.Bot(command_prefix=":", help_command=None)

#Define Activities
def play():
	@client.event
	async def on_ready():
		clear()
		rstart()
		await client.change_presence(status=STATUSz, activity=discord.Game(name=PLAYTXT))

def stream():
	@client.event
	async def on_ready():
		clear()
		rstart()
		await client.change_presence(activity=discord.Streaming(name=STRTXT, url=STRURL))

def listen():
	@client.event
	async def on_ready():
		clear()
		rstart()
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=LISTXT), status=STATUSz)

def watch():
	@client.event
	async def on_ready():
		clear()
		rstart()
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=WATXT), status=STATUSz)

def clear():
	os.system("clear")

def rstart():
	print("Custom Status Ready : Made By INCOGNITO")

def rands():
	async def status_task():
		while True:
			await client.change_presence(activity=discord.Game(name=PLAYTXT), status=STATUSz)
			await asyncio.sleep(secs)
			await client.change_presence(activity=discord.Streaming(name=STRTXT, url=STRURL))
			await asyncio.sleep(secs)
			await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=LISTXT), status=STATUSz)
			await asyncio.sleep(secs)
			await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=WATXT), status=STATUSz)
			await asyncio.sleep(secs)
	@client.event
	async def on_ready():
		clear()
		rstart()
		client.loop.create_task(status_task())

#Starts The Code
if activitys == "PLAYING":
	play()
elif activitys == "LISTENING":
	listen()
elif activitys == "STREAMING":
	stream()
elif activitys == "WATCHING":
	watch()
elif activitys == "ALL":
	rands()

#Login
keep_alive()
client.run(TOKEN, bot=False)
