#!/usr/bin/python3
from discord.utils import get
import discord
import toml
import responses

async def send_message(msg, user_msg, is_private):
    try:
        response = responses.handle_response(user_msg)
        if response:
            await msg.author.send(response) if is_private else await msg.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    config_file = "config.toml"
    config = toml.load(config_file)
    TOKEN = config["bot_token"]
    recipient_id = config["recipient_id"]

    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        #recipient = await client.fetch_user(recipient_id)
        #await recipient.send(f"Created video: {video_title}")

    @client.event
    async def on_message(msg):
        #print(msg.content)
        if msg.author == client.user:
            return
        
        if msg.guild is None:
            return 
        
        # channel = get(client.get_all_channels(), name=config["channel_name"])
        # CHANNEL_ID = channel.id
        # #print(channel.content)
        # if msg.channel.id == CHANNEL_ID:
        #     channel_message = await msg.fetch_message(message.id)
        #     msg_content = channel_message.content
        
        username = str(msg.author)
        user_msg = str(msg.content)
        channel  = str(msg.channel)
        
        print(f"{username} said {user_msg} in channel {channel}")


        # if not user_msg:
        #     user_msg = msg_content
        
        if user_msg and user_msg[0] == "?":
            # remove the '?'
            user_msg = user_msg[1:]
            await send_message(msg, user_msg, is_private=True)
        else:
            await send_message(msg, user_msg, is_private=False)

    client.run(TOKEN)

