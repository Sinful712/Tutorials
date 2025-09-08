from time import sleep


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
def GetFloatInput():
    global Operation
    Operation = float(input(">>> "))

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


class RatioCalc:


    Iteration = 0
    
    while True:
        if Iteration == 0:
            print("\nIf you want to choose another calculator type 'Done'.")
            print("Width(W) or Hight(H) first: ")
            Iteration = Iteration + 1
        else:
            print("\nW or H:")

        WH = str(input())
        print()
        
        if WH == "W" or WH == "w":
            print("Width: ")
            a = GetFloatInput()
            print()

            print('Hight: ')
            b = GetFloatInput()
            print()

            print('Width: ')
            c = GetFloatInput()
            print()

            print('Calculating...\n')
            sleep(0.5)
            x = float((c * b) / a)

            print("-> ", a, " : ", b, "  =  ", c, " : ", x,)

        elif WH == "H" or WH == "h":
            print("Hight: ")
            a = GetFloatInput()
            print()

            print('Width: ')
            b = GetFloatInput()
            print()

            print('Hight: ')
            c = GetFloatInput()
            print()

            print('Calculating...\n')
            sleep(0.5)
            x = float((c * b) / a)

            print("-> ", b, " : ", a, "  =  ", x, " : ", c,)

        elif WH == 'Done' or WH == 'done':
            print("\nReturning...\n")
            sleep(1)
            break

        else:
            continue

## Calculator Start ##

# Variables 
CalcChoice = 0

print('''Choose a calculator(1 or 2):
      1. Simple Calculator
      2. Ratio Calculator
      3. Exit
      ''')
CalcChoice = str(input(">>> "))

while True:
    if CalcChoice == 1:
        SimpleCalc()
        continue
        
    elif CalcChoice == 2:
        RatioCalc()
        continue
        
    elif CalcChoice == 3:
        break
    else:
        print('Sorry thats not one one of the choices.')
        continue