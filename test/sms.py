import requests

res = requests.get("https://facedetection-1-s8245812.deta.app/user/get/datasets")

data = res.json()

for i in data["datasets"]:
    name = i["name"]
    images = i["images"]

    print(name)
    print(images)

# name = "Glendell_Bringino"
#
# get_phone_number_by_name = requests.get("url/get/user-phone")
#
# res = requests.post(
#     url="https://facedetection-1-s8245812.deta.app/sms/send",
#     json={
#         "send_to": get_phone_number_by_name.json()["phone_number"],
#         "body": "Hello sample text message demo",
#         "name": name,
#     },
# )

print(res.json())
