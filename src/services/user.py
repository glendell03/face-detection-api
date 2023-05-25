from src.utils.supabase import supabase


def create_user(name: str, phone: str, grade: int, section: str, guardian: str):
    data = (
        supabase.table("user")
            .insert({"name": name, "phone": phone, "grade": grade, "section": section, "guardian": guardian})
        .execute()
    )
    return data.data[0]


def get_user_by_name(name: str):
    data = supabase.table("user").select("*").eq("name", name).single().execute()
    return data.data
