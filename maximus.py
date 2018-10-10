def max(int1, int2):
    if int1 > int2:
        max_val = int1

    elif int2 > int1:
        max_val = int2

    else:
        max_val = 'Integers are equivalent'

    return max_val

int1 = int(input('Enter an integer:'))
int2 = int(input('Enter another integer:'))
print('Maximum of two integers:', max(int1, int2))
