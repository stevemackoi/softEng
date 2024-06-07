import re
highway_number = int(input())
if highway_number % 100 == 0:
    print(highway_number, "is not a valid interstate highway number.")
elif (highway_number > 99) and (highway_number % 2 == 1):
    print("I-" + str(highway_number) + " is auxiliary, serving I-" + re.sub("^0+", "", str(highway_number)[-2:]) + ", going north/south.")
elif (highway_number > 99) and (highway_number % 2 == 0):
    print("I-" + str(highway_number) + " is auxiliary, serving I-" + re.sub("^0+", "", str(highway_number)[-2:]) + ", going east/west.")
elif highway_number % 2 == 1:
    print("I-" + str(highway_number) + " is primary, going north/south.")
elif highway_number % 2 == 0:
    print("I-" + str(highway_number) + " is primary, going east/west.")
