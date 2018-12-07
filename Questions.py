import Character
import random

def randomQuestion(character, randomIndex):
    question = character
    questionIndex = randomIndex
    if questionIndex == 0:
        questionString = 'O personagem e o/a: ' + question.name + '?'
    if questionIndex == 1 and question.gender == 'masculino':
        questionString = 'O personagem e masculino?'
    if questionIndex == 1 and question.gender == 'feminino':
        questionString = 'O personagem e feminino?'
    if questionIndex == 1 and question.gender == 'nao_tem':
        questionString = 'O personagem nao tem genero?'
    if questionIndex == 2:
        questionString = 'O personagem pertence ao jogo: ' + question.game + '?'
    if questionIndex == 3:
        questionString = 'O personagem e humano?'
    if questionIndex == 4:
        questionString = 'O personagem e antagonista?'
    if questionIndex == 5:
        questionString = 'O personagem e um Pokemon?'
    if questionIndex == 6:
        questionString= 'O personagem e o mais conhecido do mundo dele?'
    if questionIndex == 7:
        questionString = 'O personagem e uma variacao da serie original?'
    if questionIndex == 8:
        questionString = 'O personagem e uma crianca?'
    if questionIndex == 9:
        questionString = 'O personagem e considerado Top Tier?'

    return questionString


def randomIndex(current_characters):
    available_characters = current_characters
    index_avaible = []
    gender = available_characters[0].gender
    game = available_characters[0].game
    human = available_characters[0].human
    antagonist = available_characters[0].antagonist
    pokemon = available_characters[0].pokemon
    most_known = available_characters[0].most_known
    variation = available_characters[0].variation
    child = available_characters[0].child
    top_tier = available_characters[0].top_tier

    if len(available_characters) == 1:
        index_avaible.append(0)
    for x in range(0, len(available_characters)):
        if available_characters[x].gender != gender:
            index_avaible.append(1)
    for x in range(0, len(available_characters)):
        if available_characters[x].game != game:
            index_avaible.append(2)
    for x in range(0, len(available_characters)):
        if available_characters[x].human != human:
            index_avaible.append(3)
    for x in range(0, len(available_characters)):
        if available_characters[x].antagonist != antagonist:
            index_avaible.append(4)
    for x in range(0, len(available_characters)):
        if available_characters[x].pokemon != pokemon:
            index_avaible.append(5)
    for x in range(0, len(available_characters)):
        if available_characters[x].most_known != most_known:
            index_avaible.append(6)
    for x in range(0, len(available_characters)):
        if available_characters[x].variation != variation:
            index_avaible.append(7)
    for x in range(0, len(available_characters)):
        if available_characters[x].child != child:
            index_avaible.append(8)
    for x in range(0, len(available_characters)):
        if available_characters[x].top_tier != top_tier:
            index_avaible.append(9)
    index_avaible = set(index_avaible)
    index_avaible = random.sample(index_avaible, 1)
    index_avaible = index_avaible[0]
    return index_avaible
