name = input("full name ")
i = 0

def normalise(x):
    x = x.strip()
    x = x.capitalize()
    x = x.split(" ")
    return x

print(normalise(name))

for name in normalise(name):
    print(name[0])


llength = len(normalise(name[0]))
while i <= len(normalise(name)):
    print(normalise(name[i]))
    i = i + 1

