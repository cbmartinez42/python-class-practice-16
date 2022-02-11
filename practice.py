class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        self.followers = 0
        self.following = 0
        print('new user being created')
    
    def is_star(self):
        self.followers = 1000
    
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'chris')
print(user_1.name)
user_2 = User('002', "joe")
user_2.is_star()
user_1.follow(user_2)
print(
    f"{user_1.name} has followed {user_2.name}. {user_2.name} now has {user_2.followers} and {user_1.name} is following {user_1.following} people")

print(user_2.followers)
