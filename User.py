class User(object):
    def __init__(self,userName,password):
        self.userName = userName
        self.password = password
        self.isLogon = False

    def __str__(self):
        return f"{self.userName} login: {self.isLogon}"