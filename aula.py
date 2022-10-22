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
def corretor(resp,gab):
    qtd = len(gab)
    print(f"Qunatidade de questoes: {qtd}")
    nota = 0
    correcao = []
    #print(f"Valor{gabarito} // Tipo{type(gabarito)} // Tipo{type(respostas)}")
    if resp==gab:
        nota = 10
        correcao = gab
        return nota
    else:
        print(type(resp))
        print(type(gab)) 
        print('else nota nao foi 10')
        return nota

numero_de_questores = 1
nota_aluno = 0
if numero_de_questores == 0: numero_de_questores += 1
sorteio = random.sample(range(1,6),numero_de_questores)
print(sorteio)
gabarito_aluno = []
gabarito_prova = []
for i in sorteio:
    print(perguntas[i]['questao'])
    print(perguntas[i]['resposta'])
    resposta_aluno = str.capitalize(input("Digite sua resposta: "))
    gabarito_aluno.append(resposta_aluno)
    gabarito_prova.append(perguntas[i]['gabarito'])
#print(f"Gabarito Aluno: {gabarito_aluno}")
#print(f"Gabarito Prova: {gabarito_prova}")
nota_aluno = corretor(list(gabarito_aluno),list(gabarito_prova))
print(f"a nota do aluno foi: {nota_aluno}")