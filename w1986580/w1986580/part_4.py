# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student UoW ID: w1986580
# Student IIT ID: 20221889
# Date: 29 July 2023


progress = 0
module_trailer = 0
module_retriever = 0
exclude = 0
outcome = 0

progress_list = {}

# Asking for credit inputs and checking for errors
def ask_result(grade):
    try:
        answer = int(input(f"Please enter your credits at {grade}: "))
        if answer not in range(0, 130, 20):
            print("Out of range")
            return ask_result(grade)
        else:
            return answer
    except ValueError:
        print("Integer required")
        return ask_result(grade)


    
# Checking progression outcome, the student ID and credits at pass, defer, fail
def progression_level():
    global progress
    global module_trailer
    global module_retriever
    global exclude
    global outcome
    while True:
        try:
            
            detail_list = []
            pass_level = ""
            
            ask_id = input("\nEnter your student ID (e.g.w1234567): ")   # Getting student ID
            id_length = len(ask_id)
            if id_length == 8:
                if ask_id in progress_list:
                    print("Entered UoW ID already exist")
                    continue
                else:
                    result_pass = ask_result("pass")

                    result_defer = ask_result("defer")

                    result_fail = ask_result("fail")

                    total = result_pass + result_defer + result_fail

                    if total != 120:
                        print("Total incorrect")
                        continue
                    else:                       # Checking for progression outcomes
                        if result_pass == 120:
                            pass_level = "Progress"
                            progress += 1
                        elif result_pass == 100:
                            pass_level = "Progress (module trailer)"
                            module_trailer += 1
                        elif result_fail >= 80:
                            pass_level = "Exclude"
                            exclude += 1
                        else:
                            pass_level = "Do not progress – module retriever"
                            module_retriever += 1
                        print(pass_level)
                        outcome += 1

                    detail_list.append(pass_level)
                    detail_list.append(result_pass)
                    detail_list.append(result_defer)
                    detail_list.append(result_fail)
                    
                    progress_list[ask_id] = detail_list   # Adding data to the progress list dictionary

                        
            else:
                print("Invalid input")
                continue

        except ValueError:
            print("Integer required")
            continue

        break


# Reading progression list data from the textfile
def read_file():
    with open('part_4 (save file - dictionary).txt', 'r') as f:
        output = f.read()
        print(output)
    
#------reference for read file :- https://www.pythontutorial.net/python-basics/python-read-text-file/       



# Asking for another set of data and Calling for the histogram     
def run_program():
    progression_level()

    while True:
        further_more = input("\nWould you like to enter another set of data?" '\n' "Enter 'y' for yes or 'q' to quit and view results: ")   # Asking user wish to continue or not
        if further_more == "y":
           progression_level()
           continue
        elif further_more == "q":
           with open('part_4 (save file - dictionary).txt', 'w') as f:
                print("-" * 60, "\nHistogram") 
                print(f"Progress {progress}   : {'*' * progress}")
                print(f"Trailer {module_trailer}    : {'*' * module_trailer}")
                print(f"Retriever {module_retriever}  : {'*' * module_retriever}")
                print(f"Excluded {exclude}   : {'*' * exclude}")
                print()
                print(f"{outcome} outcomes in total")
                print("-" * 60, "\n")

                #------reference for the histogram :- https://realpython.com/python-histograms/


                print("Part 4:")
                for progression_data in progress_list:  # Getting progression data from progress list dictionary and printing the data
                    data = progress_list[progression_data]
                    output = (f"{progression_data} : {data[0]} - {str(data[1:])[1:-1]}")
                    f.write(f"{output}\n")   # Saving progression list dictionary data to the textfile
                    print(output)
                print("\n")
                break
            
        else:
            print("Invalid input. Try again")


    print("Part 3:")  # Reading the saved data in the file and print the data
    read_file()

#------reference for the functions :- https://www.programiz.com/python-programming/function


