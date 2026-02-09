num1= int(input('select fisrt number: '))
num2= int(input('select second number: '))
print('select the operation (a,b,c,d)')
print('a= add (+)')
print('b= subtract (-)')
print('c= multiply (*)')
print('d= divide (/)')
choice= input('select the operation: ')
if choice == 'a':
    print('Result' , num1 + num2)
elif choice == 'b':
    print('Result' , num1 - num2)
elif choice == 'c':
    print('Result' , num1 * num2)
elif choice == 'd':
    if num2 != 0:
        print('Result' , num1 / num2)
    else:
        print('cannot divide by zero')
else:
    print('invalid please select from a,b,c,d')
