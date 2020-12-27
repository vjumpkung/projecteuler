import array as arr
target = 100
answer = 0
fibo = arr.array('i',[1,2])
for n in range (1,target):
    if fibo[n] <= 4000000:
        next = fibo[n-1] + fibo[n]
        if next >= 4000000:
            totalfibo = len(fibo)
            break
        fibo.append(next)
    else:
        totalfibo = len(fibo)
        break
for i in range(0,totalfibo):
    if fibo[i] % 2 == 0 :
        answer = fibo[i] + answer       
print(answer)