from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

# from discord_services.responses import get_response
from responses import get_response

load_dotenv()
TOKEN: Final = os.getenv("DISCORD_BOT_TOKEN")
print(TOKEN)

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def

DB_TOKEN = eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3NDA5MTkwOTEsImlkIjoiODNhNDU0NmEtYTU5MS00MDgwLWJjYWQtMDU2YWEyZGYzZWVmIn0.QiBZv72uoUl2QAJp2oJB01u3cBlFdYo3SHRCFhrlHA2CXWZXL-ZZW2lSINiomSKw0TADRNdOoRo_ef5QbDAhCw
DB_LINK = libsql://etqan-mamfmahmoud.turso.io