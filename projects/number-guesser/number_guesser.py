import random

LOW, HIGH = 1, 100

def get_int(prompt):
    while True:
        s = input(prompt).strip()
        if s.lstrip("-").isdigit():
            return int(s)
        print("Please enter a whole number.")

def main():
    print(f"=== Number Guesser ({LOW}–{HIGH}) ===")
    secret = random.randint(LOW, HIGH)
    attempts = 0

    while True:
        guess = get_int("Your guess: ")
        attempts += 1

        if guess < LOW or guess > HIGH:
            print(f"Stay within {LOW}–{HIGH}.")
            continue

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"🎉 Correct! You got it in {attempts} attempts.")
            break

    # play again?
    again = input("Play again? (y/n): ").strip().lower()
    if again in {"y", "yes"}:
        print()
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
