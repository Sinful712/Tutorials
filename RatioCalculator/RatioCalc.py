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
            a = GetFloatInput("Width: ")
            print()

            b = GetFloatInput("Hight: ")
            print()

            c = GetFloatInput("Width: ")
            print()

            print('Calculating...\n')
            sleep(0.5)
            x = float((c * b) / a)

            print(f"-> {a} : {b}  =  {c} : {x}")

        elif WH == "H" or WH == "h":
            a = GetFloatInput("Hight: ")
            print()

            b = GetFloatInput("Width: ")
            print()

            c = GetFloatInput("Hight: ")
            print()

            print('Calculating...\n')
            sleep(0.5)
            x = float((c * b) / a)

            print(f"-> {b} : {a}  =  {x} : {c}")

        elif WH == 'Done' or WH == 'done':
            print("\nReturning...\n")
            sleep(1)
            break

        else:
            continue