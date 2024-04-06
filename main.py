from auth.authFunctions import *
import json


def menu() -> None:
    print(
        "====== Menu ====== \n"
        + "1. Login \n"
        + "2. Cadastrar Usuario \n"
        + "3. Atualizar Dados \n"
        + "4. Mostrar Lista \n"
        + "5. Maior Numero primo \n"
        + "0. Sair \n"
        + "=================="
    )


def mostrar_lista(listaDeUsuarios) -> None:
    print("====== Lista de Usuários ======")
    for usuario in listaDeUsuarios:
        print(f"Email: {usuario.email} | Senha: {usuario.senha} | Role: {usuario.role}")
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
def salvar_dados_usuarios(lista_usuarios):
    with open("dados_usuarios.json", "w") as file:
        json.dump([usuario.__dict__ for usuario in lista_usuarios], file)


def carregar_dados_usuarios():
    try:
        with open("dados_usuarios.json", "r") as file:
            dados = json.load(file)
            return [Usuario(**usuario) for usuario in dados]
    except FileNotFoundError:
        return []


def main():
    userLogado = None
    listUsuarios = carregar_dados_usuarios()
    # ADMIN = ("admin", "162", "ADMIN"))
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

                for user in listUsuarios:
                    if user.email == email and user.senha == senha_hash:
                        userLogado = user
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

            case "0":
                print("Saindo")
                break


if __name__ == "__main__":
    main()
