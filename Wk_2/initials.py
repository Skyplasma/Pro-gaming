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
