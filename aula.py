import random
perguntas = { 1:{
                'questao':'quanto e 2+2?',
                'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                'gabarito': 'C'},
                2:{
                'questao':'quanto e 2+1?',
                'resposta' : {'A':'3', 'B': '2', 'C':'4', 'D': '6'},
                'gabarito': 'A'},
                3:{
                'questao':'quanto e 2+4?',
                'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                'gabarito': 'D'},   
                4:{
                'questao':'quanto e 2/2?',
                'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                'gabarito': 'A'},
                5:{
                'questao':'quanto e 2x4?',
                'resposta' : {'A':'3', 'B': '8', 'C':'4', 'D': '6'},
                'gabarito': 'B'},
                6:{
                'questao':'quanto e 4-3?',
                'resposta' : {'A':'7', 'B': '2', 'C':'1', 'D': '6'},
                'gabarito': 'C'}  
}

"""#funcao a ser implementada recebe um int e retorna
    #str = Pergunta
    #lista = Opções Randomizadas
    #str = Gabarito
def busca_questao(num_questao): 
    print('Hello world!') """
#compara os gabaritos e retorna nota e quais questoes erradas
def gerador_questao(num_questao:int,banco_questoes:dict )->list:
    """A ser implementada"""
    """Recebe a quantidade de questoes e retorna uma lista com as n questoes e o gabarito da prova"""
    
def corretor(resp:list,gab:list)->list:
    """Corrigir a prova, recebe o gabarito e as resposta e retornar nota do aluno com uma lista das respostas certas e erradas."""
    qtd = len(gab)
    peso_nota = 10.0/qtd
    nota = 0.0
    correcao = []
    for r, g in zip(resp, gab):
        if r == g:
            correcao.append(1)
            nota += peso_nota
        else:
            correcao.append(0)
    return nota , correcao

numero_de_questoes = 2
nota_aluno = 0
if numero_de_questoes == 0: numero_de_questoes += 1
sorteio = random.sample(range(1,6),numero_de_questoes)
print(sorteio)
gabarito_aluno = []
gabarito_prova = []
numero_de_questores = int(input("Numero de questoes: "))
if numero_de_questores == 0:
    numero_de_questores += 1
sorteio = random.sample(range(1,6),numero_de_questores)

for i in sorteio:
    print(perguntas[i]['questao'])
    for n in perguntas[i]['resposta']:
        print(f"{n} - {perguntas[i]['resposta'][n]}")
    resposta_aluno = str.capitalize(input("Digite sua resposta: "))
    gabarito_aluno.append(resposta_aluno)
    gabarito_prova.append(perguntas[i]['gabarito'])
    
#CORREÇÃO DA PROVA E NOTA DO ALUNO
nota_aluno = corretor(list(gabarito_aluno),list(gabarito_prova))
print(f"A nota do aluno foi: {nota_aluno[0]}")
print(f"Os acertos do aluno: {nota_aluno[1]}")