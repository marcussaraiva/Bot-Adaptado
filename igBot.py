from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password, path):
        self.username = username
        self.password = password
        self.path = path
        #self.profile = 'dollynhocoach'
        # self.driver = webdriver.Firefox(executable_path="C:\\Users\\Serjao\\Desktop\\geckodriver.exe")
        self.driver = webdriver.Firefox(executable_path="C:\\Users\\mvfsa\\OneDrive\\Área de Trabalho\\Pastas\\igBot\\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(10)
        '''
        botao_login = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        botao_login.click()
        ''' 
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
            try:
                # comentario_fixo = ["@karolabreu5 "]
                # comentarios = ["@marcus.saraiva18", "@marcus.saraiva18", "@marcus.saraiva18", "@__gaabreu", "@dudalyra5", "@isa_fs", "@don.bre", "@lgsaraiva76", "@finattidelainecristina", "@__gaabreu", "@__gaabreu"]
                comentarios = ["Que princesa linda!!!", "Linda demais. amo mto!!!"]
                i=0
                while(i!=2):
                    driver.find_element_by_class_name("Ypffh").click()
                    campo_comentario = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(2,5))
                    # Acrescentar for para número de perfis por comentário
                    #self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario) 
                    # self.digite_como_uma_pessoa(comentario_fixo,campo_comentario)
                    #time.sleep(random.randint(2,5))
                    self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
                    time.sleep(random.randint(3,5))
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