# coding: utf-8

speed, weight, strength = map(float, input().split())

result = ""
if speed <= 4.5 and weight >= 150 and strength >= 200:
    result += "Wide Receiver "
if speed <= 6.0 and weight >= 300 and strength >= 500:
    result += "Lineman "
if speed <= 5.0 and weight >= 200 and strength >= 300:
    result+= "Quarterback"
if result == "":
    print("No positions")
else:
    print(result)

