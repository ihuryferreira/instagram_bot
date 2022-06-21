from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, login, password):
        # Adicionando o endereço da pasta onde fica o chromedriver.exe
        chromedrive_path = './chrome-win/chromedriver.exe'
        #executando o chromedrive
        self.bot = webdriver.Chrome(executable_path=chromedrive_path)
        #esperar 2 segundos
        time.sleep(2)
        #carregando a página do instagram
        self.bot.get('https://www.instagram.com/accounts/login/')
        #esperando 4 segundos
        time.sleep(4)
        # Pegando o name do login do input do instagram
        usuario = self.bot.find_element(by=By.NAME, value='username')
        usuario.clear() # limpando o input
        #Espera 2 segundos
        time.sleep(2)
        # adicionando o login do usuario
        usuario.send_keys(login)
        #Espere 2 segundos
        time.sleep(2)
        #Pegando o name da senha
        senha = self.bot.find_element(by=By.NAME, value='password')
        senha.clear() # limpando o input
        # adicionando a senha
        senha.send_keys(password)
        #esperar 2 segundos
        time.sleep(2)
        # botao de confirmar o login e senha
        botao = self.bot.find_element(by=By.NAME, value='password')
        botao.send_keys(Keys.RETURN)

    def eliminando_botoes_indesejados(self):
        bot = self.bot
        #esperar a página atualizar por 4 segundos
        time.sleep(4)
        #=================
        # botao Agora não
        not_now = bot.find_element(by=By.CSS_SELECTOR, value='button.sqdOP.yWX7d.y3zKF')
        not_now.click() # clicando nele
        time.sleep(5)

        #clicando no botão Agora não
        try:
            not_now2 = bot.find_element(by=By.CSS_SELECTOR, value='button._a9--._a9_1')
            not_now2.click() #confirmando o click
        except Exception as e:
            print(f'Erro: {e}')
            pass
        time.sleep(5)

    def pagina_da_pessoa(self, username_influencer):
        bot = self.bot
        
        bot.get('https://instagram.com/' + username_influencer + '/')
        time.sleep(8)
		
        bot.find_element(by=By.XPATH, value='//div[text()=" seguidores"]').click()
        time.sleep(5)
        
    # def curtir(self):
    #     bot = self.bot
    #     time.sleep(2)
    #     try:
    #         btn_curtir = bot.find_element(by=By.XPATH, value="//button[@class='_acan _acap _acas']")
    #         btn_curtir.click()
    #         time.sleep(2)
    #         print("curtiu")
    #         time.sleep(1)
    #     except Exception as e:
    #         print(f'erro: {e}')
    #         pass

    #     i = 1
    #     while(True):
    #         i+= 100
    #         bot.execute_script(f'window.scrollTo(0,{i})')
    #         self.curtir()

# if '__init__' == __name__:
#     instabot = InstagramBot('ihuryferreira@icloud.com', 'Ihu@2356')
#     time.sleep(10)
#     instabot.eliminando_botoes_indesejados()
#     time.sleep(5)
#     # nome do follower
#     instabot.pagina_da_pessoa('romuloccastro')
#     time.sleep(5)
#     instabot.curtir()

# "ihurybrazul", "Ihu@2356"
# "ihuryferreira@icloud.com", "Ihu@2356"
# "ihgorazul@gmail.com", "Ihg@2356"