import logging
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel

# Fungsi untuk meneruskan pesan dari channel ke channel
def forward_message(update, context):
    # Ganti ID channel tujuan dengan ID channel yang diinginkan
    destination_channel_id = 'your_destination_channel_id'

    # Mengganti 'api_id' dan 'api_hash' dengan nilai API ID dan API Hash Anda
    api_id = 'your_api_id'
    api_hash = 'your_api_hash'

    with TelegramClient('session_name', api_id, api_hash) as client:
        # Mendapatkan objek InputPeerChannel dari ID channel tujuan
        destination = InputPeerChannel(int(destination_channel_id), 0)

        # Meneruskan pesan dari channel sumber ke channel tujuan
        client.forward_messages(destination, [update.message])

def main():
    # Mengganti 'api_id' dan 'api_hash' dengan nilai API ID dan API Hash Anda
    api_id = 'your_api_id'
    api_hash = 'your_api_hash'

    with TelegramClient('session_name', api_id, api_hash) as client:
        # Mendapatkan objek InputPeerChannel dari ID channel sumber
        source_channel = InputPeerChannel(int('your_source_channel_id'), 0)

        # Mengganti 'limit' dengan jumlah pesan yang ingin Anda teruskan
        messages = client.get_messages(source_channel, limit=10)

        for message in messages:
            # Meneruskan pesan dari channel sumber ke channel tujuan
            client.forward_messages(InputPeerChannel(int('your_destination_channel_id'), 0), [message])

if __name__ == '__main__':
    main()
