# main.py
#
# A Python script that runs on the command-line as a calculator
# This was Josue's first lines of code before finishing high school
# and before attending Google CSSI 2017 and UC Irvine
#
# Author: Josue Lopez
# Date:   May 5th, 2017 @ 12:40 AM PST
#
# coding=utf-8

#To run this Calculator program just press the "play" button or triangle
running = True
while running:
  
  lang = True
  while lang:
    
    lang2 = int(input("\n1.English\n\n2.Español\n\n\"Please enter a number.\"\n\"Porfavor elije un numero.\""))
    if lang2 == 1:
      print("------------------------------------------")
      print("Welcome to the Calculator Program! (= \n\nYour operations are:")
      print("\n1 = Addition")
      print("2 = Subtraction")
      print("3 = Multiplication")
      print("4 = Division")
      print("5 = Exit the program \n ")
        
      cmd = input("Choose a number: ")
      cmd = int(cmd)
    
      if cmd == 1:
          adding = True
          while adding:
            
            print("-------------------------------------")
            print("Addition\n")
            first = int(input("Enter your first number :"))
            second = int(input("Enter your second number :"))
            print("-------------------------------------")
            print("Answer:\n")
            print(first + second)
            print("----------------------------------------------------")
            
            asking = True
            while asking:
              choice = raw_input("Do you want to continue adding?\n\n")
    
              if choice in ["Yes","yes","y","Ye","ye","Y"]:
                print("\nOkay! Let's continue adding.\n")
                asking = False
                adding = True
        
              elif choice in ["No","N","n","no"]:
                print("\nOkay, I guess we're done adding.\n")
                asking = False
                adding = False
                
                running2 = True
                while running2:
                  choice = raw_input("Do you still want to use the calculator?\n")
                  
                  if choice in ["Yes","yes","y","Ye","ye","Y"]:
                    print("\nOkay! Let's continue.\n")
                    running2 = False
                    running = True
                  elif choice in ["No","N","n","no"]:
                    print("\nOkay then, We're done.")
                    running2 = False
                    running = False
                  else:
                    print("\nPlease enter either \"Yes\" or \"No\" \n ")
                    running2 = True
              else:
                print("\nPlease enter either \"Yes\" or \"No\" \n ")
                asking = True
        
      elif cmd == 2:
          subtracting = True
          while subtracting:
            
            print("----------------------------------------------------")
            print("Subtraction\n")
            first = int(input("Enter your first number :"))
            second = int(input("Enter your second number :"))
            print("----------------------------------------------------")
            print("Answer:\n") 
            print(first - second)
            print("----------------------------------------------------")
            
            asking = True
            while asking:
              choice = raw_input("Do you want to continue subtracting?\n\n")
              if choice in ["Yes","yes","y","Ye","ye","Y"]:
                print("Okay Let's continue subtracting!")
                asking = False
                subtracting = True
    
              elif choice in ["No","N","n","no"]:
                asking = False
                subtracting = False
                
                running2 = True
                while running2:
                  choice = raw_input("Do you still want to use the calculator?\n")
                  
                  if choice in ["Yes","yes","y","Ye","ye","Y"]:
                    print("\nOkay! Let's continue.\n")
                    running2 = False
                    running = True
                  elif choice in ["No","N","n","no"]:
                    print("\nOkay then, We're done.")
                    running2 = False
                    running = False
                  else:
                    print("\nPlease enter either \"Yes\" or \"No\" \n ")
                    running2 = Truerunning = False
                print("\n Done")
              else:
                print("\nPlease enter either \"Yes\" or \"No\" ")
                asking = True
        
      elif cmd == 3:
          print("----------------------------------------------------")
          print("Multiplication\n")
          first = int(input("Enter your first number :"))
          second = int(input("Enter your second number :"))
          result = first * second
          print("----------------------------------------------------")
          print("Answer:\n") 
          print(result)
          print("\nDone")
    
      elif cmd == 4:
          print("----------------------------------------------------")
          print("Division\n")
          first = int(input("Enter your first number :"))
          second = int(input("Enter your second number :"))
          result = first / second
          print("----------------------------------------------------")
          print("Answer:\n") 
          print(result)
          print("\nDone")
            
      elif cmd == 5:
          print("----------------------------------------------------")
          keeplooping = True 
          while keeplooping:
            choice = raw_input("Are you sure you want to quit this progam?\n\n")
    
            if choice in ["Yes","yes","y","Ye","ye","Y"]:
              print("\nYou have quitted the program.\n")
              keeplooping = False
              lang= False
              running = False
              
        
            elif choice in ["No","N","n","no"]:
              keeplooping = False
              running = True
            
            else:
              print("\nPlease enter either \"Yes\" or \"No\" \n ")
              keeplooping = True
            
      elif cmd < 0:
          print("\n * * * Sorry, please enter a positive number. * * *\n")
          running = True
          
      else: 
          print("\n * * * Please enter a number from 1 through 5. * * *\n")
          running = True
          
    if lang2 == 2:
      print("------------------------------------------")
      print("Bienvenido a la Calculadora! (= \n\nLas operaciones son:")
      print("\n1 = Sumar")
      print("2 = Restar")
      print("3 = Multiplicacion")
      print("4 = Division")
      print("5 = Salir del programa \n ")
        
      cmd = input("Elije un numero: ")
      cmd = int(cmd)
    
      if cmd == 1:
          adding = True
          while adding:
            
            print("-------------------------------------")
            print("Addition\n")
            first = int(input("Enter your first number :"))
            second = int(input("Enter your second number :"))
            print("-------------------------------------")
            print("Answer:\n")
            print(first + second)
            print("----------------------------------------------------")
            
            asking = True
            while asking:
              choice = raw_input("Do you want to continue adding?\n\n")
    
              if choice in ["Yes","yes","y","Ye","ye","Y"]:
                print("\nOkay! Let's continue adding.\n")
                asking = False
                adding = True
        
              elif choice in ["No","N","n","no"]:
                print("\nOkay, I guess we're done adding.\n")
                asking = False
                adding = False
                
                running2 = True
                while running2:
                  choice = raw_input("Do you still want to use the calculator?\n")
                  
                  if choice in ["Yes","yes","y","Ye","ye","Y"]:
                    print("\nOkay! Let's continue.\n")
                    running2 = False
                    running = True
                  elif choice in ["No","N","n","no"]:
                    print("\nOkay then, We're done.")
                    running2 = False
                    running = False
                  else:
                    print("\nPlease enter either \"Yes\" or \"No\" \n ")
                    running2 = True
              else:
                print("\nPlease enter either \"Yes\" or \"No\" \n ")
                asking = True
        
      elif cmd == 2:
          subtracting = True
          while subtracting:
            
            print("----------------------------------------------------")
            print("Subtraction\n")
            first = int(input("Enter your first number :"))
            second = int(input("Enter your second number :"))
            print("----------------------------------------------------")
            print("Answer:\n") 
            print(first - second)
            print("----------------------------------------------------")
            
            asking = True
            while asking:
              choice = raw_input("Do you want to continue subtracting?\n\n")
              if choice in ["Yes","yes","y","Ye","ye","Y"]:
                print("Okay Let's continue subtracting!")
                asking = False
                subtracting = True
    
              elif choice in ["No","N","n","no"]:
                asking = False
                subtracting = False
                
                running2 = True
                while running2:
                  choice = raw_input("Do you still want to use the calculator?\n")
                  
                  if choice in ["Yes","yes","y","Ye","ye","Y"]:
                    print("\nOkay! Let's continue.\n")
                    running2 = False
                    running = True
                  elif choice in ["No","N","n","no"]:
                    print("\nOkay then, We're done.")
                    running2 = False
                    running = False
                  else:
                    print("\nPlease enter either \"Yes\" or \"No\" \n ")
                    running2 = Truerunning = False
                print("\n Done")
              else:
                print("\nPlease enter either \"Yes\" or \"No\" ")
                asking = True
        
      elif cmd == 3:
          print("----------------------------------------------------")
          print("Multiplication\n")
          first = int(input("Enter your first number :"))
          second = int(input("Enter your second number :"))
          result = first * second
          print("----------------------------------------------------")
          print("Answer:\n") 
          print(result)
          print("\nDone")
    
      elif cmd == 4:
          print("----------------------------------------------------")
          print("Division\n")
          first = int(input("Enter your first number :"))
          second = int(input("Enter your second number :"))
          result = first / second
          print("----------------------------------------------------")
          print("Answer:\n") 
          print(result)
          print("\nDone")
            
      elif cmd == 5:
          print("----------------------------------------------------")
          keeplooping = True 
          while keeplooping:
            choice = raw_input("Estás seguro que quieres cerar la aplicaion?\n\n")
    
            if choice in ["Yes","yes","y","Ye","ye","Y","Si","si","s","SI","sI"]:
              print("\nHaz cerado la aplicacion. Gracias.\n")
              keeplooping = False
              lang= False
              running = False
              
        
            elif choice in ["No","N","n","no"]:
              keeplooping = False
              lang = True
            
            else:
              print("\nElije \"Si\" o \"No\" \n ")
              keeplooping = True
            
      elif cmd < 0:
          print("\n * * * Sorry, please enter a positive number. * * *\n")
          running = True
          
      else: 
          print("\n * * * Please enter a number from 1 through 5. * * *\n")
          running = True
        
    else:
      print("\nChoose \"1\" for English.\n\nElije \"2\" para Español.\n")
      lang = True
      
