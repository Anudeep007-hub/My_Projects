import sys

class Grade_calculator(object):
        def __init__(self, result = 0.0, count = 0, final_result = 0.0): 
            self.count = count
            self.result = result
            self.f_res = final_result
        def calculator(self,credit,grade):
            self.count += 1
            self.result += (credit*grade)/(credit)
            self.f_res = self.result/self.count
            print("Your grade is: {}", format(self.f_res)) 

User = Grade_calculator() # Creating an user for
while(True): #Creating a loop until user opts to exit
     key = ""
     print("E- Enter grades Q-Quit\n")
     key = input("Enter your choice:  ") 

     if key == "e" or key == "E":
          user_input = "" #Initializing input as a string 
          print("Enter your input as credit<space>grade (E.g: 4 8)\n")
          user_input = input().split()
          User.calculator(int(user_input[0]), int(user_input[1]))
     elif key == "Q" or key == "q":
          sys.exit() 


        