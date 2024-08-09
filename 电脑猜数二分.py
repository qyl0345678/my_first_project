import random
right_number = random.randint(0,10000)

middle = 0
number = -1
count = 1
low_number = 0
high_number = 10000
while right_number != middle:
    middle = int((high_number + low_number) / 2 )
    if right_number == middle :
        i = 0
    elif right_number <= middle :
        high_number = middle
        count += 1
    else:
        low_number = middle
        count += 1
print(f"正确的数是{right_number},猜了{count}次。")