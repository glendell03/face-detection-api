from fastapi import APIRouter

from src.services.storage import get_files, get_public_url

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/get")
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
