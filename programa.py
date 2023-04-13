# App pra armazenar senhas e credenciais.

from funcoes import * # Tradução: De funcoes.py importe *(todas as funções).

# Loop infinito.
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
        input("Aperte \"ENTER\" para voltar ao menu.")
    elif opcao == 2:
        mostrar_senhas()
        input("Aperte \"ENTER\" para voltar ao menu.")
    elif opcao == 3:
        limpar_senhas()
        input("Aperte \"ENTER\" para voltar ao menu.")
    else:
        print("Opção inválida")
        input("Aperte \"ENTER\" para voltar ao menu.")
