from auth.authFunction import *

userLogado = None
listUsuarios = [Usuario("admin", "admin123", "ADMIN")]

def menu():
     print("====== Menu ====== \n"
          + "1. Cadastrar Usuario \n"
          + "2. Login \n"
          + "==================")
     
def validaUsuario():
    if userLogado is None:
        raise Exception('O usuário não está logado!')
    if userLogado.role  != 'ADMIN':
        raise Exception('Você precisa ser um administrador para acessar essa função!')

while True:
    menu()
    opcao = input("Opção: ")

    match opcao:
        case "1":
            try:
                validaUsuario()
                novo_usuario = cadastro()
                listUsuarios.append(novo_usuario)
            except ValueError as ve:
                print(ve)
                break
            except Exception as e:
                print(e)
                break
          
        case "2":
            email = input("Email: ")
            senha = input("Senha: ")

            for user in listUsuarios:
                if user.email == email and user.senha == senha:
                    userLogado = user

            if userLogado is None or userLogado.role != "ADMIN":
                print("\nUsuário ou Senha Inválido!")

            

