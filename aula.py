import random
perguntas = { '1':{
                'questao':'quanto e 2+2?',
                    'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                    'gabarito': 'C'},
                '2':{
                'questao':'quanto e 2+1?',
                    'resposta' : {'A':'3', 'B': '2', 'C':'4', 'D': '6'},
                    'gabarito': 'A'},
                '3':{
                'questao':'quanto e 2+4?',
                    'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                    'gabarito': 'D'},   
                '4':{
                'questao':'quanto e 2/2?',
                    'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                    'gabarito': 'A'},
                '5':{
                'questao':'quanto e 2x4?',
                    'resposta' : {'A':'3', 'B': '8', 'C':'4', 'D': '6'},
                    'gabarito': 'B'},
                '6':{
                'questao':'quanto e 4-3?',
                    'resposta' : {'A':'7', 'B': '2', 'C':'1', 'D': '6'},
                    'gabarito': 'C'}  
}
def busca_questao(num_questao):
    print('Hello world!') 
#ETAPA1:criar um lista com 5 numeros randomicos referente ao indice das questos da prova 
#def sorteio_prova():
sorteio = random.sample(range(1,6),4)
print(sorteio)
gabarito_aluno = []
for i in sorteio:
    busca_questao(i)
    resposta_aluno = int(input("Digite sua resposta"))
    gabarito_aluno.append(resposta_aluno)
    print(gabarito_aluno)
    for i, perguntas_k, perguntas_v in perguntas.items():
        print(perguntas_k)
    """"for pk in perguntas:
        if i   
        print(f'{pergunta[i]}"""
#  salvar os numeros em sequencia numa lista/dict 
 