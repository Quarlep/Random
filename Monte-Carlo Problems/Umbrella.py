from random import uniform

for p in range(1, 99):
    sum_dry = 0
    for i in range(10 ** 5):
        dry = 0
        while True:
            rain_status = uniform(0, 99)
            if p > rain_status:
                break
            else:
                dry += 1
        sum_dry += dry
        data = [(p / 100, sum_dry / 0**5)]

print(data)
