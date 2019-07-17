import discord

import config
import butt

class ButtBot(discord.Client):

    async def on_message(self, message):
        server_id = message.guild.id
        channel_id = message.channel.id
        if not config.is_channel_authorized(server_id, channel_id):
            return

        if message.author == self.user:
            return

        response = butt.buttify(message.content)
        await message.channel.send(response)