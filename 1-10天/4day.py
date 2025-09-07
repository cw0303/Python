
#分支结构
# TODO: ---------------- Section 1 ----------------
#使用if和else构造分支结构
# 构造分支结构最常用的是if、elif和else三个关键字
# 举例 ：身体质量指数（BMI）的计算器


weight = float(input("请您输入您的体重,单位KG: "))  # 输入体重
height = float(input("请您输入您的身高,单位M: "))  # 输入身高
BMI = weight / (height * height)
if BMI < 18.5:
    print("您的体重过轻")
elif 18.5 <= BMI < 24:
    print("您的体重正常")
elif 24 <= BMI < 28:
    print("您的体重过重")
else:
    print("您的体重肥胖")
print("您的BMI指数为: %.1f" % BMI)  # 输出BMI指数，保留两位小数









# TODO: ---------------- Section 2 ----------------
#使用match和case构造分支结构,此处暂时无法运行
"""
Python 3.10版本引入了match-case语句，类似于其他编程语言中的switch-case语句
http_status_code = int(input("请输入HTTP状态码: "))
match http_status_code:
    case 200:
        print("请求成功")
    case 301:
        print("永久重定向")
    case 302:
        print("临时重定向")
    case 400:
        print("请求错误")
    case 401:
        print("未授权")
    case 403:
        print("禁止访问")
    case 404:
        print("未找到")
    case 500:
        print("服务器错误")
    case 502:
        print("网关错误")
    case 503:
        print("服务不可用")
    case _:
        print("未知状态码")
"""


# TODO: ---------------- Section 3 ----------------
#分支结构的应用
#例子1：分段函数求值
#输入x,若x>1,则y=3x-5;若-1<=x<=1,则y=x+2;若x<-1,则y=5x+3
x = float(input("请输入一个实数x: "))
if x>1:
    y = 3 * x - 5
elif -1 <= x <= 1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'{y = }')  # 输出y的值，保留两位小数








# TODO: ---------------- Section 4 ----------------
#例子2：百分制成绩转换成等级
#要求：1.如果输入的成绩在90分以上（含90分），则输出A；
#      2.输入的成绩在80分到90分之间（不含90分），则输出B；
#      3.输入的成绩在70分到80分之间（不含80分），则输出C；
#      4.输入的成绩在60分到70分之间（不含70分），则输出D；
#      5.输入的成绩在60分以下，则输出E

score = float(input('请输入您的学习成绩(百分制):  ')) # 输入成绩
if score >= 90:
    grade = 'A'
elif  90>score>=80:
    grade = 'B'
elif  80>score>=70:
    grade = 'C'
elif  70>score>=60:
    grade = 'D'
else:
    grade = 'E'
print('您的等级是:'f"{grade = }",'您的成绩是:'f'{score = }')  # 输出成绩和等级




# TODO: ---------------- Section 5 ----------------
#例子3：计算三角形的周长和面积。
#要求：输入三条边的长度，如果能构成三角形就计算周长和面积；否则给出“不能构成三角形”的提示。
a = float(input("请输入三角形的第一条边长: "))  # 输入第一条边长
b = float(input("请输入三角形的第二条边长: "))  # 输入第二条边长
c = float(input("请输入三角形的第三条边长: "))  # 输入第三条边长
if a + b > c and a +c > b and b + c > a:  # 判断能否构成三角形
    perimeter = a + b + c  # 计算周长
    s = perimeter / 2  # 计算半周长
    area = (s*(s-a)*(s-b)*(s-c))**0.5  # 计算面积，海伦公式
    print('三角形的周长是:'f"{perimeter:.1f}") # 输出周长 
    print(f'三角形的面积为: {area:.2f}')  # 输出面积，保留两位小数
else:
    print("不能构成三角形")




