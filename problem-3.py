import array as arr
import math
primefactor = arr.array('i',[])
factor = arr.array('f',[])
myinput = 600851475143
for n in range(1,myinput):
    print("testing number : ",n)
    if myinput % n == 0:
        number = math.floor(myinput/n)
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            primefactor.append(number)
    else:
        print("")
print("Answer is",max(primefactor))