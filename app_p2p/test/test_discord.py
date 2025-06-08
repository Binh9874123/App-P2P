import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập với tên {bot.user}")

    channel_id = 1381104661133525064
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("🤖 Bot đã sẵn sàng hoạt động!")

@bot.command()
async def hello(ctx):
    await ctx.send("👋 Xin chào! Đây là bot Discord.")

# @bot.command()
# async def anh(ctx):
#     try:
#         with open("ten_file_anh.jpg", "rb") as f:
#             picture = discord.File(f)
#             await ctx.send("📷 Đây là ảnh của bạn:", file=picture)
#     except FileNotFoundError:
#         await ctx.send("❌ Không tìm thấy file 'ten_file_anh.jpg'.")

# Thay TOKEN_MOI bằng token mới của bạn
bot.run("MTM4MTEwMDM3MjMyNzkyNzk2OQ.GLVtG8.VXUeEAbtmbbND_PScFyb9w0yYKmfVn2BCurZZ8")
