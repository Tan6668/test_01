
#---------------------------------------示例1-------------------------------
# class Dog:
#     '''这是类的文档字符串
#     描述狗的行为和属性
#     '''
#     pass

# dog1 = Dog() #用Dog 
# print(id(dog1))
# dog2 = Dog()
# print(id(dog2))

#*********************示例语法***************

# class Dog:
#     '''这是类的文档字符串
#     描述狗的行为和属性
#     '''
#     def eat(self, food):
#         print("小狗正在吃",food)
    
#     def sleep(self, hour):
#         print("小狗睡了", hour, '小时')

#     def play(self, obj):
#         print("小狗玩了", obj)

# dog1 = Dog() #用Dog 
# dog1.eat("骨头")
# dog1.sleep(1)
# dog1.play("球")

# dog2 = Dog()
# dog2.eat("狗粮")
# dog2.play("飞盘")
# dog2.sleep(3)

#*********************************实例属性-********************
# class Dog:
#     def eat(self, food):
#         print(self.color, self.kinds,"小狗正在吃", food)
#         self.last_food = food
#     def food_info(self):
#         print(self.color, self.kinds, '上次吃的是', self.last_food)

# dog1 = Dog()
# dog1.color = '白色'
# dog1.kinds = '京巴'
# #print(dog1.color, '的', dog1.kinds)
# dog1.eat('骨头')


# dog2 = Dog()
# dog2.color = '灰色'
# dog2.kinds = '哈士奇'
# dog2.eat('狗粮')

# dog1.food_info()
# dog2.food_info()

# class Human:
#     def set_info(self, name, age, address='不详'):
#         print(self.name, self.age, self.address)
#         name = self.name
#         age = self.age
#         address = self.address

#     def show_info(self):
#         print(self.name, '今年', self.age, '岁', '家庭住址:', self.address)

# h1 = Human()
# h1.set_info('小张', 20, '北京市朝阳区')
# h2 = Human()
# h2.set_info('小李', 18)
# h1.show_info()
# h2.show_info()      

# class Car:
#     '''定义汽车类'''

#     def __init__(self, c, b, m):
#         self.color = c
#         self.brand = b
#         self.model = m

#     def run(self, speed):
#         print(self.color, '的', self.brand, self.model, '正在以', speed, '速度行驶')

# a4 = Car('红色', '奥迪', 'A4')
# a4.run(199)

# t1 =Car('蓝色', '野马', '4')
# t1.run(220)

# Car('红色', '奥迪', 'A4').run(220)


# class Student():
#     def __init__(self, n, a, c='0'):
#         self.name = n
#         self.age = a
#         self.chengji = c

#     def set_score(self, c):
#         self.chengji = c

#     def show_info(self):
#         print(self.name, self.age, self.chengji)

# L = []
# L.append(Student('小张', 20, 100))
# L.append(Student('小李', 18, 98))
# L.append(Student('小王', 19))
# L[2].set_score(80)
# for s in L:
#     s.show_info()

class Car:
    def __init__(self, info):
        self.info = info
        print("汽车", info, '对象被创建！')
    def __del__(self):
        print("汽车", self.info, '对象被销毁')

c1 = Car("BYD E6")
input()