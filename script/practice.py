# -*- coding: utf-8
# 标准库相当于解释器的外部扩展，使用前需要提前导入；
# 内置函数是解释器的一部分，随解释器的启动而生效

# 内置函数 1 - abs - 返回一个数的绝对值
# abs_numbs = abs(-123.123)
# print(abs_numbs)

# 内置函数 2 - all - 判断迭代器的内部所有元素的值是否均为真值
# all_str = all([0, 2, 3, 4, 5])  # 0 值为假
# print(all_str)

# all_str = all([1, 2, 3, 4, 5])
# print(all_str)

# all_str = all({1, 2, 3, 4, 5})
# print(all_str)

# 内置函数 3 - any - 判断迭代器的内部任意元素的值是否均为真值
# all_str = all([1, 2, 3, 4, 5])  # 0 值为假
# print(all_str)

# 内置函数 4 - ascii

# 内置函数 5 - bin

# 内置函数 6 - bool

# 内置函数 7 - breakpoint

# 内置函数 8 - bytearray

# 内置函数 9 - bytes

# 内置函数 10 - callable

# 内置函数 11 - chr

# 内置函数 12 - classmethod

# 内置函数 13 - compile

# 内置函数 14 - complex

# 内置函数 15 - delattr

# 内置函数 16 - dict

# 内置函数 17 - dir

# 内置函数 18 - divmod

# 内置函数 19 - enumerate

# 内置函数 20 - eval

# 内置函数 21 - exec

# 内置函数 22 - filter

# 内置函数 23 - float

# 内置函数 24 - format

# 内置函数 25 - forzenset

# 内置函数 26 - getattr

# 内置函数 27 - globals

# 内置函数 28 - hasattr

# 内置函数 29 - hash

# 内置函数 30 - help

# 内置函数 31 - hex

# 内置函数 32 - id

# 内置函数 33 - input

# 内置函数 34 - int

# 内置函数 35 - isinstance

# 内置函数 36 - issubclass

# 内置函数 37 - iter

# 内置函数 38 - len

# 内置函数 39 - list

# 内置函数 40 - locals

# 内置函数 41 - map

# 内置函数 42 - max

# 内置函数 43 - memoryview

# 内置函数 44 - min

# 内置函数 45 - next

# 内置函数 46 - object

# 内置函数 47 - oct

# 内置函数 48 - open

# 内置函数 49 - ord - 对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数
# ordStr = ord('a')
# print(ordStr)

# 内置函数 50 - pow

# 内置函数 51 - print

# 内置函数 52 - property

# 内置函数 53 - range

# 内置函数 54 - repr

# 内置函数 55 - reversed

# 内置函数 56 - round

# 内置函数 57 - set

# 内置函数 58 - setattr

# 内置函数 59 - slice

# 内置函数 60 - sorted

# 内置函数 61 - staticmethod

# 内置函数 62 - str

# 内置函数 63 - sum

# 内置函数 64 - super

# 内置函数 65 - tuple

# 内置函数 66 - type

# 内置函数 67 - vars

# 内置函数 68 - zip

# 内置函数 69 - __import__

# Python 变量类型和运算符
# Python 变量的定义与事用
# num = 8888888888888888888888
# print(type(num))

# Python整数类型（int）详解
# 十进制 0-9
# 二进制形式 0/1， 0b 或 0B 开头
# 八进制 0-7， 0o 或 0O 开头
# 十六进制 0-9A-F（a-f）,0x 或 0X 开头
# 十六进制
# hex1 = 0x45
# hex2 = 0x4Af
# print("hex1Value: ", hex1)
# print("hex2Value: ", hex2)

# # 二进制
# bin1 = 0b101
# print('bin1Value: ', bin1)
# bin2 = 0B110
# print('bin2Value: ', bin2)

# # 八进制
# oct1 = 0o26
# print('oct1Value: ', oct1)
# oct2 = 0O41
# print('oct2Value: ', oct2)

# click = 1301547
# distance = 384000000
# print("Python教程阅读量：", click)
# print("地球和月球的距离：", distance)

# print(type(12E4))  # 指数形式的小数

# Python 复数类型（complex）详解: 实部 + 虚部（以j 或 J 作为后缀）
# c1 = 12 + 0.2j
# print(c1, type(c1))

# c2 = 6 - 1.2j
# print(c2, type(c2))

# print(c1 + c2)
# print(c1 - c2)

# Python 字符串详解（包含长字符串和原始字符串）
# s2 = '''It took me six months to write this Python tutorial.
# Please give me more support.
# I will keep it updated.'''
# num = 20 + 4 / 4 + \
#     2 * 3
# print(s2)
# print(num)

# rstr = 'D:\\Program Files\\Python 3.8\\python.exe'
# print(rstr)

# rstr = r'D:\\Program Files\\Python 3.8\\python.exe'
# print(rstr)

# str1 = r'I\'m a great coder!'
# print(str1)

# str1 = 'I\'m a great coder!'
# print(str1)

# str1 = r'D:\Program Files\Python 3.8' '\\'
# print(str1)

# Python bytes 类型及用法

# Python input() 函数：获取用户输入的字符串
# str = input("Enter a number: ")
# print(str)

# a = input("Enter a number: ")
# b = input("Enter another number: ")
# print("aType: ", type(a))
# print("bType: ", type(b))
# result = a + b
# print("resultValue: ", result)
# print("resultType: ", type(result))

# a = input("Enter a number: ")
# b = input("Enter another number: ")
# a = float(a)
# b = int(b)
# print("aType: ", type(a))
# print("bType: ", type(b))
# result = a + b
# print("resultValue: ", result)
# print("resultType: ", type(result))

# Python print() 函数高级用法
# user_name = 'Charlie'
# user_age = 8
# # 同时输出多个变量和字符串
# print("name: ", user_name, "age", user_age, sep = '|')
# print("name: ", user_name, "age", user_age, sep = '|', end="")
# print("name: ", user_name, "age", user_age, "\t", sep = '|', end="")

# f = open("demo.txt", "w")
# print("abc", file=f)
# print("123", file=f)
# f.close()

# Python 格式化字符串（格式化输出）
# age = 8
# print("C语言中文网已经%d岁了！" %age)

