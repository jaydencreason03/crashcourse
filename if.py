print('Left or Right (L/R)?')
direction = input()
if direction.lower() == 'l':
    print('You are going to the left.')
elif direction.lower() == 'r':
    print('You are going to the right.')
else:
    print('You did not enter L or R!')
    