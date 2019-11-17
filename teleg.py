import time
from telethon import TelegramClient, events

api_id = 816076
api_hash = '6610241144933060d3dcee555025b5c4'

phone = '6281278376630'
session_file = 'equalgorithm'   
password = 'x68ren6bgf'  

message = "Sorry, I'll be away until next week!"

if __name__ == '__main__':
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                await event.respond(message)


    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
    