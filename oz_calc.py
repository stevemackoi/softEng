total_ounces = int(input())

OUNCES_IN_POUND = 16
POUNDS_IN_TON = 2000

tons = total_ounces // (OUNCES_IN_POUND * POUNDS_IN_TON)
remaining_ounces = total_ounces % (OUNCES_IN_POUND * POUNDS_IN_TON)

pounds = remaining_ounces // OUNCES_IN_POUND
ounces = remaining_ounces % OUNCES_IN_POUND

print(f"Tons: {tons}")
print(f"Pounds: {pounds}")
print(f"Ounces: {ounces}")
