class User(object):
    def __init__(self,user_name,password):
        self.userName = user_name
        self.password = password
        self.isLogon = False

    def __str__(self):
        return f"{self.user_name} login: {self.isLogon}"
