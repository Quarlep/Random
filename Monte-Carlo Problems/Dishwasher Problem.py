from random import uniform

clumsy = 0
broken = 0
for i in range(10**4):
    for i in range(5):
        num = uniform(0, 1)
        if num < 0.2:
            broken += 1
    if broken >= 4:
        clumsy += 1
        broken = 0
    else:
        broken = 0
print(clumsy / 10**4)
