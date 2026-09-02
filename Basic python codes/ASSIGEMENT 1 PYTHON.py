import datetime #used whenever we work with not fixed date and time

full_name = input("enter your full name:").strip() #.strip() is used to remove some extra spacinf if by mistake given in input

if full_name =="":
    print("Invalid input")
else:
    len_name = len(full_name)
    formatt_name = full_name.title() #.title() is used to change first letters of full name to capital
    print("\n NAME ANALYSIS ")
    print("FORMATTED NAME IS:",formatt_name)
    print("IDENTIFIER BYTE-COUNT:",len_name)

    user_age = input("enter you current age:")
    if user_age.isdigit():  #.isdigit() is used to check weather the age is in digits or not
        user_age = int(user_age) # int is used for tyep casting of string into integer
        current_year = datetime.date.today().year # date.time.today().year year is used to extract current year whenever the code is being run
        age_2045 = user_age +(2045 - current_year)
        score=((len_name*10) + age_2045)/2


        print("\nProgram: Temporal Profile Analyzer")
        print("Purpose: Computes an AI Era Readiness Score from user Metadeta")
        print("Author:", full_name)
        print("Date: 31.07.2026")

        print("Name length:",len_name)
        print("Current age:" ,user_age)
        print("Age in 2045:", age_2045)
        print(f"AI Readiness Score:,{score:.2f}") # f is used to convert normal intger to float and score:.2f is used to extend float value till 2 digits

        if user_age < 10:
            repeat = user_age
            print(repeat)
        else:
            repeat = user_age//10
            repeatted_name = formatt_name * repeat
            print("Bonus Solution:", repeatted_name)
    else:
        print("Invalid Input")
        

        
        
        
