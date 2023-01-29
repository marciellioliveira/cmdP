#Modulos
import xml.etree.ElementTree as et #Implementa uma API para analisar dados XML
from os.path import exists
import os

clear = lambda: os.system('cls')


#Funçõe dos modulos
def generateXML(file_name, novo_usuario, nova_senha):
    root = et.Element("usuarios")

    usuario = et.Element("usuario")
    root.append(usuario)

    nome = et.SubElement(usuario, "login")
    nome.set('name', 'login')
    nome.text = novo_usuario
    senha = et.SubElement(usuario, "senha")
    senha.set('name', 'senha')
    senha.text = nova_senha

    tree = et.ElementTree(root)
    with open (file_name, 'wb') as files:
        tree.write(files)

tree = et.parse('telas/telas.xml')
root = tree.getroot()

file_existe = exists('cadastros/usuarios.xml')
if file_existe:
    treeUsuario = et.parse('cadastros/usuarios.xml')
    rootUsuario = treeUsuario.getroot()

def escolha():
    for element in root.findall("./tela[@name='escolha']/"):
        print(element.text)
        cmd_digitado = input("Digite um comando: ")
        # print(f"CMD Digitado: {cmd_digitado}")        
        
        for tela in root.findall('tela'):
            nome_tela = tela.get('name')
            # print(nome_tela)
            
            if cmd_digitado == nome_tela:
                if cmd_digitado == 'entrar':
                    clear()
                    entrar()
                elif cmd_digitado == 'cadastrar':
                    clear()
                    cadastrar()
                elif cmd_digitado == 'alterar':
                    clear()
                    alterar()
                elif cmd_digitado == 'sair':
                    clear()
                    sair()
                elif cmd_digitado == 'ajuda':
                    clear()
                    ajuda()
                    escolha()
                
def telas():
    for element in root.findall("./tela[@name='telas']/"):
        print(element.text)

        res = input("Digite um comando para aprender: ")

        for tela in root.findall('tela'):
            nome_tela = tela.get('name')
            # print(type(nome_tela))

            if res == nome_tela:
                if nome_tela == 'about_python':
                    clear()
                    about_python()
                    break
                elif nome_tela == 'syntax':
                    clear()
                    syntax()
                    break
                elif nome_tela == 'comment':
                    clear()
                    comment()
                    break
                elif nome_tela == 'variables':
                    clear()
                    variables()
                    break
                elif nome_tela == 'data_types':
                    clear()
                    data_types()
                    break
                elif nome_tela == 'numbers':
                    clear()
                    numbers()
                    break
                elif nome_tela == 'casting':
                    clear()
                    casting()
                    break
                elif nome_tela == 'strings':
                    clear()
                    strings()
                    break
                elif nome_tela == 'booleans':
                    clear()
                    booleans()
                    break
                elif nome_tela == 'operators':
                    clear()
                    operators()
                    break
        break   
    telas()            
         
#Funções Complementares
def bemvindo():
    print("Bem Vindo!")
    telas()
    # for element in root.findall("./tela[@name='bemvindo']/"):
    # print(element.text)
        
def cadastrar():
    for element in root.findall("./tela[@name='cadastrar']/"):
        print(element.text)
        usuario = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")
        generateXML('./cadastros/usuarios.xml', usuario, senha)
        print("Usuário cadastrado com sucesso!")
        break
    escolha()


def entrar():  
    for element in root.findall("./tela[@name='entrar']/"):
        print(element.text)
        usuario_entrada = input("Qual o seu usuário? ")
        senha_entrada = input("Qual a sua senha? ")               
    
        for login in rootUsuario.findall('usuario/login'):
            for senha in rootUsuario.findall('usuario/senha'):
                
                if usuario_entrada == login.text and senha_entrada == senha.text:
                    bemvindo()
                else:
                    print('Usuario ou senha invalidos')
                    # tentar_novamente = input("Tentar novamente? S - SIM | N - NÃO: ") 

                    # if tentar_novamente.lower == 's':
                    #     escolha()
                    #     break
                    # else:
                    #     exit() 
                    #     break                         
        break
    

def alterar():
    for element in root.findall("./tela[@name='alterar']/"):
        print(element.text)
        usuario = input("Qual o seu novo usuário? ")
        senha = input("Qual a sua nova senha? ")
        generateXML('./cadastros/usuarios.xml', usuario, senha)
        print("Usuário alterado com sucesso!")
        print(f"Seu novo usuário é: {usuario}\nSua nova senha é: {senha}")
        break
    escolha()


def sair():
    for element in root.findall("./tela[@name='sair']/"):
        print(element.text)
        break        
    exit()

def ajuda():
     for element in root.findall("./tela[@name='ajuda']/"):
        print(element.text) 
        break  

def erro():
    for element in root.findall("./tela[@name='erro']/"):
        print(element.text)
        break

#Sobre Python
def about_python():
    for element in root.findall("./tela[@name='about_python']/"):
        print(element.text)
        break

#Sobre syntax
def syntax():
    for element in root.findall("./tela[@name='syntax']/"):
        print(element.text)
        break

#Sobre comment
def comment():
    for element in root.findall("./tela[@name='comment']/"):
        print(element.text)
        break

#Sobre variables
def variables():
    for element in root.findall("./tela[@name='variables']/"):
        print(element.text)
        break

#Sobre data_types
def data_types():
    for element in root.findall("./tela[@name='data_types']/"):
        print(element.text)
        break

#Sobre numbers
def numbers():
    for element in root.findall("./tela[@name='numbers']/"):
        print(element.text)
        break

#Sobre casting
def casting():
    for element in root.findall("./tela[@name='casting']/"):
        print(element.text)
        break

#Sobre strings
def strings():
    for element in root.findall("./tela[@name='strings']/"):
        print(element.text)
        break

#Sobre booleans
def booleans():
    for element in root.findall("./tela[@name='booleans']/"):
        print(element.text)
        break

#Sobre operators
def operators():
    for element in root.findall("./tela[@name='operators']/"):
        print(element.text)
        break

#Tela Inicial
def inicio():
    clear()
    escolha()   

inicio()



