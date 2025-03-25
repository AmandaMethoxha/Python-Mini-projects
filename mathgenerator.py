# generate a bunch of random math questions, ask the user and dont move to the next question without the right answer.
# time how long it takes the user to answer the questions

import random
import time
OPERATORS = ["+", "-", "*"]   # string with python operators
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

#expr, answer = generate_problem()
#print(expr,answer)

wrong = 0
input ("press enter to start!")
print("-------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem nr #" + str(i+1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("-------------")
print("Nice work!You finished in", total_time, "seconds!")