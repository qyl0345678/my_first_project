import time

def progress_funcion():
    count = 0
    while count <= 100:
        progress = '⁙' * count + '⁎' * ( 100 - count )
        count += 1
        print(progress,end = "\r")
        time.sleep(0.1)
    return count

def callback_function():
    if count == 101:
        print(end = "\n")
        print("运行结束啦")
    return

count = int( progress_funcion() )
callback_function()