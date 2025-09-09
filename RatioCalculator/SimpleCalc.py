from time import sleep

from Utils import GetFloatInput
class SimpleCalc:
    
    # Variables
    Operation = str(' ')
    a = 0
    b = 0
    c = 0
    
    print('''Choose an operation:
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          ''')

# Start of SimpleCalc
    while True:
        if Operation == 1:
            print("Num1: ")
            a = GetFloatInput()
            print()

            print("Num1: ")
            b = GetFloatInput()
            print()

            print('Calculating...\n')
            sleep(0.5)
            c = a + b

            print("-> ", a, ' + ', b, ' = ', c)

        elif Operation == 2:
            print("Num1: ")
            a = GetFloatInput()
            print()

            print("Num1: ")
            b = GetFloatInput()
            print()

            print('Calculating...\n')
            sleep(0.5)
            c = a - b

            print("-> ", a, ' - ', b, ' = ', c)

        elif Operation == 3:
            print("Num1: ")
            a = GetFloatInput()
            print()

            print("Num1: ")
            b = GetFloatInput()
            print()

            print('Calculating...\n')
            sleep(0.5)
            c = a + b

            print("-> ", a, ' + ', b, ' = ', c)

        elif Operation == 4:
            print("Num1: ")
            a = GetFloatInput()
            print()

            print("Num1: ")
            b = GetFloatInput()
            print()

            print('Calculating...\n')
            c = a + b

            print("-> ", a, ' + ', b, ' = ', c)

        elif Operation == 'Done'or Operation == 'done':
            print("\nReturning...\n")
            sleep(1)
            
            break

        else:
            print('...That?...')
            sleep(1)
            print('Thats, not one of the options...')
            sleep(1)
            print('Please choose one of the options given.')

            continue
