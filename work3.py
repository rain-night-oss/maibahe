"""
试编程实现分两行输入两个非零整数，并在4 行中按顺序输出两个数的加、减、乘、除的计算结果。
要求输出与如下示例格式相同，符号前后各有一个空格。
"""
#输入整数变量a和b，定义输入函数
##############Begin##################
a = int(input())
b = int(input())
##############End####################

#a和b之间进行四则运算并输出
##############Begin##################
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
##############End####################

'''
试编程实现分两行输入两个非零浮点数，并在4 行中按顺序输出两个数的加、减、乘、除的计算式和计算结果。
计算结果str.format()方法保留小数点后3位数字。要求输出与如下示例格式相同，符号前后各有一个空格。
'''
#输入浮点型变量a和b，定义输入函数
#############Begin##############
a = float(input())
b = float(input())
#############End################

#a和b之间进行四则运算并输出
#############Begin################
print(f'{a} + {b} = {a + b:.3f}')
print(f'{a} - {b} = {a - b:.3f}')
print(f'{a} * {b} = {a * b:.3f}')
print(f'{a} / {b} = {a / b:.3f}')
#############End################

'''
完善一个根据用户输入的数值和符号进行四则运算的小程序。
'''
a = int(input('请输入一个整数：'))    
b = int(input('请再输入一个整数：')) 
sign = input('请输入运算符号')
# 补充你的代码
# eval()函数把字符串f"{a}{sign}{b}"转为计算表达式
# 字符串里包含引号时，内部引号与边界应用不同的引号
print(f'{a}{sign}{b}={eval(f"{a}{sign}{b}")}')

'''
完善一个能随机出题进行四则运算的小程序。
'''
import random
random.seed(0)  # 随机数种子，用于评测，请不要修改
# 在注释语句后面补充合适的代码，使程序能完成预期的功能
def calculator(n, maximum):
    """随机产生n道正整数四则运算的题目,用户输入计算结果，
    判断输入正确与否,并统计正确率。题目保证减法不出现负数."""
    correct = 0
    for i in range(n):  # 循环n次，每次产生一个新问题
        b = random.randint(0, maximum)  # 随机产生一个maximum以内整数
        a = random.randint(b, maximum)  # 随机产生一个b到maximum以内整数，避免减法出现负数
        sign = random.choice('+-*/')    # 随机获取一个运算符号
        # 先输出一个格式化的计算表达式并保持光标不换到下一行，类似5+10=
        print(f'{a}{sign}{b}=', end='')
        # 接受用户输入的一个浮点数，并转换为浮点类型
        result = float(input())
        # 如果计算结果正确，输出'恭喜你，回答正确'并统计答对的次数，注意满足条件时执行的语句要缩进
        if result == eval(f"{a}{sign}{b}"):
            print('恭喜你，回答正确')
            correct = correct + 1

        # 否则输出'回答错误，你要加油哦！'
        else:
            print('回答错误，你要加油哦！')
            
    # 以下语句不要修改
    print(f'答对{correct}题，正确率为{correct / n * 100}%')


# 以下语句不要修改
if __name__ == '__main__':
    num = int(input('请输入出题数量：'))
    m = int(input('请输入参与计算的最大数字：'))
    calculator(num, m)  # 调用函数完成计算

"""
编写程序，用户入自己的姓名，输出以下界面后，再在下一行输出“欢迎您，***同学！”
|++++++++++++++++++++++|
|                      |
|   Welcome to WHUT    |
|                      |
|++++++++++++++++++++++|
"""
my_name = input()  # 输入学生的姓名                             
########### Begin ############
# 输出以上界面
print('|++++++++++++++++++++++|')
print('|                      |')
print('|   Welcome to WHUT    |')
print('|                      |')
print('|++++++++++++++++++++++|')
# 输出“欢迎您，***同学！”
print(f"欢迎您，{my_name}同学！")
########### End ############

'''
# 在三行中分别输入当前的年、月、日的整数值，按要求完成输出。
# 1 输出年月日，空格分隔，格式：2020 09 16
# 2 输出年-月-日，连字符“-”分隔，格式：2020-09-16
# 3 输出年/月/日，斜线“/”分隔，格式：2020/09/16
# 4 输出月，日，年，逗号“,”分隔，格式：09,16,2020
# 5 用str.format()格式输出，格式：2020 年09 月16 日
# 6 用字符串拼接方法输出，格式：2020 年09 月16 日
'''
year = input()                         # 输入当前年
month = input()                        # 输入当前月
date = input()                         # 输入当前日
# =======================================================
print(year,month,date)
print(year,month,date,sep='-')
print(year,month,date,sep='/')
print(month,date,year,sep=',')
print('{}年{}月{}日'.format(year,month,date))
print(year+"年"+month+"月"+date+"日")

'''
用户通过键盘输入一个字符串，将这个字符串转为可计算对象，再将转换结果乘3后输出到显示器上。
'''
s = input()
print(eval(s) * 3)

'''
用户输入一个整数m，表示替换域的浮点数输出时保留m位小数。按输入的精度输出保留m位小数的圆周率的值
'''
pi = 3.14159265358979
m = int(input())
print(f'圆周率值为：{pi:.{m}f}')

'''
提示用户输入他们的姓名、年龄和身高，然后格式化并输出这些信息。
'''
name = input("请输入您的姓名：")
age = int(input("请输入您的年龄："))
height = float(input("请输入您的身高（米）："))
# 按格式输出信息
print(f"姓名：{name}")
print(f"年龄：{age} 岁")
print(f"身高：{height} 米")

