
from RatioCalc import RatioCalculator
from SimpleCalc import SimpleCalculator
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
        SimpleCalculator()
        continue
        
    elif CalcChoice == 2:
        RatioCalculator()
        continue
        
    elif CalcChoice == 3:
        break
    else:
        print('Sorry thats not one one of the choices.')
        continue