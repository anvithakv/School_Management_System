from models.user import User

class Admin(User):

    def __init__(self, username):
        super().__init__(username)

    def dashboard(self):
        return "Admin Dashboard"