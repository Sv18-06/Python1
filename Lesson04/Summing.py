array = [28, 44, 92, 27, 83]
result = 0

#for k in array:
#    result += k
#print(result)

i = 0
length = len(array)
while i < length:
    result += array[i]
    i += 1
print(result)
