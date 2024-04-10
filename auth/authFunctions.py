from models.usuario import Usuario
from models.roleEnum import Role
from pokemon.pokeFunctions import pega_pokemon
import re


# TODO QUESTÃO 1
def _valida_email(email: str) -> bool:

# Compilar a expressão regular para encontrar padrões de endereços de e-mail
    regexEmail = re.compile(
        r"([A-Za-z0-9]+[.-_])*"   # Nome de usuário: letras, números, ponto, hífen ou sublinhado, repetidos zero ou mais vezes
        r"[A-Za-z0-9]+"           # Nome de usuário: letras maiúsculas ou minúsculas ou dígitos de 0 a 9
        r"@"                      # Separador entre nome de usuário e domínio
        r"[A-Za-z0-9-]+"          # Domínio: letras maiúsculas ou minúsculas, dígitos de 0 a 9 ou hífen
        r"(\.[A-Z|a-z]{2,})+"     # TLD (domínio de nível superior): letras maiúsculas ou minúsculas, pelo menos duas
    )


    if email is None:
        return False

    if not re.fullmatch(regexEmail, email):
        return False

    return True


def _valida_senha(senha: str) -> bool:

    n = len(senha)

    if n < 12:
        return False

    numeros = len(re.findall(r"\d", senha))  # regex para numeros
    maiusculas = len(re.findall(r"[A-Z]", senha))  # regex para letra minusculas
    minusculas = len(re.findall(r"[a-z]", senha))  # regex para letra maiuscula
    especiais = len(
        re.findall(r"[!@#$%&*()\[\]{};,.:/\\|]", senha)
    )  # regex para caracter especial

    if numeros < 2 or maiusculas < 2 or minusculas < 2 or especiais < 2:
        return False

    return True


def _valida_role(role: str) -> bool:
    return role.upper() in Role.__members__


# TODO QUESTÃO 2
def cadastro() -> Usuario:
    try:
        email = input("Digite o Email: ")
        senha = input("Digite a Senha: ")
        role = input("Digite sua Role: ").upper()

        if not _valida_email(email):
            raise ValueError("Email inválido")

        if not _valida_senha(senha):
            raise ValueError("Senha inválida")

        if not _valida_role(role):
            raise ValueError("Role Inválida")

        senha = hash(senha)

        id_user = hash(email + senha)
        
        pokemon = pega_pokemon(id_user)

        return Usuario(id_user, email, senha, role, pokemon)
    except ValueError as ve:
        print(f"Erro durante o cadastro: {ve}")


# TODO QUESTÃO 3
def atualizar_dados(userLogado: Usuario, listaDeUsuarios: list[Usuario]) -> None:

    try:
        if userLogado == None:
            raise Exception("O usuário não está logado!")
        
        if userLogado.role == "USER":
            senha = input("Digite sua nova Senha: ")

            if not _valida_senha(senha):
                raise ValueError("Senha inválida")

            userLogado.senha = hash(senha)
            print("Usuario Atualizado com Sucesso!")

        else:  # ADMIN
            email = input("Digite o email do Usuario: ")

            usuario = next(
                (user for user in listaDeUsuarios if user.email == email), None
            )

            if usuario is None:
                raise Exception("Nenhum usuário encontrado.")

            if usuario.role == "ADMIN":
                raise Exception("O usuário encontrado é um administrador.")

            senha = input("Digite a Nova Senha: ")

            if not _valida_senha(senha):
                raise ValueError("Senha inválida")

            usuario.senha = senha
            print("Senha do usuário atualizada com sucesso!")

    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)


# TODO QUESTÃO 4
def maior_num_primo(n: int) -> int:
    if n < 2:
        return
    for num in reversed(range(1, n + 1)):
        if all(num % i != 0 for i in range(2, num)):
            return num


# TODO Questão 5
def hash(senha: str) -> str:
    senha_ord = ""
    for char in senha:
        senha_ord += str(ord(char))

    senha_ord = int(senha_ord)
    numPrimo = maior_num_primo(1025)

    return str(senha_ord % numPrimo)


# TODO Questão 9
def pegar_por_id(listaDeUsuarios: list[Usuario]) -> Usuario:
    id_usuario = input("Qual o id do usuario: ")
    for user in listaDeUsuarios:
        if user.id == id_usuario:
            return user
    else:
        return None
