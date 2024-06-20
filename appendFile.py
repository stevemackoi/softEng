file_name = input()

with open(file_name, 'r') as file:
    lines = file.readlines()

word1 = lines[0].strip()
word2 = lines[1].strip()
word3 = lines[2].strip()

sentence = f"{word1} {word2} {word3}"

with open(file_name, 'a') as file:
    file.write(f"\n{sentence}")
    
with open(file_name, 'r') as file:
    update = file.read()
    
print(update)
