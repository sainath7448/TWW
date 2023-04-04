n = 7

c = 2 

while c*c < n:
    if n % c == 0:
        print("Not prime")
        break 
    c += 1 
if n <= 1:
    print("neither Prime nor composite")
else:
    print("Prime")