# name = "C语言中文网"
# age = 8
# url = "http://c.biancheng.net/"
# print("%s已经%d岁了，它的网址是%s。" % (name, age, url))
# 指定最小输出宽度
# n = 1234567
# print("n(10):%10d." % n)
# print("n(5):%5d." % n)
# url = "http://c.biancheng.net/python/"
# print("url(35):%35s." % url)
# print("url(20):%20s." % url)
# 指定对齐方式
# 指定小数精度

# Python 转义字符及用法 \0dd 八进制编码方式，\xhh 十六进制编码方式
# str1 = "Oct: \061\062\063"
# str2 = "Hex: \x31\x32\x33\x78\x79\x7A"
# print(str1)
# print(str2)

# Python 类型转换， Python 数据类型转换函数大全
# height = 79.0
# print(height, type(height))
# print("您的身高： " , height)
# print("您的身高： "  + str(height))

# Python 算术运算符及拥发详解
# + 加；- 减；* 乘； / 除； // 整除； % 取余； ** 幂运算；

# Python 赋值运算符
# 基本赋值运算符 = 
# 扩展后的赋值运算符

# Python 位运算符详解

# Python 比较运算符（关系运算符）
# a = 123
# b = 123
# c = 123.123
# d = 123.123

# e = f = c

# print(a == b, a is b)
# print(e is f, c is d)

# Python 逻辑运算符及其用法 
# and: and 运算优先级大于or
# or
# not

# url = "http://c.biancheng.net/cplus/"
# print("----False and xxx-----")
# print( False and print(url) )
# print("----True and xxx-----")
# print( True and print(url) )
# print("----False or xxx-----")
# print( False or print(url) )
# print("----True or xxx-----")
# print( True or print(url) )

# pB = print("http://c.biancheng.net/cplus/")
# print(pB) # None

# Python 三目运算符（三元运算符）用法详解
# a = int(input("Input a: "))
# b = int(input("Input b: "))
# print("a 大于 b") if a > b else (print("a 小于 b") if a < b else print("a = b"))

# Python 运算符优先级，左结合性与右结合性

# Python 序列详解（包括序列类型和常用操作）
# 序列索引
# 序列切片
# 序列相加
# 序列相乘
# 检查元素是否包含在序列中
# str="C语言中文网"
# print(str[0] == str[-6])
# print(str[5] == str[-1])
# print(str[:2])
# print(str[::2])

# str="c.biancheng.net"
# print('c'in str)

# 和序列相关的内置函数
# strL="c.biancheng.net"
# #找出最大的字符
# print(max(strL))
# #找出最小的字符
# print(min(strL))
# #对字符串中的元素进行排序
# print(sorted(strL))

# print(reversed(sorted(strL)))

# print(len(strL))

# print(list(strL))

# print(str(strL))

# print(sum([1, 2, 3]))

# Python list 列表详解
# print(type( ["http://c.biancheng.net/python/", 1, [2,3,4] , 3.0] ))

# num = [1, 2, 3, 4, 5, 6, 7]
# name = ["C语言中文网", "http://c.biancheng.net"]
# program = ["C语言", "Python", "Java"]
# emptylist = [ ]

# print(num, name, program, emptylist)

# 将字符串转换成列表
# list1 = list("hello")
# print(list1)

# # 将元组转换成列表
# tuple1 = ('Python', 'Java', 'C++', 'JavaScript')
# list2 = list(tuple1)
# print(list2)

# # 将字典转换成列表
# dict1 = {'a':100, 'b':42, 'c':9}
# list3 = list(dict1)
# print(list3)

# # 将区间转换成列表
# range1 = range(1, 6)
# list4 = list(range1)
# print(list4)

# # 创建空列表
# print(list())

#Python删除列表 del
# intlist = [1, 45, 8, 34]
# print(intlist)
# del intlist
# print(intlist)

# a = 123
# print (a)
# del a
# print (a)

# Python list 列表添加元素的3 种方法
# 拼接法 +
# language = ["Python", "C++", "Java"]
# language2 = ["Python", "C++"]
# birthday = [1991, 1998, 1995]
# info = language + birthday
# print("language =", language)
# print("birthday =", birthday)
# print("info =", info)

# Python append() 方法添加元素，用于在列表的末尾追加元素
# l = ['Python', 'C++', 'Java']
# #追加元素
# l.append('PHP')
# print(l)

# #追加元组，整个元组被当成一个元素
# t = ('JavaScript', 'C#', 'Go')
# l.append(t)
# print(l)

# #追加列表，整个列表也被当成一个元素
# l.append(['Ruby', 'SQL'])
# print(l)

# print(l + ['Ruby', 'SQL'])

# Python extend() 方法添加元素
# l = ['Python', 'C++', 'Java']
# #追加元素
# l.extend('C')
# print(l)

# #追加元组，元祖被拆分成多个元素
# t = ('JavaScript', 'C#', 'Go')
# l.extend(t)
# print(l)

# #追加列表，列表也被拆分成多个元素
# l.extend(['Ruby', 'SQL'])
# print(l)

# Python insert() 方法插入元素
# l = ['Python', 'C++', 'Java']
# #插入元素
# l.insert(1, 'C')
# print(l)

# #插入元组，整个元祖被当成一个元素
# t = ('C#', 'Go')
# l.insert(2, t)
# print(l)

# #插入字符串，整个字符串被当成一个元素
# l.insert(0, "http://c.biancheng.net")
# print(l)

# Python list 列表删除元素（4种方法）
# del 根据索引值删除元素
# pop() 根据索引值删除元素
# remove() 根据元素值进行删除
# clear() 删除列表所有元素

# lang = ["Python", "C++", "Java", "PHP", "Ruby", "MATLAB"]
# #使用正数索引
# del lang[2]
# print(lang)
# #使用负数索引
# del lang[-2]
# print(lang)

# nums = [40, 36, 89, 2, 36, 100, 7]
# nums.pop(3)
# print(nums)
# nums.pop()
# print(nums)

# nums = [40, 36, 89, 2, 36, 100, 7]
# #第一次删除36
# nums.remove(36)
# print(nums)
# #第二次删除36
# nums.remove(36)
# print(nums)
# #删除78
# nums.remove(78)
# print(nums)

