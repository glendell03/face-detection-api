import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = "AC5635efe7c9855057fd23bbe7acdb2f04"
auth_token = "cbebed66b71c7565d9b5a1d4f9b9953f"
twilio = Client(account_sid, auth_token)
