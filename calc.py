import sys
import os
class Color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

while True:
   calc = input(Color.BLUE + Color.BOLD + "Type calculation" + Color.END + ": ")
   if 'clear' in calc:
      clearConsole()
   if 'exit' in calc:
      sys.exit()
   if 'clear' not in calc:
      try:
         print(Color.GREEN + Color.BOLD + "Answer" + Color.END + ": " + str(eval(calc)) + "\n")
         ans=int(eval(calc))
      except Exception as error:
         if 'ans' in str(error):
            print(Color.RED + Color.BOLD + "You can not use the previous answer as there not currently not one!\n" + Color.END)
         else:
            print(Color.RED + Color.BOLD + "looks like something went wrong: " + Color.END + str(error) + Color.RED + Color.BOLD + "!\n" + Color.END)  
