import vonage

secret = "FHtusWUFB2NLOYzw"
key = "953cb623"

client = vonage.Client(key, secret)
sms = vonage.Sms(client)
