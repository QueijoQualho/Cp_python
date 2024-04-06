from auth.authFunctions import *
from pokemon.pokeFunctions import pega_pokemon
from pprint import pprint
import json

def menu() -> None:
    print(
        "====== Menu ====== \n"
        + "1. Login \n"
        + "2. Cadastrar Usuario \n"
        + "3. Atualizar Dados \n"
        + "4. Mostrar Lista \n"
        + "5. Maior Numero primo \n"
        + "6. Pegar Usuario Pro id \n"
        + "0. Sair \n"
        + "=================="
    )


def mostrar_lista(listaDeUsuarios) -> None:
    print("====== Lista de Usuários ======")
    pprint([usuario.__dict__ for usuario in listaDeUsuarios])  # Usando pprint aqui
    print("==============================")


def valida_usuario_acesso(userLogado: Usuario) -> bool:
    try:
        if userLogado is None:
            raise Exception("O usuário não está logado!")
        if userLogado.role != "ADMIN":
            raise Exception(
                "Você precisa ser um administrador para acessar essa função!"
            )
    except Exception as e:
        print(e)
    else:
        return True


# TODO Questao 7
def salvar_dados_usuarios(lista_usuarios) -> None:
    with open("dados_usuarios.json", "w") as file:
        # TODO Questao 10
        json.dump([usuario.__dict__ for usuario in lista_usuarios], file)


def carregar_dados_usuarios() -> list:
    try:
        with open("dados_usuarios.json", "r") as file:
            dados = json.load(file)
            return [Usuario(**usuario) for usuario in dados]
    except FileNotFoundError:
        return []

def main():
    userLogado = None
    listUsuarios = carregar_dados_usuarios()
    # ADMIN = Usuario("admin", "162", "ADMIN"))
    # Senha = ASDasd123!@#

    while True:
        menu()
        opcao = input("Opção: ")

        match opcao:
            case "1":
                email = input("Email: ")
                senha = input("Senha: ")

                # TODO Questão 6
                senha_hash = hash(senha)

                for usuario in listUsuarios:
                    if usuario.email == email and usuario.senha == senha_hash:
                        userLogado = usuario
                        break
                else:
                    print("Senha ou Email inválidos")

            case "2":
                if valida_usuario_acesso(userLogado):
                    novo_usuario = cadastro()
                    listUsuarios.append(novo_usuario)
                    salvar_dados_usuarios(listUsuarios)

            case "3":
                atualizar_dados(userLogado, listUsuarios)
            case "4":
                mostrar_lista(listUsuarios)
            case "5":
                n = input("Digite um numero: ")

                if n != None and n.isdigit():
                    print(f"O maior numero primo é {n}")
                else:
                    print("Valor inválido")
            case "6":
                usuario = pegar_por_id(listUsuarios)

                if usuario:
                    pprint(usuario.__dict__)
                else:
                    print("Usuário não encontrado.")

            case "0":
                print("Saindo")
                break


if __name__ == "__main__":
    main()
