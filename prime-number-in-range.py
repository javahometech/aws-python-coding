start = 1
end = 100
for i in range(start,end):
    if i == 1 or i == 2:
        print(i, 'Is prime')
    else:
        isPrime = True
        for x in range(2,i):
            if i%x == 0:
               isPrime = False
        if isPrime:
            print(i, 'is prime')
