from discord.ext import commands
import discord
import json
import asyncio

bot = commands.Bot(command_prefix="$")
bot_ver = "-C:0.01"

with open("data/item.json", encoding="utf8") as item_db:
	item_db = json.load(item_db)


@bot.event
async def on_ready():
	print(f"Ready! Current version: 0.01")
	await bot.change_presence(status=discord.Status.idle, activity=discord.Game("with Discord.py"))

@bot.command()
async def item(ctx, MODE, *, ITM):
	if not(ctx.author.guild_permissions.administrator):
		return
	if(MODE.upper() == "TELL"):
		try:
			await ctx.send(f"{ITM.lower().title()}: " + item_db[ITM.lower().title()])
		except(KeyError):
			await ctx.send("Este item não existe.")
	elif(MODE.upper() == "ADD"):
		
		ITM_DESC = ITM.split(";")[1]
		ITM_NAME = ITM.split(";")[0].lower().title()

		item_db[ITM_NAME] = ITM_DESC

		with open("data/item.json", "w", encoding="utf8") as itm:
			json.dump(item_db, itm, indent=4)
	elif(MODE.upper() == "REMOVE"):
		item_db.pop(ITM.lower().title())
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

	try:
		with open(f"data/{ctx.author.display_name}.json", encoding="utf8") as memberName:
			memberName = json.load(memberName)

		embed = discord.Embed(title="Identidade de " + memberName.get("Name"), color=0xad1328)
		embed.add_field(name="Altura:", value=memberName.get("Height"), inline=True)
		embed.add_field(name="Idade:", value=memberName.get("Age"), inline=True)
		await ctx.send(embed=embed)
	except(FileNotFoundError):
		await ctx.send("```ID não encontrado.```")




bot.run("NzMzOTA1MjU4MDQ0MTk0ODg4.XxJ8iA.qBOonTgc44jBRg9GMgEPpdGP3wo")	
