print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's play :) ")
score = 0
total = 4

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit" :
    print('Correct')
    score += 1
else:
    print("Incorrect!")


answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit" :
    print('Correct')
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory" :
    print('Correct')
    score += 1
else:
    print("Incorrect!")


answer = input("What does PSU stand for? ").strip().lower()
if answer in ("power supply unit", "power supply"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

pct = (score / total) * 100
print(f"You got {score} out of {total} correct — {pct:.0f}%")
