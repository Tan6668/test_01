# L = [x for x in range(100)]
# print(L)
# r = range(100)
# it = iter(r)
# while True:
#     print(next(it))

#---------------------------------示例1-----------------------------
# def myyield():
#     print("即将生成2")
#     yield 2
#     print("生成器生成结束")

# gen = myyield()
# # print(gen)

# # it = iter(gen)
# # print(next(it))
# # print(next(it))

# for x in gen:
#     print(x)

#-------******************示例2*-*****************************

# def myinteger(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1

# for x in myinteger(10):
#     print(x)
# it = iter(myinteger(20))
# print(next(it))
# print(next(it))
# L = [x for x in MemoryError(20)]
# print(L)

# def myeven(start, stop):
#     i = start
#     while i < stop:
#         if i % 2 == 0:
#             yield i
#         i += 1
        
# evens = list(myeven(10, 20))
# print(evens)
# for x in myeven(21, 30):
#     print(x)
#******************示例3****************************


# L = [2, 3, 5, 7]
# def gen(n):
#     for x in n:
#         yield x ** 2 + 1
# for x in gen(L):
#     print(x)


# L = [2, 3, 5, 7]
# gen = (x ** 2 + 1 for x in L)
# for x  in gen:
#     print(x)


# L = [2, 3, 5, 7]
# L1 = [x ** 2 + 1 for x in L]
# print(L1)


# def myfilter(func, iterable):
#     for x in iterable:
#         if func(x):
#             yield x
#     # it = iter(iterable)
#     # while True:
#     #     try:
#     #         x = next(it)
#     #         if func(x):
#     #             yield x
#     #     except StopIteration:
#     #         return

# for i in myfilter(lambda x: x % 2 == 1, range(10)):
#     print(i)


# def myzip(iterable1, iterable2):
#     it1 = iter(iterable1)
#     it2 = iter(iterable2)
#     while True:
#         try:
#             x1 = next(it1)
#             x2 = next(it2)
#             yield (x1, x2)
#         except StopIteration:
#             return

# numbers = [10086, 10000, 10010, 34543]
# names = ['移动', '电信', '联通']
# for t in myzip(numbers, names):
#     print(t)

def mynumerable(iterable, start=0):
    it1 = iter(iterable)
    while True:
        try:
            x1 = next(it1)
            yield (start, x1)
            start += 1
        except StopIteration:
            return

names = ['移动', '电信', '联通']
for t in mynumerable(names, 101):
    print(t)
