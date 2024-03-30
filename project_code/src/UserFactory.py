# UserFactory.py
from project_code.src.UserInputParser import UserInputParser
from project_code.src.User import User
class UserFactory:
    @staticmethod
    def create_user(parser: UserInputParser) -> User:
        while True:
            username = parser.parse("Enter a username: ")
            if not username:
                print("Username cannot be empty. Please try again.")
                continue

            password = parser.parse("Enter a password: ")
            if len(password) < 8 or not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
                print("Password must be at least 8 characters long and contain both numbers and letters. Please try again.")
                continue

            return User(username, password)