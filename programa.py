from funcoes import *

while True:
    limpar_tela()
    print("Seja bem-vindo ao Guardador de Senhas!")
    print("1- Guardar nova senha")
    print("2- Mostrar todas as senhas")
    print("3- Apagar senhas")

    opcao = int(input("Escolha a opção: "))
    limpar_tela()
    if opcao == 1:
        salvar_senha()
    elif opcao == 2:
        mostrar_senhas()
        input()
    elif opcao == 3:
        limpar_senhas()
    else:
        print("Opção inválida")
