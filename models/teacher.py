from models.user import User

class Teacher(User):

    def __init__(self, username):
        super().__init__(username)

    def dashboard(self):
        return "Teacher Dashboard"