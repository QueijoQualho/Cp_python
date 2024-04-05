from models.enums import roleUsuario

class Usuario:
    def __init__(self, email, senha, role):
        self.email = email
        self.senha = senha
        if isinstance(role, roleUsuario): 
            self.role = role
        else:
            raise ValueError("Role inválido")
