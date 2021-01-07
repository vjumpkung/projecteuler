import math
number = 100
factorial = 1
i = 1
for i in range (1,number+1):
    print("i = ",i)
    factorial = factorial*i
    print("factorial = ",factorial)
split = [int(j) for j in str(factorial)]
print(sum(split))