# url = list("http://c.biancheng.net/python/")
# url.clear()
# print(url)

# Python list 列表修改元素
# 修改单个元素
# 修改一组元素

# nums = [40, 36, 89, 2, 36, 100, 7]
# nums[2] = -26  #使用正数索引
# nums[-3] = -66.2  #使用负数索引
# print(nums)

# nums = [40, 36, 89, 2, 36, 100, 7]
# #修改第 1~4 个元素的值（不包括第4个元素）
# nums[1: 1] = [45.25, -77, -52.5]
# print(nums)

# nums = [40, 36, 89, 2, 36, 100, 7]
# #在4个位置插入元素
# nums[4: 4] = [-77, -52.5, 999]
# print(nums)

# Python list 列表查找元素
# index() 方法
# count() 方法

# nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
# #检索列表中的所有元素
# print( nums.index(2) )
# #检索3~7之间的元素
# print( nums.index(100, 3, 7) )
# #检索4之后的元素
# print( nums.index(7, 4) )
# #检索一个不存在的元素
# print( nums.index(55) )

# nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
# #统计元素出现的次数
# print("36出现了%d次" % nums.count(36))
# #判断一个元素是否存在
# if nums.count(100):
#     print("列表中存在100这个元素")
# else:
#     print("列表中不存在100这个元素")

# print("列表中存在 36") if nums.count(36) else print("列表中不存在 36")

# Python tuple 元组详解
# 不可变序列
# print(type( ("c.biancheng.net",1,[2,'a'],("abc",3.0)) ))

# Python 创建元组
# num = (7, 14, 21, 28, 35)
# course = ("Python教程", "http://c.biancheng.net/python/")
# abc = ( "Python", 19, [1,2], ('c',2.0) )
# print(num, course)
# print(abc)

# course = "Python教程", "http://c.biancheng.net/python/"
# print(course)

#最后加上逗号
# a =("http://c.biancheng.net/cplus/",)
# print(type(a))
# print(a)
# #最后不加逗号
# b = ("http://c.biancheng.net/socket/")
# print(type(b))
# print(b)

# 使用 tuple() 函数创建元组
# 将字符串转换成元组
# tup1 = tuple("hello")
# print(type(tup1), tup1)

# #将列表转换成元组
# list1 = ['Python', 'Java', 'C++', 'JavaScript']
# tup2 = tuple(list1)
# print(tup2)

# #将字典转换成元组
# dict1 = {'a':100, 'b':42, 'c':9}
# tup3 = tuple(dict1)
# print(tup3)

# #将区间转换成元组
# range1 = range(1, 6)
# tup4 = tuple(range1)
# print(tup4)

# #创建空元组
# print(tuple())

# # Python 访问元组元素
# url = tuple("http://c.biancheng.net/shell/")
# #使用索引访问元组中的某个元素
# print(url[3])  #使用正数索引
# print(url[-4])  #使用负数索引
# #使用切片访问元组中的一组元素
# print(url[9: 18])  #使用正数切片
# print(url[9: 18: 3])  #指定步长
# print(url[-6: -1])  #使用负数切片

# Python 修改元组
# 元组是不可变序列，通过创建一个新的元组去替代旧的元组

# tup = (100, 0.5, -36, 73)
# print(tup)
# # 对元组进行重新赋值
# tup = ('Shell脚本',"http://c.biancheng.net/shell/")
# print(tup)

# tup1 = (100, 0.5, -36, 73)
# tup2 = (3+12j, -54.6, 99)
# print(tup1+tup2)
# print(tup1)
# print(tup2)

# # Python 删除元组
# tup = ('Java教程',"http://c.biancheng.net/java/")
# print(tup)
# del tup
# print(tup)

# Python dict 字典详解
# Python dict 是一种无序的、可变的序列，它的元素以键值对的形式存储

# a = {'one': 1, 'two': 2, 'three': 3}  #a是一个字典类型
# print(type(a), a, a['one'])

# Python 创建字典
# 使用 {} 创建字典
# 通过 fromkeys() 方法创建字典
# 通过 dict() 映射函数创建字典

# #使用字符串作为key
# scores = {'数学': 95, '英语': 92, '语文': 84}
# print(scores)
# #使用元组和数字作为key
# dict1 = {(20, 30): 'great', 30: [1,2,3]}
# print(dict1)
# #创建空元组
# dict2 = {}
# print(dict2)

# knowledge = ['语文', '数学', '英语']
# scores = dict.fromkeys(knowledge, 60)
# print(scores) # {'语文': 60, '数学': 60, '英语': 60}

# a = dict(a= 1, b = 2, c = "c", 第四个 = "第四个")
# print(type(a), a)

# #方式1
# demo = [('two',2), ('one',1), ('three',3)]
# print(type(demo), demo)
# #方式2
# demo = [['two',2], ['one',1], ['three',3]]
# print(type(demo), demo)
# #方式3
# demo = (('two',2), ('one',1), ('three',3))
# print(type(demo), demo)
# #方式4
# demo = (['two',2], ['one',1], ['three',3])
# print(type(demo), demo)
# a = dict(demo)
# print(type(a), a)

# keys = ['one', 'two', 'three'] 
# values = [1, 2, 3]
# a = dict( zip(keys, values) )
# print(type(a), a)

# 创建空的字典
# d = dict()
# print(d)

# Python 访问字典表
# tup = (['two',26], ['one',88], ['three',100], ['four',-59])
# dic = dict(tup)
# print(dic['one'])  #键存在
# print(dic['five'])  #键不存在

# a = dict(two=0.65, one=88, three=100, four=-59)
# print( a.get('one'), a.get('five'), a.get('five', '该键不存在') )

# Python 删除字典
# a = dict(two=0.65, one=88, three=100, four=-59)
# print(a)
# del a['two']
# print(a)

# del a
# print(a)

# Python 字典基本操作（包括添加、修改、删除键值对）
# # Python字典添加键值对
# a = {'数学':95}
# print(a)
# #添加新键值对
# a['语文'] = 89
# print(a)
# #再次添加新键值对
# a['英语'] = 90
# print(a)

# # Python字典修改键值对
# a = {'数学': 95, '语文': 89, '英语': 90}
# print(a)
# a['语文'] = 100
# print(a)

