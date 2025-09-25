"""
Mad Libs generator
Reads a story containing placeholders like <adjective>, <location>, etc.,
asks the user for each word, then prints the completed story.
"""

import os
import re

def main():
    # Always load story.txt from the same folder as this script
    here = os.path.dirname(__file__)
    story_path = os.path.join(here, "story.txt")

    with open(story_path, "r", encoding="utf-8") as f:
        story = f.read()

    # Find placeholders like <noun>, <adjective> … (without the angle brackets)
    placeholders = re.findall(r"<([^>]+)>", story)

    # Keep order but make unique (dict preserves insertion order)
    unique_placeholders = list(dict.fromkeys(placeholders))

    answers = {}
    for ph in unique_placeholders:
        user_input = input(f"Enter a word for {ph}: ").strip()
        answers[ph] = user_input

    # Replace each <placeholder> with the user’s answer
    for ph, val in answers.items():
        story = story.replace(f"<{ph}>", val)

    print("\n" + story)

if __name__ == "__main__":
    main()
