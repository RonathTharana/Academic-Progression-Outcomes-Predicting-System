# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student UoW ID: w1986580
# Student IIT ID: 20221889
# Date: 29 July 2023


# Importing files into the main file
from part_1 import run_program as run_program1
from part_2 import run_program as run_program2
from part_3 import run_program as run_program3
from part_4 import run_program as run_program4

#------Reference for the import :- https://realpython.com/python-import/#:~:text=In%20Python%2C%20you%20use%20the,while%20keeping%20your%20projects%20maintainable.


# Printing instructions about the program to the user
def info():                         
    print("\nWelcome to progression checker!")
    print("\nPart 1 - Student version"
          "\nPart 2 - Staff version - Histogram (list)"
          "\nPart 3 - Staff version - Histogram (Text file)"
          "\nPart 4 - Staff version - Histogram (Dictionary)")
    print("\nOptions"
          "\nEnter 1 for Part 1"
          "\nEnter 2 for Part 2"
          "\nEnter 3 for Part 3"
          "\nEnter 4 for Part 4")

    

# Asking for input and checking whether they are correct
def start_program():
    info()

    while True:
        try:
            number = int(input("\nEnter your number from the above options (Enter 0 to exit): "))
            if number in range(0, 5):
                if number == 1:
                    run_program1()
                elif number == 2:
                    run_program2()
                elif number == 3:
                    run_program3()
                elif number == 4:
                    run_program4()
                else:
                    break
            else:
                print("Out of range. Try again")
        except ValueError:
             print("Invalid input. Try again")
             continue

# Running the program
start_program()