# # Python字典删除键值对
# # 使用del语句删除键值对
# a = {'数学': 95, '语文': 89, '英语': 90}
# del a['语文']
# del a['数学']
# print(a)

# 判断字典中是否存在指定键值对
# a = {'数学': 95, '语文': 89, '英语': 90}
# # 判断 a 中是否包含名为'数学'的key
# print('数学' in a) # True
# # 判断 a 是否包含名为'物理'的key
# print('物理' in a) # False

# print(dir(dict))

# Python dict字典方法完全攻略（全）
# keys()、values() 和 items() 方法

# scores = {'数学': 95, '语文': 89, '英语': 90}
# print(scores.keys())
# print(scores.values())
# print(scores.items())

# a = {'数学': 95, '语文': 89, '英语': 90}
# b = list(a.keys())
# print(b)

# b = list(a.values())
# print(b)

# b = list(a.items())
# print(b)

# a = {'数学': 95, '语文': 89, '英语': 90}
# for k in a.keys():
#     print(k,end=' ')
# print("\n---------------")
# for v in a.values():
#     print(v,end=' ')
# print("\n---------------")
# for k,v in a.items():
#     print("key:",k," value:",v)

# copy() 方法
# a = {'one': 1, 'two': 2, 'three': [1,2,3]}
# b = a.copy()
# print(type(b), b)

# a = {'one': 1, 'two': 2, 'three': [1,2,3]}
# b = a.copy()
# #向 a 中添加新键值对，由于b已经提前将 a 所有键值对都深拷贝过来，因此 a 添加新键值对，不会影响 b。
# a['four']=100
# print(a)
# print(b)
# #由于 b 和 a 共享[1,2,3]（浅拷贝），因此移除 a 中列表中的元素，也会影响 b。
# b['three'].remove(1)
# print(a)
# print(b)

# # update() 方法
# a = {'one': 1, 'two': 2, 'three': 3}
# a.update({'one':4.5, 'four': 9.3})
# print(a)

# # pop() 和 popitem() 方法
# a = {'数学': 95, '语文': 89, '英语': 90, '化学': 83, '生物': 98, '物理': 89}
# print(a)
# a.pop('化学')
# print(a)
# a.popitem()
# print(a)

# # setdefault() 方法
# a = {'数学': 95, '语文': 89, '英语': 90}
# print(a)
# #key不存在，指定默认值
# a.setdefault('物理', 94)
# print(a)
# #key不存在，不指定默认值
# a.setdefault('化学')
# print(a)
# #key存在，指定默认值
# a.setdefault('数学', 100)
# print(a)

# Python set 集合详解
# Python 中的集合，用来保存不重复的元素，即集合中的元素都是唯一的，互不相同；
# 同一个结合，只能存储不可变的数据类型

# a =  {1,2,1,(1,2,3),'c','c'}
# print(type(a), a)

# Python 创建set 集合
# 使用 {} 创建
# set() 函数创建集合
# a = {1,'c',1,(1,2,3),'c'}
# print(type(a),a)

# # Python 访问set 集合元素
# a = {1,'c',1,(1,2,3),'c'}
# for ele in a:
#    print(ele,end=',')

# # Python删除set集合
# a = {1,'c',1,(1,2,3),'c'}
# print(a)
# del(a)
# print(a)

# Python set 集合基本操作（添加、删除、交集、并集、差集）
# 向 set 集合中添加元素
# a = {1,2,3}
# a.add((1,2))
# print(a)
# a.add([1,2])
# print(a)

# 从set集合中删除元素
# a = {1,2,3}
# a.remove(1)
# print(a)
# a.remove(1)
# print(a)

# a = {1,2,3}
# a.remove(1)
# print(a)
# a.discard(1)
# print(a)

# Python set集合做交集、并集、差集运算
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 & set2)  # 交集
# print(set1 | set2)  # 并集
# print(set1 - set2)  # 差集
# print(set1 ^ set2)  # 对称差集

# Python set 集合方法详解（全）
# print(dir(set))

# # Python frozenset 集合（set 集合的不可变版本）
# # print(dir(frozenset))
# s = {'Python', 'C', 'C++'}
# fs = frozenset(['Java', 'Shell'])
# s_sub = {'PHP', 'C#'}
# #向set集合中添加frozenset
# s.add(fs)
# print('s =', s, type(s))
# print(type(fs), fs)
# #向为set集合添加子set集合
# s.add(s_sub)
# print('s =', s)

# Python 字符串拼接（包含字符串拼接数字）
# str1 = "Python教程" "http://c.biancheng.net/python/"
# print(str1)
# str2 = "Java" "Python" "C++" "PHP"
# print(str2)

# name = "C++教程"
# url = "http://c.biancheng.net/cplus/"
# info = name + "的网址是：" + url
# print(info)

# Python字符串和数字的拼接
# name = "C语言中文网"
# age = 8
# course = 30
# info = name + "已经" + str(age) + "岁了，共发布了" + repr(course) + "套教程。"
# print(info)

# str() 用于将数据转换成适合人类阅读的字符串形式；
# repr() 用于将数据转换成适合解释器阅读的字符串形式（Python表达式的形式）， 适合在开发和调试阶段使用，如果没有等价的语法，则会发生SyntaxError 异常；

# s = "http://c.biancheng.net/shell/"
# s_str = str(s)
# s_repr = repr(s)
# print( type(s_str) )
# print (s_str)
# print( type(s_repr) )
# print (s_repr)

# # Python 截取字符串（字符串切片）方法详解
# url = 'http://c.biancheng.net/python/'
# #获取索引为10的字符
# print(url[10])
# #获取索引为 6 的字符
# print(url[-6])

# # 获取多个字符（字符串截去/字符串切片）
# url = 'http://c.biancheng.net/java/'
# #获取索引从3处22（不包含22）的子串
# print(url[7: 22]) # 输出 zy
# #获取索引从7处到-6的子串
# print(url[7: -6]) # 输出 zyit.org is very
# #获取索引从-7到6的子串
# print(url[-21: -6])
# #从索引3开始，每隔4个字符取出一个字符，直到索引22为止
# print(url[3: 22: 4])

# Python len() 函数详解： 获取字符串长度或字节数
# a='http://c.biancheng.net'
# print(len(a))

