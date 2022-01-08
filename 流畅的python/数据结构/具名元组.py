from collections import namedtuple

"""
1、python中的元组tuple元素用index访问
2、nametuple采用intem的index和name访问
"""

User = namedtuple('User',['name', 'sex', 'age'])
#直接创建User对象user
user = User(name='kongxx', sex='male', age=21)
#other method
user2 = User._make(['kongxx','male',21])
#User(name='kongxx', sex='male', age=21) User(name='kongxx', sex='male', age=21)
print(user,user2)

# 获取用户的属性
print(user.name)
print(user.sex)
print(user.age)
# 修改对象属性，注意要使用"_replace"方法
user = user._replace(age=22)
print(user)
# User(name='user1', sex='male', age=21)