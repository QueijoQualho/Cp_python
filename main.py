from auth.authFunction import *

while True:
    print("====== Menu ====== \n"
          + "1. Cadastro \n"
          + "2. Login \n"
          + "==================")
    opcao = input("Opção: ")

    match opcao:
        case "1":
            cadastro()

