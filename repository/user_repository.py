from models.user_models import User

class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_user_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def get_all_users(self) -> list:
        return self.users
    
    def delete_user(self, user_id: int) -> bool:
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return True
        return False
    
    def update_user(self, user_id: int, updated_user: User) -> bool:
        for index, user in enumerate(self.users):
            if user.id == user_id:
                self.users[index] = updated_user
                return True
        return False