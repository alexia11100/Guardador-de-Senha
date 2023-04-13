import os

# Função pra limpar a tela do terminal.
def limpar_tela():
    os.system("cls")

# Função pra apagar as senhas do arquivo Senhas.txt.
def limpar_senhas():
    arquivo = open("Senhas.txt", "w")
    arquivo.write("")
    print("Arquivo de senha vazio.")

# Função pra adicionar novas senhas (email, app e nova senha).
def salvar_senha():
    app = input("Que app vc deseja cadrastar a senha? ")
    email_do_app = input("Qual o email dessa conta? ")
    nova_senha = input("Informe a senha: ")
    limpar_tela()

    print("Aplicativo:",app)
    print("Email:",email_do_app)
    print("Senha:",nova_senha + "\n")
    confirmacao = input("Confirme seus dados com \"S\" ou \"N\": ")
    limpar_tela()

    if confirmacao == "S":
        arquivo = open("Senhas.txt", "a")
        arquivo.write(f"{app}|{email_do_app}|{nova_senha}\n")
        
        print("Senha adicionada com sucesso!\n")
        registrar_nova = input("Digite \"S\" para registrar outra senha ou \"N\" para voltar ao menu: ")
        
        if registrar_nova == "S":
            limpar_tela()
            return salvar_senha()
        
    else:
        print("Ok, senha não adicionada.")

# Função pra mostrar todas as senhas ja registradas no app.
def mostrar_senhas():
    arquivo = open("Senhas.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)