# str1 = "人生苦短，我用Python"
# print(len(str1.encode()))

# Python split() 方法详解：分割字符串
# print(dir(str))

# str = "C语言中文网 >>> c.biancheng.net"
# print(type(str), str)

# list1 = str.split() #采用默认分隔符进行分割
# print(type(list1), list1)

# list2 = str.split('>>>') #采用多个字符进行分割
# print(type(list2), list2)

# list3 = str.split('.') #采用 . 号进行分割
# print(type(list3), list3)

# list5 = str.split('>') #采用 > 字符进行分割
# print(type(list5), list5)

# str = "C语言中文网   >>>   c.biancheng.net"  #包含 3 个连续的空格
# list6 = str.split()
# print(type(list6), list6)

# Python join() 方法：合并字符串

# list = ['c','biancheng','net']
# a = '.'.join(list)
# print(type(a), a)

# dir = '','usr','bin','env'
# print(type(dir), dir)
# a = '/'.join(dir)
# print(type(a), a)

# str = "c.biancheng.net"
# print(str.count('bian'))

# Python find() 方法：检测字符串中是否包含某字符串
# str = "c.biancheng.net"
# print(str.find('z'), str.find('e'))

# Python index() 方法： 监测字符串中是否包含某字符串
# str = "c.biancheng.net"
# print(str.index('z'))

# S = 'http://c.biancheng.net/python/'
# addr = 'http://c.biancheng.net'
# print(S.ljust(35, '-'), len(S))
# print(addr.ljust(35, '-'), len(addr))

# print(S.rjust(35, '-'), len(S))
# print(addr.rjust(35, '-'), len(addr))

# print(S.center(35, '-'), len(S))
# print(addr.center(35, '-'), len(addr))

# Python startswith() 和 endswith() 方法
# str = "c.biancheng.net"
# print(type(str), str, str.startswith('c'), str.startswith('.', 1), str.endswith('t'))

# Python 字符串大小写转换（3种）函数及用法
# str = "c.biancheng.net"
# print(str.title(), str)

# str = "I LIKE c"
# print(str.lower(), str)

# str = "i like C"
# print(str.upper(), str)

# Python 去除字符串中空格（删除指定字符）的3在种方法
# str = "  c.biancheng.net \t\n\r"
# print(type(str), str.center(len(str) + 2, '-'))
# str1 = str.strip()
# print(type(str1), str1.center(len(str1) + 2, '-'))

# #以货币形式显示
# print("货币形式：{:,d}".format(1000000))
# #科学计数法表示
# print("科学计数法：{:E}".format(1200.12))
# #以十六进制表示
# print("100的十六进制：{:#x}".format(100))
# #输出百分比形式
# print("0.01的百分比表示：{:.0%}".format(0.01))

# Python encode() 和 decode() 方法：字符串编码转换
# str = "C语言中文网"
# print(str.encode())
# print(str.encode("UTF-8"))
# print(str.encode('GBK'))
# print(str.encode('gb2312'))

# str = "C语言中文网"
# bytes = str.encode("GBK")
# print(type(bytes), bytes)
# print(bytes.decode("utf-8", "ignore"))

# Python dir() 和 help() 帮助函数
# print(dir())
# print(help())

# Python 流程控制
# 顺序结构、选择（分支）结构和 循环结构；

# Python if else 条件语句详解
# age = int(input("请输入你的年龄： "))
# if age < 18:
#     print("你还未成年，建议在家人陪同下使用该软件！")
#     print("如果你已经得到了家长的同意，请忽略以上提示。")

# #该语句不属于if的代码块
# print("软件正在使用中...")

# import sys

# age = int(input("请输入你的年龄： "))
# if age < 18:
#     print("你还未成年，建议在家人陪同下使用该软件！")
#     print("如果你已经得到了家长的同意，请忽略以上提示。")
#     sys.exit()
# else:
#     print("你已经成年，可以使用该软件。")
#     print("时间宝贵，请不要在该软件上浪费太多时间。")

# print("软件正在使用中...")

# height = float(input("输入身高（米）："))
# weight = float(input("输入体重（千克）："))
# bmi = weight / (height * height)  #计算BMI指数

# if bmi < 18.5:
#     print("BMI指数为："+str(bmi))
#     print("体重过轻")
# elif bmi >= 18.5 and bmi < 24.9:
#     print("BMI指数为："+str(bmi))
#     print("正常范围，注意保持")
# elif bmi>=24.9 and bmi<29.9:
#     print("BMI指数为："+str(bmi))
#     print("体重过重")
# else:
#     print("BMI指数为："+str(bmi))
#     print("肥胖")

# Python if else 条件语句
# b = False
# if b:
#     print('b是True')
# else:
#     print('b是False')
# n = 0
# if n:
#     print('n不是零值')
# else:
#     print('n是零值')
# s = ""
# if s:
#     print('s不是空字符串')
# else:
#     print('s是空字符串')
# l = []
# if l:
#     print('l不是空列表')
# else:
#     print('l是空列表')
# d = {}
# if d:
#     print('d不是空字典')
# else:
#     print('d是空字典')
# def func():
#     print("函数被调用")
# if func():      # func() 执行结果返回值为空，即 None
#     print('func()返回值不是空')
# else:
#     print('func()返回值为空')

# Python if else 对缩进的要求
# Python 是以缩进来标记代码块的，代码块一定要有缩进，没有缩进的不是代码块。 另外，同一个代码块的缩进量要相同，缩进量不同的不属于同一个代码块；
# age = int( input("请输入你的年龄：") )
# if age < 18 :
#     print("警告：你还未成年，不能使用该软件！")
# else:
#     print("你已经成年，可以使用该软件。")

# 不要忘记缩进
# 缩进多少合适
# Python 要求代码块必须缩进，但是却没有要求缩进量，你可以缩进 n 个空格， 也可以缩进 n 个Tab 键的位置

# 所有语句都要缩进
# age = int( input("请输入你的年龄：") )
# if age < 18 :
#     print("你还未成年，建议在家人陪同下使用该软件！")
# print("未成年人如果得到了家长的同意，请忽略以上提示。")  #忘记缩进

