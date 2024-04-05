from models import roleEnum

class Usuario:
    def __init__(self, email, senha, role):
        self.email = email
        self.senha = senha
        self.role = roleEnum(role)
     
