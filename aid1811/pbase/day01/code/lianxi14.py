#-----------------------------------示例1-------------------------------------
# def div_applen(n):
#     print("%d个苹果你想分给几个人？"%n)
#     s = input('请输入人数：')
#     count = int(s)
#     result = n / count
#     print("每一个人分了", result, '个苹果')
# try:
#     div_applen(10)
#     print("分苹果成功")
# except ValueError:
#     print("分苹果失败")
# print("程序正常结束")




# try:
#     n = 1000 / 0
#     print(n)
# except ZeroDivisionError:
#     print("0不能为除数")


# def div_applen(n):
#     print("%d个苹果你想分给几个人？"%n)
#     s = input('请输入人数：')
#     count = int(s)
#     result = n / count
#     print("每一个人分了", result, '个苹果')
# try:
#     div_applen(10)
#     print("分苹果成功")
# except ValueError as err:
#     print("分苹果失败, err =", err)
# except:
#     print("除ValueError类型异常，分苹果失败")
# else:
#     print("此try语句内没有发生任何异常，一切安好")
# finally:
#     print("我是try里的finally子句，我一定会被执行")
# print("程序正常结束")


# def get_score():
#     s = input("请输入成绩(0~100):")
#     try:
#         a = int(s)
#     except ValueError:
#         return 0
#     if 0 <= a <= 100:
#         return a
#     else:
#         return 0
# score = get_score()
# print("学生成绩是：", score)
#---------------------------------------示例2----------------------------------

# def fry_egg():
#     print("打开天然气点燃....")
#     try:
#         count = int(input("请输入鸡蛋个数："))
#         print("完成煎鸡蛋，共煎了%d个鸡蛋"%count)
#     finally:
#         print("关闭天然气")

# fry_egg()

# def make_except():
#     print("开始")
#     #raise ValueError
#     error = ValueError("着火了")
#     raise error
#     print("结束")
# try:
#     make_except()
#     print("make_except 调用完成")
# except ValueError as error:
#     print("收到ValueError类型的错误对象")
#     print("error=",error)
# #except ZeroDivisionError:
#     #print("收到ZeroDivisionError类型的错误对象")
# print("程序正常结束")


# def f1():
#     n = int(input("请输入整数："))
    

# def f2():
#     try:
#         f1()
#     except ValueError as err:
#         print("f1函数内错误")
#         print('f2里的err=', err)
#         raise 
# try:
#     f2()
# except ValueError as err:
#     print("f2内发生了ValueError类型错误")
#     print(err)
# def get_age():
#     a = int(input("请输入(0~140)之间的整数"))
#     if a < 0:
#         raise ValueError
#     elif:
#         a > 140
#         raise ValueError
#     else:
#         return a
   
# try:
#     age = get_age()
#     print("用户输入的年龄是：", age)
# except ValueError as err:
#     print("用户输入的不是0~140之间的数")


# def get_score():
#     s = int(input("请输入学生成绩"))
#     return s 
# get_score()
# score = get_score
# print("成绩是", score)

# L = [1, 3, 5, 7, 9]
# it = iter(L)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
        # break

s = {'唐僧', '悟空', '八戒', '沙僧'}
it = iter(s)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
print("遍历结束")


