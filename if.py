print('Left or Right (L/R)?')
direction = input()
number = 10
if direction.lower() == 'l':
    print('You are going to the left.')
elif direction.lower() == 'r':
    print('You are going to the right.')
else:
    print('You did not enter L or R!')
    while number != 0:
        print(number)
        number -= 1
    