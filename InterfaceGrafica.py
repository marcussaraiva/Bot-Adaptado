import PySimpleGUI as sg
import igBot as kingo

class InterfaceGrafica:
    def __init__(self):
        layout = [
            [sg.Text("Usuario:", size=(10,1)), sg.Input(key="Username", size=(40,1))],
            [sg.Text("Senha:", size=(10,1)), sg.Input(key="Password", size=(40,1), password_char="*")],
            [sg.Text("Caminho:", size=(10,1)), sg.Input(key="Path", size=(40,1))],
            [sg.Text("Quantidade por comentário:", size=(10,1)), sg.Input(key="TotalComment", size=(40,1))],
            [sg.Text("Comentários:", size=(10,1))],
            [sg.Multiline(key="Comments", size=(50, 20))],
            [sg.Button('Enviar')]
        ]

        #Janela
        janela = sg.Window("Bot Instagram").layout(layout)
        self.button, self.values = janela.read()

    def Iniciar(self):
        username = self.values["Username"]
        password = self.values["Password"]
        path = self.values["Path"]
        comments = self.values["Comments"]
        totalComment = self.values["TotalComment"]
        
        # print(f'Username: {username}')
        # print(f'Password: {password}')
        # print(f'Password: {path}')
        # print(f'Comments: {comments}')
        iniciar = kingo.InstagramBot(username, password, path, comments, totalComment)
        iniciar.login()            

tela = InterfaceGrafica()
tela.Iniciar()