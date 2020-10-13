from discord.ext import commands
import discord
import json
import asyncio

bot = commands.Bot(command_prefix = "$")
bot_ver = "-C:0.01"

with open("data/item.json", encoding="utf8") as item_db:
	item_db = json.load(item_db)


@bot.event
async def on_ready():
	print(f"Ready! Current version: 0.01")
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game("with Discord.py"))

@bot.command()
async def item(ctx, MODE, ITM_NAME, *, ITM_DESC="!PLACEHOLDER!"):
	if not(ctx.author.guild_permissions.administrator):
		return
	if(MODE.upper() == "TELL"):
		try:
			await ctx.send(f"{ITM_NAME}: " + item_db[ITM_NAME])
		except(KeyError):
			await ctx.send("Este item não existe.")
	elif(MODE.upper() == "ADD"):
		item_db[ITM_NAME] = ITM_DESC
	elif(MODE.upper() == "REMOVE"):
		item_db.pop(ITM_NAME)
	if(MODE.upper() == "ADD" or MODE.upper() == "REMOVE"):
		with open("data/item.json", "w", encoding="utf8") as itm:
			json.dump(item_db, itm, indent=4)
		
"""
@bot.command()
async def trigger(ctx, script_name):
	with open(f"script/{script_name}.json") as script:
		script = json.load(script)
	for cmd in script["script"]:
		if(cmd["type"] == 0):
			await ctx.send(cmd["cont"])
		elif(cmd["type"] == 1):
			await asyncio.sleep(cmd["time"])
"""
"""
@bot.command()
async def liberar(ctx, *, role):
	partic_role = discord.utils.get(ctx.guild.roles, name="participante")
	taddr = discord.utils.get(ctx.guild.roles, name=role)
	for member in ctx.guild.members:
		await ctx.send("member")
		if partic_role in member.roles:
			await ctx.send("l")
			if not taddr in member.roles:
				await ctx.send("g")
				member.add_roles(taddr)
"""

@bot.command()
async def id(ctx):
	embed = discord.Embed(title="Identidade", color=0xad1328)
	await ctx.send(embed=embed)




bot.run("NzMzOTA1MjU4MDQ0MTk0ODg4.XxJ8iA.qBOonTgc44jBRg9GMgEPpdGP3wo")	
