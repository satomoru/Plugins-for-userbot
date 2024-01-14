#developed by satomoru
from asyncio import sleep
from telethon import functions
from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession

aid = 10953300
ahash = '9c24426e5d6fa1d441913e3906627f87'

with TelegramClient('session_name', aid, ahash) as client:
    print('run')

with client:
    class FakeMod:
        def __init__(self, client):
            self.client=client

        async def actfake(self, message):
            act_time = message.text.split(' ', 1)[1]
            await message.delete()
            try:
                async with self.client.action(message.chat_id, "sticker"):
                    await sleep(int(act_time))
            except BaseException:
                return


    @events.register(events.NewMessage(outgoing=True, pattern='.fact'))
    async def tfake(event):
        fmode = FakeMod(client)
        await fmode.actfake(event.message)

    with client as darknet:
        darknet.add_event_handler(tfake)


    client.start()
    client.run_until_disconnected(
