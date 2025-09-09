from time import sleep

from Utils import GetFloatInput
class RatioCalculator:


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