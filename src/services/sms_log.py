from typing import Optional

from src.utils.supabase import supabase


def insert_sms_log(name: str, photo: Optional[str] = None):
    data = supabase.table("sms_log").insert({"name": name, "photo": photo}).execute()
    return data.data


def get_latest_sms_log(name: str):
    res = (
        supabase.table("sms_log")
        .select("*")
        .limit(1)
        .eq("name", name)
        .order("created_at", desc=True)
        .single()
        .execute()
    )

    return res.data
