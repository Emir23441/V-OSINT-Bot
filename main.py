import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# Web sunucusu (UptimeRobot için)
app = Flask('')
@app.route('/')
def home():
    return "V-OSINT Aktif!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Bot kurgusu
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} sahaya indi!')

@bot.command()
async def sorgu(ctx, user_id: int):
    user = await bot.fetch_user(user_id)
    embed = discord.Embed(title="V-OSINT Tarama Sonucu", color=0xff0000)
    embed.add_field(name="Hedef", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Sızıntı Durumu", value="🔍 Kayıtlar taranıyor... Gmail sızıntısı aranıyor.", inline=False)
    await ctx.send(embed=embed)

keep_alive()
bot.run("MTQ5NDIzMTg2MDA0MDA0NDYxNQ.G8uopu.1WwKc8IwTd09P0cyAwjfE9O3b0-23PcoQRtqvs")
