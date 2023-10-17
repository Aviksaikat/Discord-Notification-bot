#!/usr/bin/python3
import discord
import responses
import toml
from discord.utils import get


class DiscordBot:
    def __init__(self, token, recipient_id):
        self.token = token
        self.recipient_id = recipient_id
        self.client = discord.Client(intents=discord.Intents.default())

    async def send_message(self, msg, user_msg, is_private):
        try:
            response = responses.handle_response(user_msg)
            if response:
                await msg.author.send(
                    response
                ) if is_private else await msg.channel.send(response)
        except Exception as e:
            print(e)

    def make_notification(self, message):
        recipient = self.client.fetch_user(self.recipient_id)
        asyncio.create_task(recipient.send(message))

    async def on_ready(self):
        print(f"{self.client.user} has connected to Discord!")

    async def on_message(self, msg):
        # print(msg.content)
        if msg.author == self.client.user:
            return

        if msg.guild is None:
            return

        # channel = get(self.client.get_all_channels(), name=config["channel_name"])
        # CHANNEL_ID = channel.id
        # #print(channel.content)
        # if msg.channel.id == CHANNEL_ID:
        #
        #     channel_message = await msg.fetch_message(message.id)
        #     msg_content = channel_message.content

        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)

        print(f"{username} said {user_msg} in channel {channel}")

        # if not user_msg:
        #     user_msg = msg_content

        if user_msg and user_msg[0] == "?":
            # remove the '?'
            user_msg = user_msg[1:]
            await self.send_message(msg, user_msg, is_private=True)
        else:
            await self.send_message(msg, user_msg, is_private=False)

    def run(self):
        self.client.event(on_ready=self.on_ready)
        self.client.event(on_message=self.on_message)
        self.client.run(self.token)


config_file = "config.toml"
config = toml.load(config_file)
TOKEN = config["bot_token"]
recipient_id = config["recipient_id"]

bot = DiscordBot(TOKEN, recipient_id)
bot.run()
