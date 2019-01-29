

#-------------------------示例1----------------------------
# def mydeco(fn):
#     def fx():
#         print("++++++++++++")
#         fn()
#         print("------------")
#     return fx
# @mydeco#( myfunc = mydeco(myfunc)),同下面
# def myfunc():
#     print("myfunc被调用!!!")

# # myfunc = mydeco(myfunc)

# myfunc()
# myfunc()
# myfunc()


#-----------------------------------示例2---------------------------
#用模拟银行业务需求，用装饰器扩展新功能
#银行：存钱，取钱
# def quanxian(fn):
#     def fx(n, x):
#         print("权限验证中...")
#         fn(n, x)
#     return fx
# def send_message(fn):
#     def fy(n, x):
#         fn(n, x)
#         print("正在发短消息给：", n, '...')
#     return fy
# @send_message
# @quanxian
# def savemoney(name, x):
#     print(name,'存钱', x, '元')
# @send_message
# @quanxian
# def withdraw(name, x):
#     print(name, '取钱', x, '元')

# savemoney('小张', 200)
# savemoney('小赵', 400)
# withdraw('小李', 500)



#此示例lst=[]不会被释放，因此可能会引起函数的不可重入
# L = [1, 2, 3]
# def f(n=0, lst=[]):
#     lst.append(n)
#     print(lst)
# f(4, L)
# f(5, L)
# f(100)
# f(200)
# #改进后
# L = [1, 2, 3]
# def f(n=0, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(n)
#     print(lst)
# f(4, L)
# f(5, L)
# f(100)
# f(200)

import math as m
r = float(input("请输入圆的半径："))
s = m.pi * r ** 2
print("圆的半径是：", s)

