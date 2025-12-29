import os

def cadastrar():
    if os.path.exists("Dados.txt"):

        while True:
            pessoa = input("Digite o nome da pessoa: ").strip().title()

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

                if idade < 0 or idade > 120:
                    print("Idade inválida!")
                    continue
                break

            except ValueError:
                print("Digite uma idade válida.")

            except Exception as erro:
                print(f"ERRO: {erro.__class__.__name__}")

        try:
            if consultar_usuario(pessoa):
                print("Essa pessoa ja esta na lista!")
                return
            else:
                with open("Dados.txt", "a", encoding="utf-8") as arq:
                    arq.write(f"{pessoa:<30}{idade:>2}" + "\n")

        except FileNotFoundError:
            print("Nao foi possivel encontrar o arquivo 'Dados.txt'")

        except Exception as erro:
            print(f"Nao foi possivel registrar a pessoa\nERRO: {erro.__class__.__name__}")

        else:
            print(f"{pessoa} foi criado com sucesso")

    else:
        print("Nao foi possível encontrar o arquivo 'Dados.txt' no diretorio principal")


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

