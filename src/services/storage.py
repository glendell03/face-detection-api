from typing import Optional

from src.utils.supabase import supabase


def get_files(id: str, name: Optional[str] = None):
    return supabase.storage.from_(id).list(name)


def get_public_url(id: str, path: str):
    return supabase.storage.from_(id).get_public_url(path)
