

#s = input("请输入一段字符串：")
#blank_count = 0
#for ch in s:
 #   if ch == ' ':
#        blank_count += 1
#
# print("空格的个数是：",blank_count)


#english_count = 0
#for ch in s:
#    if 0 <= ord(ch) <= 127:
#       english_count += 1
#print("英文字符的个数是：",english_count)


#s = input("请输入：")
#index = len(s)-1  
#while index >= 0:
 #   ch = s[index]
 #   print(ch)
 #   index -= 1

#print('以下用的for')
#for ch in s[::-1]
 #   print(ch)




#for x in range(1,21):
 #   print(x,end=' ')
#print()


#for a in range(101):
 #   if c = x * (x+1) %11 ==8:
 #       print(c)


#c = 0
#for x in range(1,100,2):
 #   c += x
#print(c)



#a = int(input("请输入一个整数："))

#for x in range(a):
 #   for y in range(1,a+1):
 #       print(y ,end=' ')
  #  print()



#for x in range(1,a+1):
 #   for y in range(x ,x+a):
 #       print(y,end=' ')
 #   print()

#a = 0
#for x in range(1,101):
 #   if x % 2 == 0 or x % 3 ==0 or x % 5 ==0 or x % 7 ==0:
  #      continue
  #  a += x
  #  print(a)



#a = input("请输入：")
#b = input("请输入：")
#c = input("请输入：")
#L = [a,b,c]
#print(L)
s = 0 
a = int(input("请输入正整数："))
for x in a:
    if x < 0:
        continue
        s += x
        L = [print(x)]
    print(L)
