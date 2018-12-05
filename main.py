import Character
import random

def yes_or_no():
    return "[ y or n ] "

def main():
    characters = list()
    with open('characters.txt','r') as f:
        for line in f:
            characters.append(line.split())

    another_one = True

    while another_one:
        current_characters = characters
        while len(current_characters) > 1:
            random_question = random.randint(0, 8)
            random_character = random.choice(current_characters)
            answer = True
            current_characters = list(filter(lambda x: x[random_question + 1] == random_character[random_question + 1] if answer \
                    else x[random_question + 1] != random_character[random_question + 1], current_characters))

        for character in current_characters:
            print(character)

        answer = input("another one? " + yes_or_no())
        another_one = answer == "y" or answer == "Y"

if __name__ == "__main__":
    main()
