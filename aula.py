import random
perguntas = { '1':{
                'questao':'quanto é 2+2?',
                    'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                    'gabarito': 'C'},
                '2':{
                'questao':'quanto é 2+1?',
                    'resposta' : {'A':'3', 'B': '2', 'C':'4', 'D': '6'},
                    'gabarito': 'A'},
                '3':{
                'questao':'quanto é 2+4?',
                    'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                    'gabarito': 'D'},   
                '4':{
                'questao':'quanto é 2/2?',
                    'resposta' : {'A':'1', 'B': '2', 'C':'4', 'D': '6'},
                    'gabarito': 'A'},
                '5':{
                'questao':'quanto é 2x4?',
                    'resposta' : {'A':'3', 'B': '8', 'C':'4', 'D': '6'},
                    'gabarito': 'B'},
                '6':{
                'questao':'quanto é 4-3?',
                    'resposta' : {'A':'7', 'B': '2', 'C':'1', 'D': '6'},
                    'gabarito': 'C'}  
}

sorteio = random.sample(range(1,6),4)
print(sorteio)
#ETAPA1:criar um lista com 5 numeros randomicos referente ao indice das questos da prova 
#def sorteio_prova():
#    rd.sample
#  salvar os numeros em sequencia numa lista/dict 
