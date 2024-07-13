is_leap_year = False
   
input_year = int(input())

#check if century years are divisible by 400
if (int(str(input_year)[-1:])) == 0:
    if input_year % 400 == 0:
        is_leap_year = True

#check if non-century years are divisible by 4
elif (input_year % 4 == 0):
    is_leap_year = True

if is_leap_year == False:
    print(input_year, "- not a leap year")
else:
    print(input_year, "- leap year")
