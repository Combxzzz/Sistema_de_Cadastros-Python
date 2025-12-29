from colorama import init, Fore, Style
import os
import sys
import Servicos
import Seguranca

init()

def menu():
    while True:
        print(Fore.GREEN + "-" * 30)
        print("MENU PRINCIPAL")
        print("-" * 30 + Style.RESET_ALL)
        print("1 - Verificar arquivo")
        print("2 - Criar usuário")
        print("3 - Listar usuários")
        print("4 - Limpar terminal")
        print("5 - Sair")

        try:
            opcao = int(input("Opção: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 1:
            Seguranca.verificar_arquivos()

        elif opcao == 2:
            Servicos.cadastrar()

        elif opcao == 3:
            print("-" * 40)
            Servicos.listar()
            print("-" * 40)

        elif opcao == 4:
            limpar_terminal()

        elif opcao == 5:
            print("Saindo do programa")
            sys.exit()

        else:
            print("Opção inválida.")


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

