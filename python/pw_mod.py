word = input()
password = (
    word
        .replace("i","1")
        .replace("a","@")
        .replace("m","M")
        .replace("B","8")
        .replace("s","$")
)
print(''.join((password,'!')))
