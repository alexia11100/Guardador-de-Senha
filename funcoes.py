import os
import base64

# Função pra limpar a tela do terminal.
def limpar_tela():
    os.system("cls")

def criptografar(texto):
    return base64.b64encode(texto.encode()).decode()

def descriptografar(texto):
    return base64.b64decode(texto).decode()

# Função pra apagar as senhas do arquivo Senhas.txt.
def limpar_senhas():
    arquivo = open("Senhas.txt", "w", encoding="utf-8")
    arquivo.write("")
    arquivo.close()
    print("Arquivo de senha vazio.")

# Função pra adicionar novas senhas (email, app e nova senha).
def salvar_senha():
    app = input("Que app vc deseja cadrastar a senha? ").title()
    email_do_app = input("Qual o email dessa conta? ")
    nova_senha = input("Informe a senha: ")
    limpar_tela()

    print("Aplicativo:",app)
    print("Email:",email_do_app)
    print("Senha:",nova_senha + "\n")
    confirmacao = input("Confirme seus dados com \"S\" ou \"N\": ")
    limpar_tela()

    if confirmacao == "S":
        try:
            arquivo = open("Senhas.txt", "r", encoding="utf-8")
        except FileNotFoundError:
            limpar_senhas()
            arquivo = open("Senhas.txt", "r", encoding="utf-8")
        conteudo = descriptografar(arquivo.read())+f"{app}|{email_do_app}|{nova_senha}\n"
        arquivo.close()

        arquivo = open("Senhas.txt", "w", encoding="utf-8")
        arquivo.write(criptografar(conteudo))
        arquivo.close()

        print("Senha adicionada com sucesso!\n")
        registrar_nova = input("Digite \"S\" para registrar outra senha ou \"N\" para voltar ao menu: ")
        limpar_tela()
        if registrar_nova == "S":
            return salvar_senha()
        
    else:
        print("Ok, senha não adicionada.")

# Função pra mostrar todas as senhas ja registradas no app.
def mostrar_senhas():
    arquivo = open("Senhas.txt", "r", encoding="utf-8")
    conteudo = descriptografar(arquivo.read())
    arquivo.close()
    conteudo = conteudo.split("\n")[:-1]
    
    print("Credenciais cadastradas:\n")

    for senha in conteudo:
        credenciais = senha.split("|")
    
        print(f"Aplicativo: {credenciais[0]}")
        print(f"Email: {credenciais[1]}")
        print(f"Senha: {credenciais[2]}\n")

def mostrar_senha_app():
    arquivo = open("Senhas.txt", "r", encoding="utf-8")
    conteudo = descriptografar(arquivo.read())
    arquivo.close()
    conteudo = conteudo.split("\n")[:-1]
    
    credenciais = []
    apps = set()
    for senha in conteudo:
        credencial = senha.split("|")
        credenciais.append(credencial)
        apps.add(credencial[0])
    apps = list(apps)
    
    for posicao in range(1,len(apps)+1):
        print(posicao,"-",apps[posicao-1])

    opcao = int(input("Escolha o app que deseja ver as senhas: "))
    limpar_tela()
    print("Credenciais cadastradas para o app "+credencial[0]+":\n")
    for credencial in credenciais:
        if credencial[0] == apps[opcao-1]:
            print("Email: ",credencial[1])
            print("Senha: ",credencial[2]+"\n")