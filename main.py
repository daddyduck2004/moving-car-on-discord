#!/usr/bin/python
import requests, time

range1 = 0
between1and2 = 20

speed = 0.7
car = "🚗"
yard = f"▁▁▁{range1 + between1and2}m▁▁▁{range1}m▁▁▁"
progress = len(yard) - 1
token = "YOUR TOKEN HERE"

def updateCS(text: str):
	signature = {"authorization": token}
	uri = "https://discord.com/api/v8/users/@me/settings"
	requests.patch(url=uri, json={"custom_status": {"text": text}}, headers=signature)

while True:
	try:
		isKm = True if range1 >= 1000 else False
		rangeUnit = "km" if isKm else "m"
		yard = f"▁▁▁▁{round((range1 + between1and2) / 1000 if isKm else range1 + between1and2,2)}{rangeUnit}▁▁▁{round(range1 / 1000 if isKm else range1,2)}{rangeUnit}▁▁▁"
		yard = f"{yard[:progress] + car + yard[progress + 1:]}"

		updateCS(yard); clsChr = len(yard)-1

		print(*clsChr*(" ",), end="\r", flush=True)
		print(yard.replace("▁", "_").replace(car, "+"), end="\r", flush=True)

		if progress > 0: progress = progress - 1
		else: progress, range1 = len(yard), range1 + between1and2 * 2
		time.sleep(1 - speed)
	except KeyboardInterrupt:
		exit()
