import requests

accessToken = input("accessToken: ")

if requests.get("https://notify-api.line.me/api/status", headers={"Authorization": "Bearer %s" % (accessToken)}).status_code != 200:
	print("Invalid access token")
	exit()

while True:
	try:
		if requests.post("https://notify-api.line.me/api/notify", headers={"Authorization": "Bearer %s" % (accessToken)}, data={"message": input("Message: ").replace("\\n","\n")}).status_code != 200:
			print("Error")
	except KeyboardInterrupt:
		print()
		break
