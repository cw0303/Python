
# TODO: ---------------- Section 1 ----------------
# 循环结构 for 循环 和 while 循环
"""
import time

for i in range(5):
    print(i)
    time.sleep(1)  # 暂停1秒


for i in range(5):
    print('Teeming is a good')
    time.sleep(1)  # 暂停1秒

# range(5) 生成的序列是从0开始，到5结束，但不包括5，即0,1,2,3,4
# range(36) 生成的序列是从0开始，到36结束，但不包括36，即0,1,2,...,34,35
# range(1, 10) 生成的序列是从1开始，到10结束，但不包括10，即1,2,3,4,5,6,7,8,9
# range(1, 10, 2) 生成的序列是从1开始，到10结束，但不包括10，步长为2，即1,3,5,7,9
# range(10, 1, -2) 生成的序列是从10开始，到1结束，但不包括1，步长为-2，即10,8,6,4,2

#代码变量名未用到i,可用_代替
for _ in range(5):
    print("Hello, World!")
    time.sleep(1)  # 暂停1秒




# TODO: ---------------- Section 2 ----------------
#例子 使用for循环打印1-100的整数
for _ in range(1,101):
    print(_,end='')

 
#例子 使用for循环打印1-100的求和

sum = 0
for _ in range(1,101):
    sum += _
print(int(sum))
#此处print不受for循环影响,因为for循环没有缩进

sum = 0
for _ in range(1,101):
    sum += _
    print(int(sum))
#此处print受for循环影响,因为for循环有缩进,每次循环都会打印当前的sum值






# TODO: ---------------- Section 3 ----------------

sum = 0
for _ in range(1,100,2):
    sum += _
print(int(sum))


#更简单的求和是python的内置sum函数
sum = sum(range(1,100,2))
print(int(sum))








# TODO: ---------------- Section 4 ----------------
#while循环 不确定循环次数推荐使用while
#例子 使用while循环打印1-100的整数 并且求和
i = 1
sum = 0
while i<=100:
    print(i)
    i += 1 # i = i + 1
    sum += i
print(sum)
#此处print不受while循环影响,因为while循环没有缩进




# TODO: ---------------- Section 5 ----------------
#break 
i = 1
sum = 0
while i<=10000:
    i += 1 # i = i + 1
    sum += i
    if sum > 10000:
        break
print(sum)
print(i)




#continue 跳过某次循环
a = 0
for i in range(1,101):
    if i % 2 ==0:
        continue
    a += i
print(a)



# TODO: ---------------- Section 6 ----------------


#嵌套的循环结构
#打印乘法口诀
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}x{j}={i*j}',end='\t')
    print()  # 每打印完一行，换行

# TODO: ---------------- Section 6 ----------------
#循环结构的应用
#例子1：判断素数,输入一个大于1的正整数判断它是不是素数
a = input('请输入一个大于1的正整数:')
a = int(a)  # 将输入的字符串转换为整数
is_prime = True  # 假设是素数
for i in range(2,a):  # 从2开始到a-1
    if a % i == 0:  # 如果a能被i整除
        is_prime = False  # 不是素数
        break  # 跳出循环 
if is_prime == True:
    print(f'{a}是素数')
else:
    print(f'{a}不是素数')





#例子2：最大公约数
#要求：输入两个大于 0 的正整数，求两个数的最大公约数。
x = input('请输入第一个大于0的正整数:')
y = input('请输入第二个大于0的正整数:')
x = int(x)
y = int(y)
while y != 0:
    x, y = y, x % y  # 辗转相除法
    # 交换x和y的值
    # x = y
    # y = x % y
    # 直到y为0时，x就是最大公约数
print(f'最大公约数是{x}')

"""
#例子3：猜数字游戏
#要求：计算机出一个 1 到 100 之间的随机数
# 玩家输入自己猜的数字，计算机给出对应的提示信息“大一点”、“小一点”或“猜对了”，如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
import random

answer = random.randint(1,101)  # 生成1到100之间的随机整数
count = 0  # 记录猜的次数

while True:
    count += 1  # 猜的次数加1
    guess_number = input('请输入你猜的数字(1-100):')
    guess_number = int(guess_number)# 将输入的字符串转换为整数
    if guess_number < answer:
        print('大一点')
    elif guess_number > answer:
        print('小一点')
    else:
        print(f'恭喜你，猜对了！你一共猜了{count}次')
        break  # 猜对了，跳出循环

