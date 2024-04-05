import re
from models import usuario
from models import roleEnum

def _validaEmail(email: str) -> bool:
    regexEmail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    if email is None:
       return False
    
    if not re.fullmatch(regexEmail, email):
       return False
    
    return True

def _validaSenha(senha: str) -> bool: 
    numeros = len(re.findall(r'\d', senha)) #regex para numeros
    maiusculas = len(re.findall(r'[A-Z]', senha)) #regex para letra minusculas
    minusculas = len(re.findall(r'[a-z]', senha)) #regex para letra maiuscula 
    especiais = len(re.findall(r'[!@#$%&*()\[\]{};,.:/\\|]', senha)) #regex para caracter especial

    n = len(senha) 

    if n < 12:
        return False
    
    if numeros < 2 or maiusculas < 2 or minusculas < 2 or especiais < 2:
        return False
    
    return True

def _validaRole(role: str) -> bool:
    return role in [r.value for r in roleEnum]

def cadastro():
    email = input("Digite o Email: ")
    senha = input("Digite a Senha: ")
    role = input("Digite sua Role: ").upper()
    
    if not _validaEmail(email):
        raise ValueError("Email inválido")
    
    if not _validaSenha(senha):
        raise ValueError("Senha inválida")
    
    if not _validaRole(role):
        raise ValueError("Role Inválida")
    
    return usuario(email, senha, role)
