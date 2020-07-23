# Mode selection for add, subtract, divide, multiply 
   #divide needs to return integers. 
#selection for number of problems to solve.
#answer again if the answer is wrong the first time. 
#timed?
    #fetch world time at start and end
#chose between different digit ranges, levels 1 - 10 
    #show the numbers that you will get on each level
#combine stuff into more functions to make the code shorter
import random
####
def addition():
    correct_answers = 0
    diff_level_min = [1, 1, 10, 20, 40, 50, 50, 100, 50, 50]
    diff_level_max = [10, 20, 40, 50, 60, 100, 150, 200, 250, 500]
    for i in range(number_questions):
        number_1 = random.randint(diff_level_min[question_diff],diff_level_max[question_diff])
        number_2 = random.randint(diff_level_min[question_diff],diff_level_max[question_diff])
        solution = number_1 + number_2
        number_1_str = (3 - len(str(number_1))) * " " + str(number_1)
        number_2_str = (3 - len(str(number_2))) * " " + str(number_2)
        check_solution = 0
        first_attempt = 1
        while check_solution == 0:
            print("What is ", number_1_str, "\n      + ", number_2_str, "?")
            user_solution = int(input("Answer: "))
            if solution == user_solution:
                print("Correct!")
                if first_attempt == 1:  #only gives a point if the answer was right the first time.
                    correct_answers += 1
                check_solution = 1 
            else:
                print("Incorrect answer, try again...")
                first_attempt = 0
    print("\nYou scored: " + str(correct_answers)+"/" + str(number_questions) + "\n")
    correct_percentage = correct_answers / number_questions * 100
    correct_percentage = round(correct_percentage)  #rounding to 0 decimal places omits the second argument
    print(str(correct_percentage) + "% correct")
####
####
def subtraction():
    correct_answers = 0
    for i in range(number_questions):
        diff_level_min = [2, 10, 20, 30, 30, 50, 75, 100, 400, 750]
        diff_level_max = [10, 20, 30, 40, 60, 80, 100, 140, 500, 1000]
        number_1 = random.randint(diff_level_min[question_diff],diff_level_max[question_diff])
        diff_level_min = [1, 8, 5, 10, 10, 30, 5, 25, 50, 50]    #different ranges are wanted for each number 
        diff_level_max = [9, 19, 19, 20, 40, 70, 95, 95, 450, 950]
        redraw = 1 
        while redraw == 1:  #only continues when number 1 is bigger than number 2. If this doesn't happen there will be negatives
            number_2 = random.randint(diff_level_min[question_diff],diff_level_max[question_diff])
            if number_1 > number_2:
                redraw = 0
        solution = number_1 - number_2
        number_1_str = (3 - len(str(number_1))) * " " + str(number_1)
        number_2_str = (3 - len(str(number_2))) * " " + str(number_2)
        check_solution = 0
        first_attempt = 1
        while check_solution == 0:
            print("\nWhat is ", number_1_str, "\n      - ", number_2_str, "?")
            user_solution = int(input("Answer: "))
            if solution == user_solution:
                print("Correct!")
                if first_attempt == 1:  #only gives a point if the answer was right the first time.
                    correct_answers += 1
                check_solution = 1 
            else:
                print("Incorrect answer, try again...")
                first_attempt = 0
    print("\nYou scored: " + str(correct_answers)+"/" + str(number_questions))
    correct_percentage = correct_answers / number_questions * 100
    correct_percentage = round(correct_percentage)  #rounding to 0 decimal places omits the second argument
    print(str(correct_percentage) + "% correct", end = "\n\n")
####
##########################################################################################################################################################  Main Code ####################
print("Welcome to the mental maths trainer\nYou can pick the type of problems to solve, how many, and how difficult.", end = "\n\n")
number_questions = int(input("Choose the number of questions to solve: "))
question_type =  str(input("Choose types of question to answer.\n(A) Addition\n(S) Subtraction\n(M) Multiplication\n(D) Division\nSelection: "))
question_diff = int(input("Choose diff level (1-10): "))
question_diff -= 1 # turns 1-10 to position 0-9



if question_type == "A" or question_type == "a":
    addition()
elif question_type == "S" or question_type == "s":
    subtraction()
elif question_type == "M" or question_type == "m":
    multiplication()
elif question_type == "D" or question_type == "d":
    division()
else:
    print("error, option not found.")