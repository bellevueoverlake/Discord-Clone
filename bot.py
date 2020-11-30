import discord
client = discord.Client()
@client.event
async def on_ready():
    print('Bot is ready. ')

@client.event
async def kick(ctx, member: discord.Member, *, reason = None):
    await member.kick(reason = reason)


@client.event
async def ban(ctx, member: discord.Member, *, reason = None):
    await member.ban(reason = reason)

client.run('NzgyNzYwNTUzNzM5MDU5MjEw.X8Q4kg.ElHj_RVsHjdUpS-uSgnEs8n_OEg')
