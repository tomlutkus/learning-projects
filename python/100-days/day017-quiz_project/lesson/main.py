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
        self.following = 0
    
    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}, Followers: {self.followers}, Following: {self.following}"

class UserList:
    def __init__(self):
        self.user_list = []
        self.fill_user_list(USERS)
    
    def fill_user_list(self, users) -> None:
        for user_id, username in users.items():
            user = User(user_id, username)
            self.user_list.append(user)
    
    def get_user(self, user_name) -> str | None:
        matching_users = []
        for user in self.user_list:
            if user_name.lower() in user.username.lower():
                matching_users.append(user)
        return matching_users if matching_users else None


user_db = UserList()

search_string = input("Type username to be found: ")
matching_users = user_db.get_user(search_string)

for line in matching_users:
    print(line)

# for user in user_db.user_list:
#     print(user.username)



# user_1 = User("001", "thomas")
# user_2 = User("002", "angela")

# print(f"ID: {user_1.id}\nUser: {user_1.username}")


