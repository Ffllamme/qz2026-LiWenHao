import json
class UserManager:
    def __init__(self):
        self.users = []
        self.max_id=0#创建初始数据库
        def add(self,name,age):
            self.max_id=self.max_id+1
            new_user = {'id':self.max_id,'name':name,'age':age}
            self.users.append(new_user)
            return new_user#导入新用户数据
        def find(self,user_id):
            for user in self.users:
                if user['id'] == user_id:
                    return user#查找用户
        def update(self,user_id,age):
            a = self.get_user(user_id)
            if a :
                a['age']=age
                return True#更新数据
        def delete(self,user_id):
            for user in self.users:
                if user['id'] == user_id:
                    self.users.remove(user)
                    return True#删除
        def list(self):
            return self.users#列出用户
        def to_json(self,filename):
            with open(filename,'w',encoding='utf-8') as f:
                json.dump(self.to_dict(),f,ensure_ascii=False,indent=4)#保存为json文件
        def from_json(self,filename):
            self.users=[]
            with open(filename,'r',encoding='utf-8') as f:
                data = json.load(f)#导入json中的数据
                self.users = data['users']
                self.max_id = data['max_id']#从json文件中加载用户