# age = int( input("请输入你的年龄：") )
# if age < 18 :
#     print("你还未成年，建议在家人陪同下使用该软件！")
#     print("未成年人如果得到了家长的同意，请忽略以上提示。")  #缩进量不对

# 不要随便缩进
# info = "Python教程的网址是：http://c.biancheng.net/python/"
#     print(info)

# Python if 语句嵌套
# proof = int(input("输入驾驶员每 100ml 血液酒精的含量："))
# if proof < 20:
#     print("驾驶员不构成酒驾")
# else:
#     if proof < 80:
#         print("驾驶员已构成酒驾")
#     else:
#         print("驾驶员已构成醉驾")

# Python pass 语句及其作用, Python 中的关键字，用来让解释器跳过此处，什么都不做
# age = int( input("请输入你的年龄：") )
# if age < 12 :
#     print("婴幼儿")
# elif age >= 12 and age < 18:
#     print("青少年")
# elif age >= 18 and age < 30:
#     print("成年人")
# elif age >= 30 and age < 50:
#     pass
# else:
#     print("老年人")

# # Python assert 断言函数及用法
# mathmark = int(input())
# # 断言数学考试分数是否位于正常范围内
# assert 0 <= mathmark <= 100
# # 只有当 mathmark 位于 [0,100]范围内，程序才会继续执行
# print("数学考试分数为：",mathmark)

# # Python while 循环语句详解
# # 循环的初始化条件
# num = 1
# # 当 num 小于100时，会一直执行循环体
# while num < 100 :
#     print("num=", num)
#     # 迭代语句
#     num += 1
# print("循环结束!")

# my_char="http://c.biancheng.net/python/"
# print(type(my_char), my_char, len(my_char))

# i = 0
# while i<len(my_char):
#     print(my_char[i],end="")
#     i = i + 1

# Python for 循环及用法详解
# add = "http://c.biancheng.net/python/"
# #for循环，遍历 add 字符串
# for ch in add:
#     print(ch,end="")

# # Python for 循环的具体应用
# print(range(101), list(range(101)))
# print("计算 1+2+...+100 的结果为：")
# #保存累加结果的变量
# result = 0
# #逐个获取从 1 到 100 这些值，并做累加操作
# for i in range(101):
#     result += i
# print(result)

# my_list = [1,2,3,4,5]
# for ele in my_list:
#     print('ele =', ele)

# my_tup = (1,2,3,4,5)
# for ele in my_tup:
#     print('ele =', ele)

# my_set = {"a": 1, "b": 2}
# for k in my_set:
#     print('ele =', k)

# # items()、keys() 以及 values()
# my_dic = {'python教程':"http://c.biancheng.net/python/",\
#           'shell教程':"http://c.biancheng.net/shell/",\
#           'java教程':"http://c.biancheng.net/java/"}
# for ele in my_dic.items():
#     print('ele =', ele)

# Python 循环结构中 else 用法
# add = "http://c.biancheng.net/python/"
# i = 0
# while i < len(add):
#     print(add[i],end="")
#     i = i + 1
# else:
#     print("\n执行 else 代码块")

# add = "http://c.biancheng.net/python/"
# i = 0
# while i < len(add):
#     print(add[i],end="")
#     i = i + 1
# #原本位于 else 代码块中的代码
# print("\n执行 else 代码块")

# Python （for 和 while）循环嵌套及用法
# i = 0
# while i<10:
#     for j in range(10):
#         print("i=",i," j=",j)       
#     i=i+1

# Python break 用法详解
# add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
# # 一个简单的for循环
# for i in add:
#     if i == ',' :
#         #终止循环
#         break
#     print(i,end="")
# print("\n执行循环体外的代码")

# add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
# for i in add:
#     if i == ',' :
#         #终止循环
#         break
#     print(i,end="")
# else:
#     print("执行 else 语句中的代码")
# print("\n执行循环体外的代码")

# add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
# print(type(range(3)), range(3), list(range(3)))
# for i in range(3):
#     print(i)
#     for j in add:
#         if j == ',':
#             break   
#         print(j,end="")
#     print("\n跳出内循环")

# add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
# #提前定义一个 bool 变量，并为其赋初值
# flag = False
# for i in range(3):
#     print(type(range(3)), range(3), list(range(3)))
#     for j in add:
#         if j == ',':
#             #在 break 前，修改 flag 的值
#             flag = True
#             break   
#         print(j,end="")
#     print("\n跳出内循环")
#     #在外层循环体中再次使用 break
#     if flag == True:
#         print("跳出外层循环")
#         break

# Python continue 的用法
# add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
# # 一个简单的for循环
# for i in add:
#     if i == ',' :
#         # 忽略本次循环的剩下语句
#         print('\n')
#         continue
#     print(i,end="")

# Python zip 函数及用法
# Python 内置函数之一，将多个序列 “压缩” 成一个zip 对象
# 将这些序列中对应位置的元素重新组合，生成一个新的元组
# zip(iterable, ...)   iterable,... 表示多个列表、元组、字典、集合、字符串，甚至还可以为 range() 区间；
# my_list = [11,12,13]
# my_tuple = (21,22,23)
# combine_zip = zip(my_list,my_tuple)
# print(type(combine_zip), combine_zip)
# print([x for x in combine_zip])
# my_dic = {31:2,32:4,33:5}
# my_set = {41,42,43,44}
# print([x for x in zip(my_dic)])
# my_pychar = "python"
# my_shechar = "shell"
# print([x for x in zip(my_pychar,my_shechar)])

# my_list = [11,12,13, 14, 15]
# my_tuple = (21,22,23, 24)
# print(zip(my_list,my_tuple), list(zip(my_list,my_tuple)))

# Python reversed 函数及用法
# 对于给定的序列（包括列表、元组、字符串以及range(n)区间）， 该函数可以返回一个逆序列的迭代器（用于遍历该逆序序列）
#将列表进行逆序
# print([x for x in reversed([1,2,3,4,5])])
# #将元组进行逆序
# print([x for x in reversed((1,2,3,4,5))])
# #将字符串进行逆序
# print([x for x in reversed("abcdefg")])
# #将 range() 生成的区间列表进行逆序
# print([x for x in reversed(range(10))])