'''
模拟一个游戏中的对话场景。程序将提示用户输入角色的名字、等级和金币数量，然后格式化并输出这些信息，模拟游戏对话的效果。
'''
name = input("请输入角色的名字：")
grade = int(input("请输入角色的等级："))
num = int(input("请输入角色拥有的金币数量："))
print(f"欢迎, 勇敢的 {name}!")
print(f"你现在的等级是 {grade} 级。")
print(f"你拥有 {num} 个金币。")
print(f"{name}，继续你的冒险吧！")

'''
提示用户输入股票的买入价格、卖出价格和持有的股票数量，然后计算并输出总收益。
'''
a = float(input("请输入股票的买入价格（每股）："))
b = float(input("请输入股票的卖出价格（每股）："))
c = int(input("请输入持有的股票数量："))
s = (b-a)*c
print(f"总收益为：{s:.2f} 元")

'''
编写一个简单的BMI计算器，程序将提示用户输入体重（公斤）和身高（米），然后计算并输出BMI值，并根据BMI值给出健康建议。
'''
weight = float(input("请输入您的体重（公斤）："))
height = float(input("请输入您的身高（米）："))
bmi = weight / (height ** 2) 
print(f"您的BMI值为：{bmi:.2f}") 
if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 24.9:
    print("体重正常")
elif 25 <= bmi < 29.9:
    print("体重超重")
else:
    print("肥胖")

'''
数学运算综合训练
'''
a = 8
b = 9
print(a+b)

a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = int(input('请输入第一个整数：')) 
b = int(input('请输入第二个整数：'))
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} % {b} = {a % b}')
print(f'{a} ** {b} = {a ** b}')

a = float(input('请输入第一个浮点数：'))
b = float(input('请输入第二个浮点数：'))
print(f'{a} + {b} = {a + b:.2f}')
print(f'{a} - {b} = {a - b:.2f}')
print(f'{a} * {b} = {a * b:.2f}')
print(f'{a} / {b} = {a / b:.2f}')

expression = input()
result = eval(expression)
print(f'{result:.3f}')

'''
同一行输出
'''
end_mark = input()
for poet in ['李白', '王维', '王勃', '白居易', '杜甫']:
    print(poet, end=end_mark)

#问好
user_name = input()
print(user_name,'你好！')
print(user_name,'，你好！')

user_name = input() 
print('{}你好！'.format(user_name))
print('{}，你好！'.format(user_name))

user_name = input() 
sign = input()
print(user_name, '你好！', sep=sign)

'''
控制小数输出精度
'''
x = float(input())
print('{:.3f}'.format(x))

'''
计算矩形面积
'''
longth = eval(input())
width = eval(input())
print(longth * width)

'''
简单数学运算
'''
def solve(a,b):
    # 在此处输入你的代码
    print(a + b)
    print(a - b)
    print(a * b)

if __name__ == '__main__':
    a = int(input())  # 输入转为整数
    b = int(input())  # 输入转为整数
    solve(a,b)        # 调用你定义的函数进行数学运算

#浮点数四则运算与格式化输出
a = float(input())
b = float(input())
print('{} + {} = {:.3f}'.format(a,b,a + b))
print('{} - {} = {:.3f}'.format(a,b,a - b))
print('{} * {} = {:.3f}'.format(a,b,a * b))
print('{} / {} = {:.3f}'.format(a,b,a / b))

#时间计算
hour = int(input())
minute = int(input())
second = int(input())
print(f'{hour:02}:{minute:02}:{second:02}')
print(f'距离午夜还剩余{86400 - hour * 3600 - minute * 60 -second}秒')

#地球数据计算
import math
radius = 6371 * 1000
# 1. 计算地球表面积（表面积公式S = 4πR2）
surface_area = 4 * math.pi * pow(radius,2)
print(f'地球表面积为{surface_area:.2f}平方米')
# 2. 计算地球体积（体积公式是V = 4πR3/3）
volume = 4 * math.pi * pow(radius,2) * radius / 3
print(f'地球体积为{volume:.2f}立方米')
# 3. 计算地球赤道的周长（圆周长公式是L = 2πR）
circumference = 2 * math.pi * radius
print(f'地球赤道周长为{circumference:.2f}米')
# 4.计算绳子与地球之间的空隙大小
new_radius = (circumference + 1) / (2 * math.pi) - radius
print(f'空隙大小为{new_radius:.2f}米')
# 5.判断老鼠是否可以从空隙中钻过
if(new_radius > 0.1):
    print('老鼠可以从空隙中钻过')
    
else:
    print('老鼠无法通过空隙')
    
#计算弓形面积
import math
AB = float(input())
CD = float(input())
AD = AB / 2
OA = (pow(AD,2) + pow(CD,2)) / (2 * CD)
AOB = 2 * math.asin(AD/OA)
sector = AOB / (2 * math.pi) * math.pi * pow(OA,2)
triangle = 1/2 * pow(OA,2) * math.sin(AOB)
arch = sector - triangle
print(f'{arch:.2f}')

#计算圆的面积
AB = float(input())
CD = float(input())
AD = AB/2
OA = (pow(AD,2) + pow(CD,2))/(2 * CD)
print(f'{OA:.2f}')

#助学贷款
tuition_per_credit = eval(input('请输入每学分学费金额：'))
living_expenses = eval(input('请输入你每个月生活费：'))
python = 3
math = 4
english = 4
pe = 2
military = 2
philosophy = 2
credits = (python + math + english + pe + military + philosophy)
total_tuition = credits * tuition_per_credit
total_cost = living_expenses * 5 + total_tuition
student_loan = total_cost * 0.6
print(f'本学期你能够贷款{student_loan:.2f}元')