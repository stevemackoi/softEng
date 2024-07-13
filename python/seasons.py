input_month = input()
input_day = int(input())
month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# Define the maximum days in each month
days_in_month = {
    "January": 31, "February": 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31
}

# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

spring_months = ["March", "April", "May", "June"]
summer_months = ["June", "July", "August", "September"]
autumn_months = ["September", "October", "November", "December"]
winter_months = ["December", "January", "February", "March"]

# Validate month and day input
if input_month not in month_list:
    print("Invalid month")
elif input_day < 1 or input_day > days_in_month[input_month]:
    print("Invalid day")
else:
    # Determine the season
    if input_month in spring_months:
        if input_month == "March" and input_day > 19:
            print("Spring")
        elif input_month == "June" and input_day < 21:
            print("Spring")
        elif input_month not in ["March", "June"]:
            print("Spring")

    if input_month in summer_months:
        if input_month == "June" and input_day > 20:
            print("Summer")
        elif input_month == "September" and input_day < 22:
            print("Summer")
        elif input_month not in ["June", "September"]:
            print("Summer")

    if input_month in autumn_months:
        if input_month == "September" and input_day > 21:
            print("Autumn")
        elif input_month == "December" and input_day < 21:
            print("Autumn")
        elif input_month not in ["September", "December"]:
            print("Autumn")

    if input_month in winter_months:
        if input_month == "December" and input_day > 20:
            print("Winter")
        elif input_month == "March" and input_day < 20:
            print("Winter")
        elif input_month not in ["December", "March"]:
            print("Winter")
