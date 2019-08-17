from random import choice

against_senator = int(input("Enter the against the bill senetors, A: "))
against_senator_used = against_senator

for_senator = 100 - against_senator

missing_senators = int(input("Enter the missing senator number: "))

total_win = 0
for i in range(10**6):
    win = 0
    against_senator = against_senator_used
    for_senator = 100 - against_senator
    for i in range(missing_senators):
        senator_choice = choice(["against", "for"])
        if senator_choice == "against":
            against_senator += -1
        else:
            for_senator += -1
    if against_senator > for_senator:
        win += 1
    total_win += win
print(total_win / 10**6)
