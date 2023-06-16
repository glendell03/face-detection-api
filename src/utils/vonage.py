import vonage

secret = "YHlV91vURqClpGVD"
key = "52ed459f"

client = vonage.Client(key, secret)
sms = vonage.Sms(client)
