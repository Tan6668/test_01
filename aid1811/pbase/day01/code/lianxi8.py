


#def myadd(x,y):
 #   print(x + y)

#myadd(100,200)
#myadd("ABC","123")

#def print_even(n):
#    for x in range(0,n,2):
#        print(x,end=' ')
#    print()

#print_even(10)

#def mymax(a,b):
 #   return a if a > b else b

#print(mymax(100,200))
#print(mymax("ABC","ABCD"))
 
#def myadd(x,y):
 #   return x + y

#a = int(input("请输入第一个数："))
#b = int(input("请输入第二个数："))
#print(a,'+',b,'的和是',myadd(a,b))

#def input_number():
#    s = []
#    while True:
#        x =int(input("请输入一个数："))
#        if x < 0:
#            break
#        else:
#            s.append(x)
#    return s

#L = input_number()
#print(max(L))
#print(min(L))
#print(sum(L))


def get_chinese_char_count(s):
    count = 0
    for x in s:
        if  0x4E00 <= ord(x) <= 0x9FA5:
            count += 1
    return count

s = input("请输入中英文字混合的字符串：")
print("你输入的中文字符的个数是：",get_chinese_char_count(s))
