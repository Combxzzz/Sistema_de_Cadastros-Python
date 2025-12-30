import os

import Interface


def cadastrar():
    if os.path.exists("Dados.txt"):

        while True:
            opcao = input("Tem certeza que deseja adicionar um novo usuário?\n[S/N]: ").strip().upper()

            if opcao == "S":
                break

            elif opcao == "N":
                return

            else:
                print("Digite uma opção válida")
                continue

        while True:
            pessoa = input("Digite o nome do usuário: ").strip().title()

            if not pessoa:
                print("Nome não pode ser vazio.")
                continue

            if not pessoa.replace(" ", "").isalpha():
                print("Digite um nome válido.")
                continue

            break

        while True:
            try:
                idade = int(input("Digite a idade: "))

                if idade < 1 or idade > 99:
                    print("Idade inválida!")
                    continue
                break

            except ValueError:
                print("Digite uma idade válida.")

            except Exception as erro:
                print(f"ERRO: {erro.__class__.__name__}")

        try:
            if consultar_usuario(pessoa):
                print("Esse usuário já está na lista!")
                return

            else:
                with open("Dados.txt", "a", encoding="utf-8") as arq:
                    arq.write(f"{pessoa:<40}{idade:>2}" + "\n")

        except FileNotFoundError:
            print("Não foi possível encontrar o arquivo 'Dados.txt'")

        except Exception as erro:
            print(f"Não foi possível registrar o usuário.\nERRO: {erro.__class__.__name__}")

        else:
            print(f"{pessoa} foi criado com sucesso!")

    else:
        print("Não foi possível encontrar o arquivo 'Dados.txt' no diretório principal.")


def consultar_usuario(entidade):
    with open("Dados.txt", "r", encoding="utf-8") as arq:
        for linha in arq:
            nome = linha[:30].strip()
            if nome == entidade:
                return True
    return False


def listar():
    try:
        with open("Dados.txt", "r", encoding="utf-8") as arq:
            print(arq.read())

    except FileNotFoundError:
        print("Arquivo nao encontrado!")

    except Exception as erro:
        print(f"ERRO: {erro.__class__.__name__}")

