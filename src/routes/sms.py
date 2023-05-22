import os
from datetime import datetime

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.utils.prisma import prisma
from src.utils.twilio import twilio

router = APIRouter(prefix="/sms", tags=["Sms"])


class SendSMS(BaseModel):
    send_to: str
    body: str
    photo: str | None = None
    name: str


@router.post("/send")
async def send_sms(req: SendSMS):
    try:
        # Find the latest log base on the input name
        find_first_name_log = await prisma.smslog.find_first(
            where={"name": req.name}, order={"createdAt": "desc"}
        )

        # Get the current date
        date_now = datetime.now().date()

        # Get the createdAt
        todays_log_date = find_first_name_log and find_first_name_log.createdAt.date()

        # Check if name is already in the log
        isAlreadyLog = date_now == todays_log_date

        if isAlreadyLog:
            return {"message": "Name is already in the log", "log": isAlreadyLog}

        # if name is not in the log create
        log = await prisma.smslog.create(
            {
                "name": req.name,
                "photo": req.photo,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now(),
            }
        )

        # Send a message
        message = twilio.messages.create(
            body=req.body,
            from_=os.getenv("TWILIO_PHONE") or "+12543182693",
            status_callback="http://postb.in/1234abcd",
            to=req.send_to,
        )

        return {
            "success": True,
            "message": f"Successfully sent the message to {message.to}",
            "log": log,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
