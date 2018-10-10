import random

def counter():
    i = 0
    odd = 0
    even = 0
    while i < 100:
        num = str(random.randint(1, 1000))
        i += 1
        if num[-1] == '1' or num[-1] == '3' or num[-1] == '5' or num[-1] == '7' or num[-1] == '9':
            odd += 1
        else:
            even += 1

    if i == 100:
        print('Tolal number of odd numbers', odd)
        print('Total number of even numbers', even)

    return
counter()
        
