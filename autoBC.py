from asyncore import write
from curses import mouseinterval
from subprocess import run
from platform import platform, system
from sys import modules
from os.path import isdir, isfile, realpath, dirname
from os import listdir

#request(plataform)  <-------------------------------------------
plataform = system()
dir = dirname(realpath(__file__))

print('Sistema identificado: {}'.format(plataform))

def requests():
    
    if 'selenium' not in modules:

        print("Dependência não encontrada: Selenium")
        print("Instalando Selenium ...")

        run(['python3','-m','pip','install','selenium'])

    if 'webdriver_manager' not in modules:

        print("Dependência não encontrada: Webdriver Manager")
        print("Instalando Webdriver Manager ...")

        run(['python3','-m','pip','install','webdriver_manager'])

    if plataform == 'Linux':

        run(['dpkg','-l','|','grep','chromedriver','>>','teste.txt'])

        file = open('teste.txt','r+')
        pacotes = file.readlines()
        file.close()

        if 'chromedriver' not in list(pacotes[0]):
            input("O drive de automação não está instalado, para continuar instale o pacote chromium-chromedriver.\nUse o comando 'sudo apt-get install chromium-chromedriver'.\n Depois continue.")
 
if not isfile('user.txt'):

    requests()
    print("Não há usuário registrado.\nPreencha com atencao...\n\n")

    user = input("Digite o código de barras: ")
    password = input ("Digite a senha: ")

    file = open ('user.txt','w')
    file.write (user + '\n' + password+'\n')

    file.close()

if plataform == 'Windows':
    if not isdir('C:\Program Files\Google\Chrome\Application'):
        try:
            run(['start', r'chromesetup\ChromeSetup.exe'])
        except:
            print("Instale o Chrome, há um instalador na pasta 'chromesetup', realize a instalação e me execute novamente.")

if plataform == 'Linux':
    
    input("Instale o Chrome, há um instalador na pasta 'chromesetup', realize a instalação e me execute novamente.")
    exit()


#Drive de automação do navegador
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
###############################################

def bot(system,username, password, renew =True, consult = False):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    if system == 'Windows':
        browser = webdriver.Chrome (executable_path = r"chromedrive\chromedriver.exe", options= options)
    if system == 'Linux':
        from webdriver_manager.chrome import ChromeDriverManager
        browser = webdriver.Chrome (ChromeDriverManager().install(), options= options)

    browser.get("http://virtua.uel.br:8080/auth/login?")
    browser.find_element(By.NAME,"username").send_keys(username)
    browser.find_element(By.NAME,"password").send_keys(password + Keys.RETURN)
    
    if renew:
        browser.find_element(By.NAME,"button.selectAll").click()
        browser.find_element(By.ID,"button.renew").click()
        
    if consult:
        pass
    
    browser.quit()


def user_file():
    dir = dirname(realpath(__file__))

    if isfile('user.txt'):

        file = open ('user.txt','r')

        user = file.readline()
        user = user[:-1]

        password = file.readline()
        password = password[:-1]
        file.close()

        bot (plataform,user, password, renew=False, consult=True)

user_file()