# list1 = [1,2,3,4,5]
# print(type(list1), list1, reversed(list1))
# for item in reversed(list1):
#     print(item, end=",")

# rlist = reversed([1,2,3,4,5])
# print(type(rlist), rlist, list(rlist), [rlist])    
# print([x for x in rlist])

# Python sorted 函数及用法
# 对序列（列表、元组、字典、集合、还包括字符串） 进行排序
#对列表进行排序
# a = [5,3,4,2,1]
# print(sorted(a))
# #对元组进行排序
# a = (5,4,3,1,2)
# print(sorted(a))
# #字典默认按照key进行排序
# a = {4:1,\
#      5:2,\
#      3:3,\
#      2:6,\
#      1:8}
# print(sorted(a.items()))
# #对集合进行排序
# a = {1,5,3,2,4}
# print(sorted(a))
# #对字符串进行排序
# a = "51423"
# print(sorted(a))

# a = "51423"
# print(sorted(a, reverse=True))

# chars=['http://c.biancheng.net',\
#        'http://c.biancheng.net/python/',\
#        'http://c.biancheng.net/shell/',\
#        'http://c.biancheng.net/java/',\
#        'http://c.biancheng.net/golang/']
# #默认排序
# print(sorted(chars))
# #自定义按照字符串长度排序
# print(sorted(chars,key=lambda x:len(x)))

# Python 函数和lambda 表达式
# n=0
# for c in "http://c.biancheng.net/python/":
#     print(c, sep='', end='')
#     n = n + 1
# print(n)

# # 自定义 len() 函数
# def my_len (str):
#     length = 0
#     for c in str:
#         length += 1
#     return length

# # 函数调用
# length = my_len("http://www.baidu.com/")
# print(type(length), length)

# Python 函数的定义
# def 函数名（参数列表）:
#   // 实现特定功能的多行代码
#   [return [返回值]]

# # 定义一个空函数，没有实际意义
# def pass_dis():
#     print("空函数， 没有实际意义")
#     pass

# # 定义一个比较字符串大小的函数
# def str_max(str1, str2):
#     return str1 if str1 > str2 else str2

# # Python 函数的调用
# pass_dis()
# strmax = str_max("http://baidu.com", "http://github.com")
# print(strmax)

# 为函数提供说明文档

# # 定义一个比较字符串大小的函数
# def str_max(str1, str2):
#     '''
#     比较2 个字符串的大小
#     '''
#     return str1 if str1 > str2 else str2

# print(type(str_max), str_max, str_max.__doc__)
# print(help(str_max))

# Python 函数值传递和引用传递（包括形式参数和实际参数的区别）
# 函数声明定义传递的参数即为形式参数，函数调用时传递的参数即为实际参数；
# 值传递： 适用于实参类型为不可变类型（字符串、数字、元组）
# 引用（地址）传递： 适用于实参类型为可变类型（列表、字典）
# def demo(obj) :
#     obj += obj
#     print("形参值为：",obj)
# print("-------值传递-----")
# a = "C语言中文网"
# print("a的值为：",a)
# demo(a)
# print("实参值为：",a)
# print("-----引用传递-----")
# a = [1,2,3]
# print("a的值为：",a)
# demo(a)
# print("实参值为：",a)    

# # 什么是位置参数， Python 位置参数
# def girth(width , height):
#     return 2 * (width + height)
# #调用函数时，必须传递 2 个参数，否则会引发错误
# print(girth(3, 2, 2))

# Python 函数关键字参数及用法
# def dis_str(str1,str2):
#     print("str1:",str1)
#     print("str2:",str2)
# #位置参数
# dis_str("http://c.biancheng.net/python/","http://c.biancheng.net/shell/")
# #关键字参数
# dis_str("http://c.biancheng.net/python/",str2="http://c.biancheng.net/shell/")
# dis_str(str2="http://c.biancheng.net/python/",str1="http://c.biancheng.net/shell/")

# # 位置参数必须放在关键字参数之前，下面代码错误
# dis_str(str1="http://c.biancheng.net/python/","http://c.biancheng.net/shell/") # SyntaxError: positional argument follows keyword argument

# # Python 函数默认参数设置
# #str1没有默认参数，str2有默认参数
# def dis_str(str1,str2 = "http://c.biancheng.net/python/"):
#     '''备注说明'''
#     print("str1:",str1)
#     print("str2:",str2)
# dis_str("http://c.biancheng.net/shell/")
# dis_str("http://c.biancheng.net/java/","http://c.biancheng.net/golang/")
# print(dis_str.__defaults__, dis_str.__doc__)

# Python None（空值）及用法
# None 常用于 assert、判断以及函数无返回值的情况
# print(type(None), None is [], None is '', None is False)

# spam = print("Hello")
# print(spam == None)

# Python return 函数返回值详解
# 返回值参数可以指定，也可以忽略不写（将返回空值None）
# def add(a, b):
#     c = a + b
#     return c
# # 函数赋值给变量
# c = add(3, 4)
# print(c)
# # 函数返回值作为其他函数的实际参数
# print(add(3, 4))

# def isGreater0(x):
#     if x > 0:
#         return True
#     else:
#         return False
# print(isGreater0(5))
# print(isGreater0(0))

# Python 变量作用域（全局变量和局部变量）
# def demo():
#     add = "http://c.biancheng.net/python/"
#     print("函数内部 add =",add)
# demo()
# print("函数外部 add =",add)

# def demo(name,add):
#     print("函数内部 name =",name)
#     print("函数内部 add =",add)
# demo("Python教程","http://c.biancheng.net/python/")
# print("函数外部 name =",name)
# print("函数外部 add =",add)

# add = "http://c.biancheng.net/shell/"
# def text():
#     print("函数体内访问：",add)
# text()
# print('函数体外访问：',add)

# 使用 global 关键字对变量进行修饰后，该变量就会变为全局变量
# def text():
#     global add
#     add= "http://c.biancheng.net/java/"
#     print("函数体内访问：",add)
# text()
# print('函数体外访问：',add)

# 获取指定作用域范围中的变量
# globals() 函数
# locals() 函数
# vars(object)

