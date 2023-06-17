from .role import Role
class User:
    
    def __init__(self, username:str, role:Role, company:str=None):
        self.username = username
        self.company = company
        self.role = role

