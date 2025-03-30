N=10000

def sum_digits(num):
    x = num
    sum = 0
    while (x > 0):
        y = x % 10
        sum += y
        x = int(x/10)
    return sum

def fn(num):
    if (num < 10):
        return 0
    else:
        return (1 + fn(sum_digits(num)))
    
count = 0
for i in range(N):
    if (fn(i) == 3):
        count += 1

print (count)
