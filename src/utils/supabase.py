import os

from dotenv import load_dotenv
from supabase.client import Client, create_client

load_dotenv()

url: str = os.getenv("SUPABASE_URL") or ""
key: str = os.getenv("SUPABASE_KEY") or ""
supabase: Client = create_client(url, key)
