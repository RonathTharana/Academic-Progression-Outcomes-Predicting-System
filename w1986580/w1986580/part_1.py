# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student UoW ID: w1986580
# Student IIT ID: 20221889
# Date: 29 July 2023


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
    

# Checking progression outcome and the credits at pass, defer and fail
def progression_level():

    while True:
        try:
            pass_level = ""
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
                elif result_pass == 100:
                    pass_level = "Progress (module trailer)"
                elif result_fail >= 80:
                    pass_level = "Exclude"
                else:
                    pass_level = "Do not progress – module retriever"
                print(pass_level)
                

        except ValueError:
            print("Integer required")
            continue

        break


def run_program():
    progression_level()

#------reference for the functions :- https://www.programiz.com/python-programming/function

    
