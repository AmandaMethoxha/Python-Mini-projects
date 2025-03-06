# Mad Libs generator
# We have a story and this story has replacable words like adjective, location... etc
# we will ask the user to give us this words and we will conject them in the story and we will read the story back out to user.

with open("story.txt", "r") as f:
    story = f.read()
    

    words = set()
    start_of_word = -1

    target_start = "<"
    target_end = ">"

    for i, char in enumerate(story):

        if char == target_start:
            start_of_word = i
        
        if char == target_end and start_of_word != -1:
            word = story[start_of_word: i+1]
            words.add(word)  # set unique words in a set
            start_of_word = -1

# i am creating a Dictionary

answers = {}

for word in words:
    answer = input("Enter a word for" + word + ": ")
    answers[word] = answer 

for word in words:
    story = story.replace(word, answers[word])

print(story)