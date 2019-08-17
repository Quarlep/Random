from random import choice

avg_drown_match = 0
for i in range(10**5):
    box_1 = 40
    box_2 = 40
    drown_match = 0
    while box_1 > 0 and box_2 > 0:
        box_random = choice(["b1", "b2"])
        if box_random == "b1":
            box_1 += -1
            drown_match += 1
        if box_random == "b2":
            box_2 += -1
            drown_match += 1
    avg_drown_match += drown_match
print(avg_drown_match / 10**5)
