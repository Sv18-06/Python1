cash = [100, 50, 20, 10, 200, 500, 1000]

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
        max_num_bills = min(quantity // i, 10) # обмеження кількості купюр
        print('Quantity - ', max_num_bills)
        quantity -= max_num_bills * i
