par = int(input())
score = int(input())

if par not in [3,4,5]:
    print("Error")
elif par - score == 2:
    print("Eagle")
elif par - score == 1:
    print("Birdie")
elif par - score == 0:
    print("Par")
elif par - score == -1:
    print("Bogey")
else:
    print("Other")
