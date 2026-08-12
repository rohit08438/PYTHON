""""
Program : Weather-Bot 3000
Purpose : Gives simple lifestyle advice based on temperature and rain
Author : Rohit Kumar Singh
Date : 08 August 2026
"""

print("Welcome to AI Climate Assitant.")
temp_input = input("Enter the temperature in celsius:").strip()

if temp_input.isdigit():
    temp_erature=int(temp_input)

    if temp_erature > 30:
        print("AI Alert: Its hot! AI suggest turing on AC")
    elif temp_erature < 15:
        print("AI Alert: Chilly! AI suggest a jacket")
    else:
        print("AI Analysis: Temperature is optimal. Enjoy your day")
    rain_check = input("Is it raining? (yes/no):").lower().strip()
    if rain_check=="yes" and temp_erature < 15:
        print("AI recommendation : Stay indoors and carry an umbrella if you go out")
    elif rain_check=="yes":
        print("AI recommendation : Carry an umbrella")
    else:
        print("AI recommendation : No umbrella needed. Enjoy your day")
else:
    print("Please enter a valid temperature in celsius.")
    
