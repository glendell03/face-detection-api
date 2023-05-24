import os
from datetime import datetime
from typing import Optional

import pandas as pd
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.services.sms_log import get_latest_sms_log, insert_sms_log
from src.utils.twilio import twilio

router = APIRouter(prefix="/sms", tags=["Sms"])


class SendSMS(BaseModel):
    send_to: str
    body: str
    photo: Optional[str] = None
    name: str


@router.post("/send")
async def send_sms(req: SendSMS):
    try:
        # Get the latest log base on the input name
        latest_log = get_latest_sms_log(req.name)

        is_already_log = False
        #
        if latest_log is not None:
            # Get the current date
            date_now = datetime.now().date()

            # Get the createdAt
            todays_log_date = pd.to_datetime(latest_log["created_at"]).date()

            # Check if name is already in the log
            is_already_log = date_now == todays_log_date

        if is_already_log:
            return HTTPException(404, "Name is already in the log")

        # if name is not in the log create
        log = insert_sms_log(req.name, req.photo)

        # Send a message
        message = twilio.messages.create(
            body=req.body,
            from_=os.getenv("TWILIO_PHONE") or "+12543182693",
            to=req.send_to,
        )

        return {
            "success": True,
            "log": log,
            "message": message,
        }
    except Exception as e:
        raise HTTPException(500, e)
