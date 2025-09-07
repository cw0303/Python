#Python语言中的运算符




# TODO: ---------------- Section 1 ----------------

# ? 算术运算符
# [] 索引、[:]切片,如果s='hello',s[0]='h',s[1:3]='el'
# ** 幂运算,如2**3=8
# ~ 取反,如~2=-3,~3=-4
# + 字符串连接,如'hello' + ' ' + 'world' = 'hello world'
# - 负号,如-2=-2
# * 乘法,如2*3=6,'hello'*3='hellohellohello'
# / 除法,如6/3=2.0
# % 取模,返回除法的余数,如7%3=1
# // 取整除向下取整,如7//3=2,-7//3=-3
# >> 右移,如8>>2=2
# << 左移,如2<<2=8
# & 按位与,如5&3=1
# | 按位或,如5|3=7
# ^ 按位异或,如5^3=6
# <=  小于等于
# >=  大于等于
# <   小于
# >   大于
# ==  等于
# !=  不等于
# and 逻辑与
# or  逻辑或
# not 逻辑非
# =  赋值
# +=  加等于
# -=  减等于
# *=  乘等于
# /=  除等于
# //= 取整除等于
# %=  取模等于
# **= 幂等于
# &=  按位与等于
# |=  按位或等于
# ^=  按位异或等于
# >>= 右移等于
# <<= 左移等于
# in 成员运算符,如'a' in 'abc' = True
# not in 非成员运算符,如'a' not in 'abc' = False
# is 身份运算符,如a is b = True
# is not 非身份运算符,如a is not b = False






# TODO: ---------------- Section 2 ----------------

a = 10
b = 3
a += b  # a = a + b
print(a)  # 13
a *= a + b  # a = a * (a + b)
print(a)  # 13 * (13 + 3) = 208










# TODO: ---------------- Section 3 ----------------

print(a := 100)  # 100,等同于a = 100,然后返回a的值
print(a)
# 海象运算符只能在Python 3.8及以上版本使用





# TODO: ---------------- Section 4 ----------------


"""
比较运算符和逻辑运算符的使用
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print('flag0 =', flag0)     # flag0 = True
print('flag1 =', flag1)     # flag1 = True
print('flag2 =', flag2)     # flag2 = False
print('flag3 =', flag3)     # flag3 = False
print('flag4 =', flag4)     # flag4 = True
print('flag5 =', flag5)     # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)      # False





# TODO: ---------------- Section 5 ----------------
# 运算符和表达式应用 例子1：华氏温度转摄氏温度
#要求：输入华氏温度将其转换为摄氏温度，华氏温度到摄氏温度的转换公式为：C = 5/9 * (F - 32)

Fahrenheit = float(input('请输入华氏摄氏度: ') )  # 输入华氏温度
Celsius = (Fahrenheit - 32) * 5 / 9  # 转换为摄氏温度
print('%.1f 华氏度 = %.1f 摄氏度' % (Fahrenheit, Celsius))  # 输出摄氏温度
print(f'{Fahrenheit:.1f} 华氏度度 = {Celsius:.1f} 摄氏度度')  # 输出摄氏温度

# ​​'%.1f华氏度 = %.1f摄氏度'​​：这是一个​​字符串模板​​，包含了文本和两个“占位符”。
# %.1f就是一个占位符，它告诉 Python：“这里稍后要放一个浮点数（小数）。”
# %是格式化操作的开始。
# .1表示保留​​1位小数​​。
# f表示这是一个​​浮点数（float）​​。
# 华氏度和 摄氏度是普通的文本。
# % (f, c)​​：这部分是​​将变量值填充到占位符​​的操作
# %是字符串格式化操作符。
# (f, c)是一个元组，包含了要填充的两个变量。它们的​​顺序非常重要​​：第一个变量 f会替换第一个 %.1f，第二个变量 c会替换第二个 %.1f。
# 所以，这行代码的整体意思是：​​打印一句话，其中两个小数点位分别用变量 f和 c的值替换，并且都只保留一位小数

# TODO: ---------------- Section 6 ----------------
# 占位符 %s ,"%s" % "Hello" = "Hello" #字符串
# 占位符 %d ,"%d" % 100 = 100 #十进制整数
# 占位符 %f ,"%f" % 3.14 = 3.140000 #浮点数
# 占位符 %.nf ,"%.2f" % 3.14159 = 3.14 #浮点数，保留n位小数
# 占位符 %x ,"%x" % 255 = ff #十六进制整数
# 占位符 %o ,"%o" % 8 = 10 #八进制整数
# 占位符 %% ,"%%" % () = % #百分号

# TODO: ---------------- Section 7 ----------------
#例子2：计算圆的周长和面积

radius = float(input('请输入圆的半径: '))  # 输入圆的半径
perimeter = 2 * 3.14 * radius  # 计算圆的周长
area = 3.14 * radius * radius  # 计算圆的面积
print('半径等于: %.3f 时' % radius, ',圆的周长是: %.3f' % perimeter, ',此时圆的面积是: %.3f.' % area)  # 输出圆的周长和面积

print(f'半径静等于:{radius: .3f}时, 圆的周长长是:{perimeter: .3f}, 此时圆的面积鸡是:{area: .3f}.')  # 输出圆的周长和面积


# TODO: ---------------- Section 8 ----------------
#例子3：判断闰年
try:
    input_year = int(input('亲爱的用户,请输入一个任意年份: '))
    is_leap_year = (input_year % 4 ==0 and input_year % 100 !=0) or (input_year % 400 ==0)
    if is_leap_year == True:
        print(f'{input_year} 是闰年')
    else:
        print(f'{input_year} 不是闰年')
except ValueError:
    print('输入错误,请输入一个整数年份,如2024')