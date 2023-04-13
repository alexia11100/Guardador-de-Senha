import os

def limpar_tela():
    os.system("cls")


def limpar_senhas():
    arquivo = open("Senhas.txt", "w")
    arquivo.write("")


def salvar_senha():
    app = input("Que app vc deseja cadrastar a senha? ")
    email_do_app = input("Qual o email dessa conta? ")
    nova_senha = input("Informe a senha: ")
    print(app, email_do_app, nova_senha)
    confirmacao = input("Confirme seus dados com \"S\" ou \"N\": ")
    if confirmacao == "S":
        arquivo = open("Senhas.txt", "a")
        arquivo.write(f"{app}|{email_do_app}|{nova_senha}\n")
        print("Senha adicionada com sucesso!")
    else:
        print("Ok, senha não adicionada.")


def mostrar_senhas():
    arquivo = open("Senhas.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)