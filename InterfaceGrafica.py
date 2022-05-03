import PySimpleGUI as sg
import igBot as kingo

class InterfaceGrafica:
    def __init__(self):
        layout = [
            [sg.Text("Usuario"), sg.Input(key="Username")],
            [sg.Text("Senha"), sg.Input(key="Password", password_char="*")],
            [sg.Text("Caminho"), sg.Input(key="Path")],
            [sg.Button('Enviar')]
        ]

        #Janela
        janela = sg.Window("Bot Instagram").layout(layout)
        self.button, self.values = janela.read()

    def Iniciar(self):
        username = self.values["Username"]
        password = self.values["Password"]
        path = self.values["Path"]
        print(f'Username: {username}')
        print(f'Password: {password}')
        print(f'Password: {path}')
        iniciar = kingo.InstagramBot(username, password, path)
        iniciar.login()

tela = InterfaceGrafica()
tela.Iniciar()