# # 全局变量
# Pyname = "Python教程"
# Pyadd = "http://c.biancheng.net/python/"
# def text():
#     #局部变量
#     Shename = "shell教程"
#     Sheadd= "http://c.biancheng.net/shell/"
#     print('函数体内 globals：', globals())
#     print('函数体内 locals：', locals())
# print('函数体外 globals：', globals())
# print('函数体外 locals：', locals())
# text()

# #全局变量
# Pyname = "Python教程"
# Pyadd = "http://c.biancheng.net/python/"
# def text():
#     #局部变量
#     Shename = "shell教程"
#     Sheadd= "http://c.biancheng.net/shell/"
#     print("函数内部的 locals:")
#     print(locals())
# text()
# print("函数外部的 locals:")
# print(locals())

# 全局变量
# locals() 返回的局部变量组成的字典，可以用来访问变量，但无法修改变量的值；
# globals() 得到一个包含所有全局变量的字典，可以访问、修改、删除、增加
# Pyname = "Python教程"
# Pyadd = "http://c.biancheng.net/python/"
# def text():
#     #局部变量
#     Shename = "shell教程"
#     Sheadd= "http://c.biancheng.net/shell/"
#     print(locals()['Shename'])
#     locals()['Shename'] = "shell入门教程"
#     print(Shename)
#     print(locals()['Shename'])
#     print(globals()['Pyname'])
#     globals()['Pyname'] = "Python入门教程"
#     print(globals()['Pyname'])
#     del globals()['Pyname']
#     print(globals())
# text()

# # 全局变量
# Pyname = "Python教程"
# Pyadd = "http://c.biancheng.net/python/"
# class Demo:
#     name = "Python 教程"
#     add = "http://c.biancheng.net/python/"
# print("有 object：")
# print(vars(Demo))
# print("无 object：")
# print(vars())

# # Python 局部函数及用法（包含 nonlocal 关键字）
# #全局函数
# def outdef ():
#     #局部函数
#     def indef():
#         print("http://c.biancheng.net/python/")
#     #调用局部函数
#     indef()
# #调用全局函数
# outdef()

# # 全局函数
# def outdef ():
#     #局部函数
#     def indef():
#         print("调用局部函数")
#     #调用局部函数
#     return indef
# #调用全局函数
# new_indef = outdef()
# # 调用全局函数中的局部函数
# new_indef()

# # 全局函数
# def outdef ():
#     name = "所在函数中定义的 name 变量"
#     #局部函数
#     def indef():
#         print(name)
#         name = "局部函数中定义的 name 变量"
#     indef()
# # 调用全局函数
# outdef()

# #全局函数
# def outdef ():
#     name = "所在函数中定义的 name 变量"
#     #局部函数
#     def indef():
#         nonlocal name
#         print(name)
#         #修改name变量的值
#         name = "局部函数中定义的 name 变量"
#     indef()
# #调用全局函数
# outdef()

# 什么是闭包， Python 闭包
# 闭包区别于嵌套函数，闭包中外部函数返回的不是一个具体的值，而是一个函数
# 闭包函数，其中 exponent 称为自由变量
# def nth_power(exponent):
#     def exponent_of(base):
#         return base ** exponent
#     return exponent_of

# square = nth_power(2)
# cube = nth_power(3)

# print(square(2))
# print(cube(2))

# # Python 闭包的 __closure__ 属性
# def nth_power(exponent):
#     def exponent_of(base):
#         return base ** exponent
#     return exponent_of
# square = nth_power(2)
# #查看 __closure__ 的值
# print(type(square.__closure__), square.__closure__)
# print(dir(square.__closure__))

# Python lambda 表达式（匿名函数）及用法
# lambda 表达式，又称匿名函数，常用来表示内部仅包含1行表达式的函数；
# 如果一个函数的函数体仅有一行表达式，则该函数就可以用lambda 表达式来代替；
# def add(x, y):
#     return x+ y
# print(add(3,4))

# add = lambda x,y:x+y
# print(add(3, 4))
# 相比函数， lambda 表达式具有以下2个优势：
# 对于单行行数， 使用lambda 表达式可以省去定义函数的过程，让代码更加简洁；
# 对于不需要多次复用的函数，使用 lambda 表达式可以在用完之后立即释放，提高程序执行的性能

# Python eval() 和 exec() 函数详解
# eval() 和 exec() 函数的功能是相似的，都可以执行一个字符串形式的Python代码，相当于一个 Python 的解释器；
# 两者不同之处在于， eval() 执行完要返回结果， exec() 执行完不反悔结果；
# dic={} #定义一个字
# dic['b'] = 3 #在 dic 中加一条元素，key 为 b
# print (dic.keys()) #先将 dic 的 key 打印出来，有一个元素 b
# dic['a'] = 4
# exec("c = 5", dic) #在 exec 执行的语句后面跟一个作用域 dic
# print(dic.keys()) #exec 后，dic 的 key 多了一个
# print(dic['__builtins__'])

# print('-----------------------------------')
# print(globals()['__builtins__'])

# a=10
# b=20
# c=30
# g={'a':6, 'b':8} #定义一个字典
# t={'b':100, 'c':10} #定义一个字典

# evalL = eval('a+b+c', g, t)
# print(type(evalL), evalL) #定义一个字典 116
# print(a, b, c)

# a = 1
# exec("a = 2") #相当于直接执行 a=2
# print(a)
# a = exec("2+3") #相当于直接执行 2+3，但是并没有返回值，a 应为 None
# print(a)
# a = eval('2+3') #执行 2+3，并把结果返回给 a
# print(a)

# exec() 中最适合放置运行后没有结果的语句， 而 eval() 中适合放置有结果返回的语句；

# Python 类和对象
# 什么是面向对象， Python 面向对象（一切皆对象）
# class Person:
#     name = 'xxxx'
#     def __init__(self, name):
#         self.name = name

# zhangsan = Person('zs')
# print(zhangsan.name)
# lisi = Person('ls')
# print(lisi.name)

# try:
#     a = int(input("输入被除数："))
#     b = int(input("输入除数："))
#     c = a / b
#     print("您输入的两个数相除的结果是：", c )
# except Exception as e:
#     print(e.args)
#     print(str(e))
#     print(repr(e))
#     print("未知异常")
# print("程序继续运行")

# import hello as h
# print(dir(h), h.say())

# from hello import say as s
# s()
# print()
