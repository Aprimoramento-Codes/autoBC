
#Drive de automação de navegador
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from platform import system
#from bs4 import BeautifulSoup

import os

dir = os.path.dirname(os.path.realpath(__file__))

system = system ()

#request(plataform)  <-------------------------------------------
plataform = plataform ()

dir = dirname(realpath(__file__))

def request(system): 
    if system =='Windows':
        if 'selenium' not in modules:
            run(['python','-m','pip','install','selenium'])     
    if system == 'Linux':
        if 'selenium' not in modules:
            run(['python3','-m','pip','install','selenium'])

request(plataform)

def bot(username, password, renew =True, consult = False):

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    browser = webdriver.Chrome (executable_path = r"" + dir +r"\chromedriver.exe", options= options)

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
    dir = os.path.dirname(os.path.realpath(__file__))

    if os.path.isfile('user.txt'):

        file = open ('user.txt','r')

        user = file.readline()
        user = user[:-1]

        password = file.readline()
        file.close()

        bot (user, password, True, False)
        
    else:

        print("Não há usuário registrado.")

        user = input("Digite o código de barras: ")
        password = input ("Digite a senha: ")

        file = open ('user.txt','w')
        file.write (user + '\n' + password)

        file.close()

        print("execute novamente")

if __name__ =='__main__':
    user_file()