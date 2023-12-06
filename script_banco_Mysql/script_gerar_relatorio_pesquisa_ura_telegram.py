#!/usr/bin/python
# -*- coding: utf-8 -*-
import telegram
from telegram import InputFile
import asyncio
import os
import subprocess
import glob

# Substitua 'TOKEN' pelo token de API do seu bot
TOKEN = '6972109447:AAERfY8GB5tAmn9R08hcN5DGLEwQEn_i2yQ'

# Diretório onde os arquivos de pesquisa são armazenados
output_directory = './Pesquisa/'

# chat ID do Telegram:
chat_id = '-1002076139759'

# Executando primeiramente o bash script
subprocess.run(["./script_banco_pesquisa.sh"])

# Aguardando até que o primeiro script seja concluído e o arquivo seja gerado:
while not glob.glob(os.path.join(output_directory, 'Pesquisa_*.csv')):
    asyncio.sleep(1)

# Encontre o arquivo mais recente no diretório
latest_file = max(glob.glob(os.path.join(output_directory, 'Pesquisa_*.csv')), key=os.path.getctime)

# Crie uma instância do bot
bot = telegram.Bot(token=TOKEN)

async def send_document():
    with open(latest_file, 'rb') as file:
        # Use o nome do arquivo mais recente como o nome do arquivo no Telegram
        filename = os.path.basename(latest_file)
        await bot.send_document(chat_id=chat_id, document=InputFile(file, filename=filename))

async def main():
    await send_document()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

