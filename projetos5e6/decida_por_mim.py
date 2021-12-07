import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso não',
            'Melhor esperar mais um pouco',
            'Você tá maluco(a)? Lógico que não',
            'Sim, imediatamente',
            'Só na próxima vez'
        ]

    def Iniciar(self):
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(50,10))],
            [sg.Button('Decida por mim')]
        ]

        self.janela = sg.Window('Decida por Mim!', layout=layout)
        while True:

            self.eventos, self.valores = self.janela.Read()

            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
            else:
                sg.WIN_CLOSED
            
        window.close()

decida = DecidaPorMim()
decida.Iniciar()