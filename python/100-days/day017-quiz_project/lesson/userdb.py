"""
userdb.py - Practicing some OOP in Python
Author: Thomas Lutkus
"""

USERS = {
    "001": "thomas",
    "002": "angela",
    "003": "ana",
    "004": "plick",
    "005": "fred",
    "006": "hendrik",
    "007": "jessica",
    "008": "anastasia"
}


class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

class UserList:
    def __init__(self):
        self.user_list = []
        self.fill_user_list(USERS)
    
    def fill_user_list(self, users) -> None:
        for user_id, username in users.items():
            user_id = User(user_id, username)
            self.user_list.append(user_id)
    
    def get_user(self, user_name) -> str | None:
        matching_users = None
        for user in self.user_list:
            if user_name in user.username:
                user_string = f"ID: {user.id}, Username: {user.username}"
                if not matching_users:
                    matching_users = [user_string]
                else:
                    matching_users.append(user_string)
        return matching_users


user_db = UserList()

search_string = input("Type username to be found: ")
matching_users = user_db.get_user(search_string)

for line in matching_users:
    print(line)

