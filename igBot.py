from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password, path, comments, totalComment):
        self.username = username
        self.password = password
        self.path = path
        self.comments = comments
        self.totalComment = totalComment
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(10)
        
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)

        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)

        time.sleep(7)
        # Caminho do sorteio
        self.comente_no_sorteio(self.path)

    def selecionar_comentarios(self, comentarios, comentados):
        for comentario in comentarios:
            if comentario not in comentados:
                    comentados.append(comentario)
                    if(len(comentados) == len(comentarios) and comentario == comentarios[0]):
                        continue
                    return comentario
            elif(len(comentarios) == len(comentados)):
                # comentados.clear()
                comentados.remove(comentario)
                return comentario
            else:
                continue;

            # Primeiro comentário
            # if(len(comentados) == 0):
            #     comentados.append(comentario)
            #     return comentario
            # # Último comentário
            # elif(len(comentarios) == len(comentados)):
            #     comentados.clear()
            #     return comentario
            # #Comentário "regular"                
            # else:
            #     if comentario not in comentados:
            #         comentados.append(comentario)
            #         return comentario

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comente_no_sorteio(self,sorteio):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ sorteio +"/")
        time.sleep(5) 
        
        contador=0
        while(0!=1):
            comentados = []
            try:
                comentarios = []
                comentarios = self.comments.split(",")
                i=0
                while(i!=2):
                    driver.find_element_by_class_name("Ypffh").click()
                    campo_comentario = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(2,5))
                    j = 0
                    # Acrescentar for para número de perfis por comentário
                    for j in range(int(self.totalComment)):
                        # self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
                        self.digite_como_uma_pessoa(self.selecionar_comentarios(comentarios, comentados),campo_comentario)
                        time.sleep(random.randint(3,5))

                        #self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario) 
                        # self.digite_como_uma_pessoa(comentario_fixo,campo_comentario)
                        #time.sleep(random.randint(2,5))
                    # Terminar for aqui
                    campo_comentario.send_keys(Keys.RETURN)
                    campo_comentario.send_keys(Keys.RETURN)
                    campo_comentario.send_keys(Keys.RETURN)
                    contador = contador + 1
                    # Total de comentarios feitos
                    print(contador)
                    i = i + 1
                    # Fim
                    time.sleep(random.randint(10,20))
                time.sleep(random.randint(180,240))
            except Exception as e:
                print(e)
                time.sleep(5)