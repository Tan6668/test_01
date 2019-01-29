
# class Human:
#     '''此示例示意类属性'''
#     count = 0

# print(Human.count)
# Human.count = 100
# print(Human.count) 

# class Human:
#     '''此示例示意类属性'''
#     count = 0

# h1 = Human()
# print(h1.count)
# h1.count = 100
# print(h1.count)
# print(Human.count)


# class Human:
#     '''此示例示意类属性'''
#     count = 0

# print(Human.count)
# h1 = Human()
# h1.__class__.count = 100
# print(Human.count)



# class Human:
#     '''此示例示意类属性'''
#     count = 0
#     def __init__(self, name):
#         print(name, '对象被创建')
#         self.name = name
#         self.__class__.count += 1
#     def __del__(self):
#         print(self.name, '对象被销毁')
#         self.__class__.count -= 1
# L = [Human('孙悟空'), Human('猪八戒')]
# h1 = Human('沙僧')
# print(Human.count)
# del L
# print(Human.count)

# class Human:
#     __slots__ = ['age']
#     def __init__(self, age):
#         self.age = age
#     def show_info(self):
#         print('年龄是：', self.age)

# h1 = Human(10)
# h1.show_info()
# h1.Age = 11
# h1.show_info()

#此示例示意用类方法来访问类变量和改变类变量
# class A:
#     v = 0
#     @classmethod
#     def get_v(cls):
#         return cls.v
#     @classmethod
#     def set_v(cls,v):
#         cls.v = v
# print(A.v)
# print(A.get_v())

# A.set_v(80)
# print(A.get_v())
# print(A.v)

# 
# class Human:
#     '''定义人类的基类'''
#     def say(self, what):
#         print("说：", what)
#     def walk(self, distance):
#         print("走了：", distance, '公里')

# class Student(Human):
#     def study(self, subject):
#         print("学习：", subject)

# class Teacher(Human):
#     def teach(self, subject):
#         print("教：", subject)


# h1 = Human()
# h1.say('天气冷了')
# h1.walk(5)
# print("---------------以下是学生－－－－－－－")
# s1 = Student()
# s1.say("吃放去")
# s1.study("面向对象")
# print("------------------老师---------------------")
# s2 = Teacher()
# s2.teach("基类")
# s2.walk(5)




# class Mylist(list):
#     def insert_head(self, n):
#         self.insert(0, n)


# myl = Mylist(range(3, 6))
# print(myl)
# myl.insert_head(2)
# print(myl)
# myl.append(6)
# print(myl)

#----------------------覆盖
# class A:
#     def work(self):
#         print("A被调用")

# class B(A):
#     def work(self):
#         print("B被调用")

# b = B()
# b.work()
# A.work(b)

#------------------super
# class A:
#     def work(self):
#         print("A被调用")

# class B(A):
#     def work(self):
#         print("B被调用")
    
#     def do_something(self):
#         self.work()
#         #super(B, self).work()
#         super().work()

# b = B()
# b.do_something()


# class Human:
#     def __init__(self, n, a):
#         self.name = n
#         self.age = a
#     def show_info(self):
#         print("姓名", self.name)
#         print("年龄", self.age)

# class Student(Human):
#     def __init__(self, n, a, s=0):
#         super().__init__(n, a)
        

# s = Student("小张", 20)
# s.show_info()