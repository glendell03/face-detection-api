from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI

from src.routes import sms, user
from src.utils.prisma import prisma

load_dotenv()
app = FastAPI()


@app.on_event("startup")
async def startup():
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown():
    await prisma.disconnect()


app.include_router(user.router)
app.include_router(sms.router)


@app.get("/health-checker")
def health_checker():
    return {"success": True, "date": datetime.now()}


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
