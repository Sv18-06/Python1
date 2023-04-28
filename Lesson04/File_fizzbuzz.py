fin = open('Numbers.txt', 'r')

for line in fin:
    fizz, buzz, k = map(int, line.split())
    for i in range(1, k+1) : 
     if i%fizz==0 and i%buzz==0:
        print('FB')
     elif i%fizz==0:
        print('Fizz ')
     elif i%buzz==0:
        print('Buzz ')
     else:
        print (i)
fin.close()