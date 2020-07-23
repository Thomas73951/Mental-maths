# Mode selection for add, subtract, divide, multiply 
   #divide needs to return integers. 
#selection for number of problems to solve.
#answer again if the answer is wrong the first time. 
#timed?
#chose between different digit ranges, easy medium hard.
import random

def addition():
    correct_answers = 0
    difficuly_level_min = [1, 1, 10, 20, 40, 50, 50, 100, 50, 50]
    difficuly_level_max = [10, 20, 40, 50, 60, 100, 150, 200, 250, 500]
    for i in range(number_questions):
        number_1 = random.randint(difficuly_level_min[question_difficulty],difficuly_level_max[question_difficulty])
        number_2 = random.randint(difficuly_level_min[question_difficulty],difficuly_level_max[question_difficulty])
        solution = number_1 + number_2
        check_solution = 0
        first_attempt = 1
        while check_solution == 0:
            print("What is ", number_1, "+", number_2, "?")
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


number_questions = int(input("choose the number of questions to solve: "))
question_type =  str(input("Choose types of question to answer.\n(A) Addition\n(S) Subtraction\n(M) Multiplication\n(D) Division\nSelection: "))
question_difficulty = int(input("Choose difficulty level (1-10): "))
question_difficulty -= 1 # turns 1-10 to position 0-9



if question_type == "A" or "a":
    addition()
elif question_type == "S" or "s":
    subtraction()
elif question_type == "M" or "m":
    multiplication()
elif question_type == "D" or "d":
    division()
else:
    print("error, option not found.")