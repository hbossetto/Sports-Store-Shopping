#Hunter Bossetto 9/13/2021

#Variables
choice = 0
qnty = 0
price = 0.0
subtotal = 0.0
tax = 0.0
total = 0.0

#Constant
TAX_RATE = 0.0925

#Display Menu
print("Enter 1 for Baseballs")
print("Enter 2 for Bats")
print("Enter 3 for Caps")
print("Enter 4 for Jerseys")
print("Enter 5 for Gloves")
print("Enter 6 to Exit")
choice = int(input('Enter your choice:'))
if choice == 1:
        price = 5.99
        qnty = int(input('Enter the quantity of Baseballs:'))
        subtotal += price * qnty

elif choice == 2:
        price = 15.49
        qnty = int(input('Enter the quantity of Bats:'))
        subtotal += price * qnty

elif choice == 3:
        price = 14.99
        qnty = int(input('Enter the quantity of Caps:'))
        subtotal += price * qnty

elif choice == 4:
        price = 10.99
        qnty = int(input('Enter the quantity of Jerseys:'))
        subtotal += price * qnty
        
elif choice == 5:
        price = 43.89
        qnty = int(input('Enter the quantity of Gloves:'))
        subtotal += price * qnty

elif choice == 6:
        exit()

else:
        print('Incorrect entry.')

tax = subtotal * TAX_RATE
total = subtotal + tax
print ('Subtotal:   $', format(subtotal, ',.2f'))
print ("Sales Tax:  $", format(tax, ',.2f'), sep="")
print ('Total:      $', format(total, ',.2f'))
