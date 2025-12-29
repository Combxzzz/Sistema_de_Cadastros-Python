import sys
import os
import time


def verificar_arquivos():
    if os.path.exists('Dados.txt'):
        print("Arquivo está presente no diretório principal.")
        time.sleep(1)
        return

    print("Arquivo não foi encontrado no diretório principal!")

    while True:
        opcao = input("Deseja criar um novo?\n[S/N]: ").strip().upper()

        if opcao == "S":
            criar_arquivos()
            return
        elif opcao == "N":
            print("Saindo do programa")
            sys.exit()
        else:
            print("Opção inválida...")


def criar_arquivos():
    try:
        with open('Dados.txt', 'w', encoding='utf-8') as arq:
            arq.write(f"{'Nome':<30}{'Idade':>5}" + "\n"*2)

    except OSError as e:
        print(f"Erro ao criar arquivo: {e.__class__.__name__}")

    except Exception as e:
        print(f"Erro ao criar arquivo: {e.__class__.__name__}")

    else:
        print("Arquivo criado com sucesso")

