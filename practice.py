class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name
        print('new user being created')
    
    
user_1 = User('001', 'chris')
# user_1.id = '001'
# user_1.name = "chris"

print(user_1.name)

user_2 = User('002', "joe")
# user_2.id = '002'
# user_2.name = "joe"

print(user_2.name)