
# __all__ = [f1, name1]
# def f1():
#     pass
# def f2():
#     pass
# def f3():
#     pass

# name1 = 'aaa'
# name2 = 'bbb'

# import random
# x = random.randint(0, 100)
# print(x)
# count = 0
# while True:
#     y = int(input("请输入一个整数"))
#     count += 1
#     if y == x :
#         print("你猜对了")
#         break 
#     elif y > x :
#         print("你猜的数字大了")
#     else :
#         print("你猜的数字小了")

# print("你一共猜了", count, '次')




# import random
# L = ['\u2660 ' + 'A', '\u2660 ' + '2', '\u2660 ' + '3', '\u2660 ' + '4', 
# '\u2660 ' + '5', '\u2660 ' + '6', '\u2660 ' + '7', '\u2660 ' + '8',
# '\u2660 ' + '9', '\u2660 ' + '10', '\u2660 ' + 'J', '\u2660 ' + 'Q',
# '\u2660 ' + 'K  ']
# x = random.sample(L, 5)
# y = random.sample(L, 5)
# print(x)
# print(y)

import random
a = [x + y for x in ['\u2660 ', '\u2663 ', '\u2665 ', '\u2666 '] for y in ['A', '2', '3', '4', '5', '6',
'7', '8', '9', '10', 'J', 'Q', 'K']]
b = ['大王', '小王']
L = a + b
L1 = random.sample(L, 17)
input()
print("第一个人的牌：",L1)
print()
L2 = []
for i in  L:
    if i not in L1:
        L2.append(i)
#print("发了第一个人剩余的牌：",L2)
print()
L3 = random.sample(L2, 17)
input()
print("这是第二个人的牌：",L3)
print()
L4 = []
for i in L2:
    if i not in L3:
        L4.append(i)
#print("发了第二个人剩余的牌：", L4)
print()
L5 = random.sample(L4, 17)
input()
print("这是第三个人的牌：",L5)
print()
L6 = []
for i in L4:
    if i not in L5:
        L6.append(i)
input()
print("这是剩余的三张牌：", L6)

