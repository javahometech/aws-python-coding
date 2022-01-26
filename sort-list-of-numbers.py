data = [1,7,9,4,3,1,7]

temp = None
for i in range(0,len(data)):
    for j in range(i+1,len(data)):
        if data[i]>data[j]:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp

print(data)
