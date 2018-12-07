from Character import Character
from Questions import randomQuestion
from Questions import randomIndex
import random

def yes_or_no():
    return "[ y or n ] "

def answer_to_bool(answer):
    return answer == "y" or answer == "Y"

def comparation_string(index, answer, character):
    if index > 2:
        return "s"
    else:
        return character[index]

def main():
    characters = list()
    with open('characters.txt','r') as f:
        for line in f:
            characters.append(Character(line.split()))

    another_one = True

    while another_one:
        current_characters = characters
        while len(current_characters) > 1:
            random_question = randomIndex(current_characters)
            random_character = random.choice(current_characters)
            answer = answer_to_bool(input(randomQuestion(random_character, random_question) + " " + yes_or_no()))
            compare_string = comparation_string(random_question, answer, random_character)
            current_characters = list(filter(lambda x: x[random_question] == compare_string if answer \
                    else x[random_question] != compare_string, current_characters))

        if not current_characters:
            print("do not know this character")
        else:
            answer = answer_to_bool(input(randomQuestion(current_characters[0], 0) + " " + yes_or_no()))
            print('Ez Boys' if answer else "do not know this character")

        answer = answer_to_bool(input("another one? " + yes_or_no()))
        another_one = answer

if __name__ == "__main__":
    main()
