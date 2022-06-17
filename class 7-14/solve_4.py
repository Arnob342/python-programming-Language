##[4] Write a Python program to read the temperature in centigrade
# and display a suitable message according to the temperature state below:
#Temp < 0 then Freezing weather
#Temp 0-10 then Very Cold weather
#Temp 10-20 then Cold weather
#Temp 20-30 then Normal in Temp
#Temp 30-40 then It’s Hot
#Temp >=40 then It’s Very Hot

temp = int (input())
if temp < 0:
    print("then Freezing weather")
elif temp>=0 and temp<=10:
    print("then Very Cold weather")
elif temp >=10 and temp <=20:
    print("then Cold weather")
elif temp>=20 and temp<=30:
    print("then Normal in Temp")
elif temp>=30 and temp<=40:
    print("then It’s Hot")
elif temp>=40:
    print("then It’s Very Hot")
