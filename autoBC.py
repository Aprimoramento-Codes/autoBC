from os.path import isfile, realpath, dirname
from turtle import delay
from selenium import webdriver    
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from subprocess import run
from datetime import date

clear = lambda: run('cls', shell=True)

dir = dirname(realpath(__file__))

ok = 'OK'
mensagem0 = "Dados do Usuario: "
mensagem1 = "Navegador Automatizado: "
mensagem2 = "Renovação: "
mensagem3 = "Consulta: "
mensagem4 = "Data de renovação: "
mensagem5 = "Agendamento de renovação: "

mensagens = [mensagem0, mensagem1, mensagem2, mensagem3, mensagem4, mensagem5]

def status(num):
    clear()
    for i in range(num):
        print(mensagens[i] + ok)

def bot(username, password, renew =True, consult = True):
    #Drive de automação do navegador
    
    ###############################################

    browser = webdriver.Chrome (service=Service(ChromeDriverManager().install()))
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    browser = webdriver.Chrome (ChromeDriverManager().install(), options= options)
    browser.get("http://virtua.uel.br:8080/auth/login?")
    status(1)
    delay(4)
    browser.find_element(By.NAME,"username").send_keys(username)
    browser.find_element(By.NAME,"password").send_keys(password + Keys.RETURN)
    
    if renew:
        browser.find_element(By.NAME,"button.selectAll").click()
        browser.find_element(By.ID,"button.renew").click()
        status(2)
        
    if consult:
        datas_de_vencimento = []
        quantidade_de_livros = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[5]/div[4]/div[1]/form[1]/table/thead/tr[1]/td/div/div[1]/span").text
        
        if quantidade_de_livros[-2] == ' ':
            quantidade_de_livros = int(quantidade_de_livros[-1])
        else:
            quantidade_de_livros = int(quantidade_de_livros[-2] + quantidade_de_livros[-1])
        for i in range(quantidade_de_livros):
            datas_de_vencimento.append(browser.find_element(By.XPATH,"/html/body/div/div[2]/div[5]/div[4]/div[1]/form[1]/table/tbody/tr[{}]/td[4]/div".format(i+1)).text)
    browser.quit()
    status(3)
    return datas_de_vencimento

def user_file():
    if isfile('user.txt'):

        file = open ('user.txt','r')

        user = file.readline()
        user = user[:-1]

        password = file.readline()
        password = password
        file.close()

        status(0)
    return bot (user, password, renew=True, consult=True)
        
def find_Due_date(datas):
    anos = [int(data[6:]) for data in datas]
    meses =  [int(data[3:5]) for data in datas]
    dias = [int(data[:2]) for data in datas]
    
    if len(set(anos)) == 1:
        if len(set(meses)) == 1:
            if len(set(dias)) == 1:
                data_de_vencimento = datas[0]
            else:
                data_de_vencimento = [datas[i] for i in range(len(datas)) if datas[i] == min(datas)][0]
        else:
            indices_mes = [i for i in range(len(meses)) if meses[i]== min(meses)]
            dias_mes_min = [dias[i] for i in indices_mes]
            data_de_vencimento = [datas[i] for i in range(len(datas)) if dias[i]==min(dias_mes_min)][0]
    else:
        anos = [anos[i] for i in range(len(datas)) if anos[i]==min(anos)]
        indices_anos = [i for i in range(len(datas)) if anos[i] == min(anos)]
        
        meses = [meses[i] for i in indices_anos]
        indices_mes = [i for i in range(len(meses)) if meses[i]==min(meses)]
        dias_mes_min = [dias[i] for i in indices_mes]
        data_de_vencimento = [datas[i] for i in range(len(datas)) if dias[i]==min(dias_mes_min)]
    status(4)
    print("A proxima execucao sera no dia {}".format(data_de_vencimento))
    return data_de_vencimento

def autoexe(data_de_vencimento):
    if date.today().strftime("%d/%m/%Y") == data_de_vencimento:
        data_de_vencimento = find_Due_date(user_file())
        
        if not isfile('renew.txt'):
            run(['schtasks','/create','/tn','Renew Books','/tr','python autoBC.py','/sc', 'ONCE', '/sd',data_de_vencimento,'/st', '08:00','/f']) 
            status(5)
            print("A proxima execucao sera no dia {}".format(data_de_vencimento))
            with open('renew.txt','w') as file:
                file.write(data_de_vencimento)
                file.close()
        else:
            run(['schtasks','/change','/tn','Renew Books','/sd',data_de_vencimento,'/st', '08:00','/f'])
            status(5)
            print("A proxima execucao sera no dia {}".format(data_de_vencimento))
    else:
        print("A proxima execucao sera no dia {}".format(data_de_vencimento)) 

if not isfile('user.txt'):
    print("Não há usuário registrado.\nPreencha com atencao...\n\n")

    user = input("Digite o código de barras: ")
    password = input ("Digite a senha: ")

    file = open ('user.txt','w')
    file.write (user + '\n' + password+'\n')

    file.close()
    
    datas_de_vencimento =  bot (user, password, renew=False, consult=True)
    
    data_de_vencimento = find_Due_date(datas_de_vencimento)
    
elif isfile(r"\renew.txt"):  
    with open('renew.txt','r') as file:
        data_de_vencimento = file.readline()
    file.close()
    autoexe(data_de_vencimento)
    
else:
    autoexe(date.today().strftime("%d/%m/%Y"))
    
input("Pressione qualquer tecla para sair...")