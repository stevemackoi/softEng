number = bin(int(input()))
print(str(number[::-1].replace("b0", "")))
#Example: '6' returns '011' (reverse binary)
