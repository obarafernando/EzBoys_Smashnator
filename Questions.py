import Character

def randomQuestion(character, randomIndex):
    question = character
    questionIndex = randomIndex
    if questionIndex == 0:
        questionString = 'O personagem é o: ' + question.name + '?'
    if questionIndex == 1 and question.gender == 'masculino':
        questionString = 'O personagem é masculino?'
    if questionIndex == 1 and question.gender == 'feminino':
        questionString = 'O personagem é feminino?'
    if questionIndex == 1 and question.gender == 'nao tem':
        questionString = 'O personagem não tem gênero?'
    if questionIndex == 2:
        questionString = 'O personagem pertence ao jogo: ' + question.game + '?'
    if questionIndex == 3:
        questionString = 'O personagem é humano?'
    if questionIndex == 4:
        questionString = 'O personagem é antagonista?'
    if questionIndex == 5:
        questionString = 'O personagem é um Pokemon?'
    if questionIndex == 6:
        questionString= 'O personagem é o mais conhecido do mundo dele?'
    if questionIndex == 7:
        questionString = 'O personagem é uma variação da série original?'
    if questionIndex == 8:
        questionString = 'O personagem é uma criança?'
    if questionIndex == 9:
        questionString = 'O personagem é considerado Top Tier?'

    return questionString

