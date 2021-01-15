number1 = float(input("Enter the first operand: "))
number2 = float(input("Enter the second operand: "))
calculation_operation = input("Enter a operation('+','-','%','x','/','^') ")

if calculation_operation == "+":
    print(number1+number2)
elif calculation_operation == "-":
    print(number1-number2)
elif calculation_operation == "%":
    print(number1%number2)
elif calculation_operation == "x":
    print(number1*number2)
elif calculation_operation == "/":
    print(number1/number2)
elif calculation_operation == "^":
    print(number1**number2)
else:
    print("I don't understand the command")


#quiz
ans = input("Are you ready to start the the quiz(yes/no)").lower()
score = 0
total_q = 5

if ans == 'yes':

    q1 = input("What is the capital of India :")
    print(q1)
    if q1.lower() == 'new delhi':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    question2 = input("What is capital of pakistan:")
    print(question2)
    if question2 .lower() == 'islamabad':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    q3 = input("What is the capital of sri lanka:")
    print(q3)
    if q3.lower() == 'colombo':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    q4 = input("what is the capital of nepal :")
    print(q4)
    if q4.lower() == 'kathamandu':
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    q5 = input("what is the capital of bhutan :")
    print(q5)
    if q5.lower() == 'thimpu':
        score += 1
        print("Correct")
    else:
        print("Incorrect")


print("your score is", score)

percent = score / total_q * 100

print(percent)

#car game

command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started =False
            print("car stoped")
    elif command == "help":
        print('''start = to start the car
                 stop = to stop the car
                 quit = to quit the game''')
    elif command == "quit":
        print("game ended")
    else:
        print("I dont't understand the command")

#for loops

for item in range[11]:
    print(item)




