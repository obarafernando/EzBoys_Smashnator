import Character

def randomQuestion(character, randomIndex):
    question = character
    questionIndex = randomIndex
    if questionIndex == 0:
        questionString = 'O personagem e o: ' + question.name + '?'
    if questionIndex == 1 and question.gender == 'masculino':
        questionString = 'O personagem e masculino?'
    if questionIndex == 1 and question.gender == 'feminino':
        questionString = 'O personagem e feminino?'
    if questionIndex == 1 and question.gender == 'nao_tem':
        questionString = 'O personagem não tem gênero?'
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
        questionString = 'O personagem e uma variação da serie original?'
    if questionIndex == 8:
        questionString = 'O personagem e uma criança?'
    if questionIndex == 9:
        questionString = 'O personagem e considerado Top Tier?'

    return questionString

