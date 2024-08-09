import random
right = random.randint(1,1000000)

num = 0
count = 1
min = 1
max = 1000000
while right != num:
    num = random.randint(min,max)
    if num == right:
        print("你猜对了！")
    else:
        print(f"猜错了,已经猜了{count}次")
        count += 1
        if num < right:
            min = num
        else:
            max = num
        
