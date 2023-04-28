cash = [1000, 500, 200, 100, 50, 20, 10]

quantity = int(input("Enter the quantity of money you want to get: "))

if quantity % 10:
 print("You've entered incorrect quantity of money")
 exit()

for i in cash:
 print(i)
 if not quantity // i:
  print('Quantity - 0')

  if not quantity:
   exit()

 if quantity // i:
  print('Quantity - ', (quantity // i))
  quantity %= i
 