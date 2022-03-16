from subprocess import run
from platform import system
from sys import modules
from time  import sleep
from os.path import isdir, isfile, realpath, dirname

#request(plataform)  <-------------------------------------------
plataform = system()
dir = dirname(realpath(__file__))
print('Sistema identificado: {}'.format(plataform))

def requests():
    if 'selenium' not in modules:
<<<<<<< HEAD
=======
        
>>>>>>> 2ad84be52ba669447bdd0d881fe9ea3be0e38268
        print("Dependência não encontrada: Selenium")
        print("Instalando Selenium ...")
        run(['python3','-m','pip','install','selenium'])
        
    if 'webdriver_manager' not in modules:
        print("Dependência não encontrada: Webdriver Manager")
        print("Instalando Webdriver Manager ...")
        
        run(['python3','-m','pip','install','webdriver_manager'])

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
            input("Instale o Chrome, há um instalador na pasta 'chromesetup', realize a instalação e me execute novamente.")
            exit()
            
def bot(username, password, renew =True, consult = False):
    #Drive de automação do navegador
    from selenium import webdriver
<<<<<<< HEAD
    from selenium.webdriver.chrome.service import Service
=======
>>>>>>> 2ad84be52ba669447bdd0d881fe9ea3be0e38268
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.chrome import ChromeDriverManager
    ###############################################
<<<<<<< HEAD
    
    browser = webdriver.Chrome (service=Service(ChromeDriverManager().install()))
=======
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    browser = webdriver.Chrome (ChromeDriverManager().install(), options= options)
>>>>>>> 2ad84be52ba669447bdd0d881fe9ea3be0e38268
    browser.get("http://virtua.uel.br:8080/auth/login?")
    
    browser.find_element(By.NAME,"username").send_keys(username)
    browser.find_element(By.NAME,"password").send_keys(password + Keys.RETURN)
    
    if renew:
        browser.find_element(By.NAME,"button.selectAll").click()
        browser.find_element(By.ID,"button.renew").click()
        
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
    return datas_de_vencimento

def user_file():
    if isfile('user.txt'):

        file = open ('user.txt','r')

        user = file.readline()
        user = user[:-1]

        password = file.readline()
        password = password
        file.close()

<<<<<<< HEAD
    return bot (user, password, renew=True, consult=True)
=======
        bot (user, password, renew=False, consult=True)
>>>>>>> 2ad84be52ba669447bdd0d881fe9ea3be0e38268

def find_Due_date(datas):
    anos = [int(data[6:]) for data in datas]
    meses =  [int(data[3:5]) for data in datas]
    dias = [int(data[:2]) for data in datas]
<<<<<<< HEAD

=======
    print(anos, meses,dias)
>>>>>>> 2ad84be52ba669447bdd0d881fe9ea3be0e38268
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
        
<<<<<<< HEAD
    with open('renew.txt','w') as file:
            file.write(data_de_vencimento)
            file.close()
        
=======
>>>>>>> 2ad84be52ba669447bdd0d881fe9ea3be0e38268
    return data_de_vencimento

def autoexe(data_de_vencimento):
    from datetime import date
    if date.today().strftime("%d/%m/%Y") == data_de_vencimento:
        data_de_vencimento == find_Due_date(user_file())
        with open('renew.txt','w') as file:
            file.write(data_de_vencimento)
            file.close()
    else:
        print("A proxima execucao sera no dia {}".format(data_de_vencimento))

if isfile(dir+'\\renew.txt'):
    
    with open('renew.txt','r') as file:
        data_de_vencimento = file.readline()
    file.close()
    
    autoexe(data_de_vencimento)
<<<<<<< HEAD
else:
    autoexe(find_Due_date(user_file()))
           
'''
=======


        
>>>>>>> 2ad84be52ba669447bdd0d881fe9ea3be0e38268
if not isfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\\autoBC.py") and plataform == 'Windows':
    Inicializar = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
    from shutil import copyfile
    copyfile(dir +'\\autoBC.py',Inicializar)
    copyfile(dir +'\\user.txt',Inicializar)
    copyfile(dir + '\\renew.txt',Inicializar)
<<<<<<< HEAD
''' 
=======
    
input()  
>>>>>>> 2ad84be52ba669447bdd0d881fe9ea3be0e38268
