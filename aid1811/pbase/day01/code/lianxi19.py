
#*********************************封装**********************
# class A:
#     def __init__(self):
#         self.__money = 100
#     def borrow(self, x):
#         if x < self.money:
#             self.money -= x
#             return x
#         return 0

# a = A()
# print(a.borrow(20))


# class A:
#     def __init__(self):
#         self.__money = 100
#     def __m(self):
#         print("被调用")
#     def show_info(self):
#         self.__m()
#         print(Self.__money)

# a = A()
# a.show_info()

# class Shape:
#     def draw(self):
#         print("Shap.draw别调用")

# class Point(Shape):
#     def draw(self):
#         print("正在画一个点")

# class Circle(Point):
#     def draw(self):
#         print("正在画一个圆")

# def my_draw(s):
#     s.draw()

# s1 = Circle
# s2 = Point
# my_draw(s1)
# my_draw(s2)

#********************多继承＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# class Plane:
#     def fly(self, height):
#         print("飞机以海拔", height, "米的高度飞行")

# class Car:
#     def run(self, speed):
#         print("汽车以", speed, "公里／小时的速度行驶")

# class PlaneCar(Plane, Car):
#     '''PlaneCar 继承自Plane, Car 类'''

# p1 = PlaneCar()
# p1.fly(10000)
# p1.run(300)

# class A:
#     def go(self):
#         print("A")
# class B(A):
#     def go(self):
#         print("B")
# class C(A):
#     def go(self):
#         print("C")
# class D(B, C):
#     def go(self):
#         print("D")
# d = D()
# d.go()

