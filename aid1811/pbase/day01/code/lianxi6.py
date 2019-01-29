

#L = [3, 5]
#print(id(L))
#L[0:0] = [1,2]
#L[3:3] = [4]
#L[6:6] = [6]
#print(L)
#print(id(L))


#L[:] = L[::-1]
#L[5:6] = []
#print(L)
#print(id(L))

#L = []
#while True:
    #x = int(input("请输入两个以上的正整数："))
    #if len(L) < 2 and x < 0:
    #    break
    #L +=x
#print(总数为：,sum(L))
#print(最大数为：,max(L))
#print(最小数为：,min(L))

#L = list("hello")
#L2 = ' '.join(L)
#L3 = '-'.join(L)
#print(L2)
#print(L3)

#L = [x%2 != 0 for x in range(1,100)]

