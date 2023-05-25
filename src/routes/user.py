from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.services.storage import get_files, get_public_url
from src.services.user import create_user, get_user_by_name

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/get/datasets")
async def get_user_datasets():
    # Get the folder of the student
    folders = get_files("Image Database")
    # Delete the last element in the array
    if folders[-1] == ".emptyFolderPlaceholder":
        del folders[-1]

    datasets = []

    # Get the images of each student
    for folder in folders:
        folderName = folder["name"]

        images = get_files("Image Database", folderName)

        urls = []

        for image in images:
            fileName = image["name"]

            if fileName != ".emptyFolderPlaceholder":
                url = get_public_url("Image Database", f"{folderName}/{fileName}")

                urls.append(url)

        datasets.append({"name": folderName, "images": urls})

    return {"success": True, "count": len(datasets), "datasets": datasets}


class AddUser(BaseModel):
    name: str
    phone: str


@router.post("/add")
async def add_user(req: AddUser):
    try:
        data = create_user(req.name, req.phone)

        return {"success": True, "message": "Successfully created a user", "data": data}
    except Exception as e:
        return HTTPException(500, e)


@router.get("/get/{name}")
async def get_user_data(name: str):
    try:
        data = get_user_by_name(name)
        return {"user": data}
    except Exception as e:
        return HTTPException(500, e)
