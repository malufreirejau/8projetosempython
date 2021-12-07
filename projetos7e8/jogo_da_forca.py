"""
Cenário do jogo: Descobri que tenho a força dentro de mim e existem 2 lados: jedis e siths. Será que sou um Jedi ou sirvo
o lado negro da força.

"""

import PySimpleGUI as sg

class JogoDaForca:
    def __init__(self):
        self.pergunta1 = 'Você gostaria de um sabre azul ou vermelho? (azul/vermelho)'
        self.pergunta2 = 'Seus poderes vêm da paz ou da emoção? (paz/emoção)'
        self.pergunta3 = 'Qual sua especialidade? (ataque/defesa)'
        self.final1 = 'Você é um Mestre Jedi'
        self.final2 = 'Você é um Jedi que precisa meditar mais e encontrar o equilíbrio'
        self.final3 = 'Você está sendo seduzido pelo lado negro da força, lute contra suas emoções negativas'
        self.final4 = 'Você é um Lord Sith'

    def Iniciar(self):

        layout = [
            [sg.Output(size=(50,0))],
            [sg.Input(size=(40,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
    ]

        self.janela = sg.Window('Jogo da Força!',layout=layout)

        while True:
            
            self.LerValores()
            # fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'azul':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'paz':
                        print(self.final1)
                    if self.valores['escolha'] == 'emoção':
                        print(self.final2)
                if self.valores['escolha'] == 'vermelho':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'defesa':
                        print(self.final3)
                    if self.valores['escolha'] == 'ataque':
                        print(self.final4)
        
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDaForca()
jogo.Iniciar()