import csv
file_name = input()
with open(file_name, mode='r') as file:
    reader = csv.reader(file)
    rows = list(reader)
    
def create_dict(row):
    return {row[i].strip(): row[i+1].strip() for i in range(0, len(row), 2)}
    
dict1 = create_dict(rows[0])
dict2 = create_dict(rows[1])

print(dict1)
print(dict2)
