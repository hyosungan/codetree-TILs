user2_id, user2_level = input().split()
user2_level = int(user2_level)

class Id_User:
    def __init__(self,id='codetree',level=10):
        self.id=id
        self.level=level

user1=Id_User()
user2=Id_User(user2_id,user2_level)

print("user",user1.id,'lv',user1.level)
print("user",user2.id,'lv',user2.level)


