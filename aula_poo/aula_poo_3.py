# setter

class Conection:
    def __init__(self, host='localhost', ):
        self.host = host
        self.user = None
        self.password = None

    def set_user (self, user):
        self.user = user

    def set_password (self, password):
        self.password = password
    
    @classmethod
    def create_whit_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    


c1 = Conection.create_whit_auth('vitor', '321')
print(c1.user, c1.password)