import random, time, operator

OPS = {"+": operator.add, "-": operator.sub, "*": operator.mul}
MIN_OPERAND, MAX_OPERAND = 3, 12
TOTAL_PROBLEMS = 10

def generate_problem():
    a = random.randint(MIN_OPERAND, MAX_OPERAND)
    b = random.randint(MIN_OPERAND, MAX_OPERAND)
    op = random.choice(tuple(OPS.keys()))
    return f"{a} {op} {b}", OPS[op](a, b)

def main():
    wrong = 0
    input("press enter to start!")
    print("-------------")
    start = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input(f"Problem nr #{i+1}: {expr} = ").strip()
            if guess == str(answer):
                break
            if guess == "":
                print("Please enter a number.")
                continue
            # optional: allow accidental non-numeric entries without crashing
            if not guess.lstrip("-").isdigit():
                print("Numbers only, try again.")
                wrong += 1
                continue
            wrong += 1

    total = time.time() - start
    print("-------------")
    avg = total / TOTAL_PROBLEMS
    print(f"Nice work! You finished in {total:.2f} seconds.")
    print(f"Wrong attempts: {wrong} | Avg time/question: {avg:.2f}s")

if __name__ == "__main__":
    main()
