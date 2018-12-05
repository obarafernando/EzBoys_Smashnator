import Character

def main():
    characters = []
    with open('characters.txt','r') as f:
        for line in f:
            characters.append(line.split())

    for character in characters:
        print(character)

if __name__ == "__main__":
    main()
