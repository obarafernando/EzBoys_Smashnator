import Character
import random

def yes_or_no():
    return "[ y or n ] "

def answer_to_bool(answer):
    return answer == "y" or answer == "Y"

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
            answer = random.choice([True, False])
            current_characters = list(filter(lambda x: x[random_question + 1] == random_character[random_question + 1] if answer \
                    else x[random_question + 1] != random_character[random_question + 1], current_characters))

        if not current_characters:
            print("do not know this character")
        else:
            print(current_characters[0])

        answer = answer_to_bool(input("another one? " + yes_or_no()))
        another_one = answer

if __name__ == "__main__":
    main()
