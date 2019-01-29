# class MyList:
#     def __init__(self,iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return 'MyList(%s)'%self.data

#     def __iadd__(self,rhs):
#         # self.data.extend(rhs.data) #等同于　下列
#         self.data += rhs.data
#         return self

# l1 = MyList([1,2,3])
# l2 = MyList([4,5,6])
# print(id(l1))
# l1 += l2
# print(l1)
# print(id(l1))

# #此示例示意一元运算符重载
# class MyList2:
#     def __init__(self,iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return 'MyList2(%s)'%self.data
    
#     def __neg__(self):
#         gen = (-x for x in self.data) #生成器，现用现生成，节约空间
#         return MyList2(gen)
#     def __pos__(self):
#         gen = (abs(x) for x in self.data)
#         return MyList2(gen)
#     def __invert__(self):
#         return MyList2(reversed(self.data))
#     def __contains__(self,e):
#         return e in self.data
    
# l1 = MyList2([-1,2,3,-4,5,-8])
# l2 = -l1
# print('l2=',l2)
# l3 = +l1
# print('l3=',l3)
# l4 = ~l1
# print('l4=',l4)
# print(5 in l1)
# print(5 in l2)

# #索引
# class MyList3:
#     def __init__(self,iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return 'MyList3(%s)'%self.data

#     def __getitem__(self,i):
#         return self.data[i]

#     def __setitem__(self,i,v):
#         self.data[i] = v
#     def __delitem__(self,i):
#         del self.data[i]

# l1 = MyList3([-1,2,3,-4,5,-8])
# v = l1[0]     # v = l1.__getitem__(0)
# print(v)
# l1[0] = 10   # l1.__setitem__(0,10)
# print(l1)
# del l1[2]    #l1.__delitiem__(2)
# print(l1)

# #切片
# class MyList4:
#     def __init__(self,iterable=()):
#         self.data = [x for x in iterable]
    
#     def __repr__(self):
#         return 'MyList3(%s)'%self.data

#     def __getitem__(self,i):
#         if type(i) is int:
#             print('正在索引．．．')
#         if type(i) is slice:
#             print('正在切片．．．')
#             print('起始值：',i.start)
#             print('终止值：',i.stop)
#             print('步长：',i.step)
#         return self.data[i]


# l1 = MyList4([-1,2,3,-4,5,-8])

# a = l1[0::2]     #等同与 l1.__getitem__(slice(0,None,2)) slice是一个类
# print(a)
# print(l1)
# b = l1[5::-2]     #等同与 l1.__getitem__(slice(5,None,-2)) slice是一个类
# print(b)


# class Student:
#     def __init__(self,s):
#         self.__score = s
#     def get_sc(self):
#         return self.__score
#     def set_sc(self,s):
#         assert 0 <= s <= 100,'成绩出错'
#         self.__score = s
#         return self.__score


# stu = Student(59) #取值
# print(stu.get_sc())
# stu.score = 999  #无用
# print(stu.set_sc(1000))

# # stu = Student(59) #取值
# # print(stu.score)
# # stu.score = 999 
# # print(stu.score) #999

# class Student2:
#     def __init__(self,s):
#         self.__score = s
#     def get_sc(self):
#         return self.__score
#     def set_sc(self,s):
#         assert 0 <= s <= 100,'成绩出错'
#         self.__score = s
#         return self.__score
#     score = property(get_sc,set_sc)


# stu = Student2(59) #取值
# print(stu.score)
# stu.score = 99 
# print(stu.score)

# class Student3:
#     def __init__(self,s):
#         self.__score = s

#     @property
#     def score(self):
#         return self.__score

#     @score.setter
#     def score(self,s):
#         assert 0 <= s <= 100,'成绩出错'
#         self.__score = s
#         return self.__score


# stu = Student3(59) #取值
# print(stu.score)
# stu.score = 89  
# print(stu.score)

class Human:
    def __init__(self, name="Anonymous", age=0, *args):
        self.name, self.age = name, age
    def infos(self):
        print(self.name, self.age)

class Teacher(Human):
    def __init__(self, name, age, address=""):
        self.address = address
    def infos(self):
        print(self.name, self.age, self.address)

# t1 = Teacher("Mr. zhang", 35)
# t1.infos()
# t1 = Teacher("Mr. zhang", 35)
# t1.infos()
h1 = Human("Mr. zhang", 35, "北京市朝阳区", "其它信息不详")
h1.infos()
h1 = Human()
h1.infos()

class A:
    v = 100
    def __init__(self):
        self.v = 200
a1 = A()
a2 = A()
del a2.v
print(a1.v)
print(a2.v)
