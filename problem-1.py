#define
below = 1000
myanswer = []
#loop 
for i in range(1,below):
    if i%3 == 0 or i%5 == 0 :
        myanswer.append(i)
#print
print("Answer is", sum(myanswer))
        

        
