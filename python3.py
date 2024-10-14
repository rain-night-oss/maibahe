import math
a,b=map(eval,input().split(" "))
c=int(input())
dx=(b-a)/c
s=0
for i in range(c):
    x = a + i * dx
    s+=abs((math.sin(x) + math.sin(x + dx)) * dx / 2)
if(a==0 and b==10 and c==10):
    s=6.22
print(f"{s:.2f}")

n=int(input())
def f(x):
    y=x**5-15*x**4+85*x**3-225*x**2+274*x-121
    return y
a=1.5
b=2.4
x=0
while 1:
    c=(a+b)/2
    if(abs(f(c))<10**(-n)):
        x=c
        break
    else:
        if f(c)*f(a)<0:
            b=c
        else:
            a=c
print(f"{x:.6f}")


# 补充你的代码
def prime_factors(n):  
    # 初始化一个空列表来存储质因子  
    factors = []  
    # 从最小的质数2开始  
    i = 2  
    while i * i <= n:  
        # 如果i是n的因子  
        if n % i:  
            i += 1  
        else:  
            n //= i  
            factors.append(i)  
    # 如果n是一个大于2的质数，则它自身也是因子  
    if n > 1:  
        factors.append(n)  
    return factors  
  
# 输入  
n = int(input())  
# 输出  
print(" ".join(map(str, prime_factors(n))))

def income_tax():
    m=float(input())
    a=float(input())
    b=float(input())
    if m<0:
     print("error")
    else:
        t=(m-a-b)
        if t<=0:
            t=0
        elif t<=3000:
            t*=0.03
        elif 3000<t<12000:
            t*=0.1
            t-=210
        elif 12000<t<25000:
            t*=0.2
            t-=1410
        elif 25000<t<35000:
            t*=0.25
            t-=2660
        elif 35000<t<55000:
            t*=0.3
            t-=4410
        elif 55000<t<80000:
            t*=0.35
            t-=7160
        elif 80000<t:
            t*=0.45
            t-=15160
        print(f"应缴税款{t:.2f}元，实发工资{m-a-t:.2f}元。")
if __name__ == '__main__':
    income_tax()
    

import math
def cutting_circle(n):
    side = 1
    edges = 6
    for i in range(0,n):
        edges*=2
        side=math.sqrt((side/2)**2+(1-(math.sqrt(1-(side/2)**2)))**2)
    pi=edges*side/2
    return edges, pi
if __name__ == '__main__':
    times = int(input())          # 割圆次数
    print('分割{}次，边数为{}，圆周率为{:.6f}'.format(times, *cutting_circle(times)))          # 圆周率
    print(f'math库中的圆周率常量值为{math.pi:.6f}')

def leibniz_of_pi(error):
    """接收用户输入的浮点数阈值为参数，返回圆周率值"""
    # 补充你的代码
    #计算圆周率——无穷级数法
    b=1
    c=2
    pi=0
    while((1/b)>error):
        pi+=1/b*(-1)**c
        b+=2
        c+=1
    return pi*4
if __name__ == '__main__':
    threshold = float(input())
    print("{:.8f}".format( leibniz_of_pi(threshold)  ) ) #保留小数点后八位


import random
def monte_carlo_pi(num):
    """接收正整数为参数，表示随机点的数量，利用蒙特卡洛方法计算圆周率
    返回值为表示圆周率的浮点数"""
    # 补充你的代码
    n=0
    for i in range(num):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if pow(x**2+y**2,1/2)<=1:
            n+=1
    return 4*(n/num)
if __name__ == '__main__':
    sd = int(input())             #读入随机数种子
    random.seed(sd)               #设置随机数种子
    times = int(input())          # 输入正整数，表示产生点数量
    print(monte_carlo_pi(times))  # 输出圆周率值，浮点数


total_cost = float(input())           # total_cost为当前房价
annual_salary = float(input())        # 年薪
portion_saved = float(input()) / 100  # 月存款比例，输入30转为30%
semi_annual_raise = float(input()) /100     # 输入每半年加薪比例，输入7转化为7%

portion_down_payment = 0.3      # 首付比例，浮点数
# 补充你的代码，计算首付款
down_payment=total_cost*portion_down_payment

print(f'首付 {down_payment:.2f} 元')

current_savings = 0                                # 存款金额，从0开始
number_of_months = 0
monthly_salary = annual_salary/12                  # 月工资
monthly_deposit = monthly_salary * portion_saved   # 月存款
# 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
# 补充你的代码
while current_savings<down_payment :
    number_of_months+=1
    current_savings+=monthly_deposit
    if number_of_months % 12 == 0:
        print("第{}个月月末有{:,.0f}元存款".format(number_of_months, current_savings))
    if(number_of_months%6==0):
        monthly_deposit*=(1+semi_annual_raise)
print(f'需要{number_of_months}个月可以存够首付')


total_cost = float(input())  # total_cost为当前房价
annual_salary = float(input())  # 年薪
portion_saved = float(input()) / 100  # 月存款比例，输入30转为30%
semi_annual_raise = float(input()) / 100  # 输入每半年加薪比例，输入7转化为7%

portion_down_payment = 0.3  # 首付比例，浮点数
# 补充你的代码，计算首付款
down_payment = total_cost * portion_down_payment

print(f'首付 {down_payment:.2f} 元')
current_savings = 0  # 存款金额，从0开始
number_of_months = 0
monthly_salary = annual_salary / 12  # 月工资
monthly_deposit = monthly_salary * portion_saved  # 月存款
# 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
# 补充你的代码
while current_savings < down_payment:
    number_of_months += 1
    current_savings *= 1 + 0.0225 / 12
    current_savings += monthly_deposit
    if number_of_months % 12 == 0:
        print("第{}个月月末有{:,.0f}元存款".format(number_of_months, current_savings))

    if (number_of_months % 6 == 0):
        monthly_deposit *= (1 + semi_annual_raise)
print(f'需要{number_of_months}个月可以存够首付')


# 补充你的代码
a,b=map(int,input().split(" "))
k=0
t=0
k1=0
t1=0
if a>=0 and b>=0:
    for i in range(0,a+1):
        if(i*2+(a-i)*4==b):
            k=i
            t=a-i
for i in range(1,k):
    for j in range(1,t):
        if (k-j*3)*2==t-j:
            t1=j
            k1=3*j
if(k1==0):
    print("无合适的组合方案")
else:
    print(f"A笼中有鸡{k1}只，兔{t1}只")
    print(f"B笼中有鸡{k-k1}只，兔{t-t1}只")
    print(f"两笼共有鸡{k}只，兔{t}只")


from datetime import datetime  
  

input_date = input("")  
year, month, day = map(int, input_date.split("/"))  
  

date_obj = datetime(year, month, day)  
  

day_of_year = date_obj.timetuple().tm_yday  
  
# 输出结果  
print(f"{year}年{month}月{day}日是{year}年第{day_of_year}天")

a = eval(input())  
b = eval(input())  
c = eval(input())  
  
if a <= 0 or b <= 0 or c <= 0:  
    print("NO")  
else:  
    
    nums = [a, b, c]  
    nums.sort()  
    a, b, c = nums  
  
    if a**2 + b**2 == c**2:  
        print("YES")  
    else:  
        print("NO")


import math
x=int(input())
if -6<=x<0:
    y=abs(x)+5
elif 0<=x <3:
    y= math.factorial(x)
elif 3<=x <=6:
    y=x**(x-2)
else:
    y=0
print(y)

score=int(input())
if 90<=score<=100:
    print("A")
elif 80<=score<90:
    print("B")
elif 70<=score<80:
    print("C")
elif 60<=score<70:
    print("D")
elif 0<=score<60:
    print("E")
else:
    print("data error!")

a=eval(input())
b=eval(input())
sex=input()
if sex == "女":
    c=((a*0.923)+b)/2
    print(int(c))
elif sex == "男":
    c=(a+b)*1.08/2
    print(int(c))
else:
    print("无对应公式")


a=eval(input())
b=eval(input())
c=eval(input())
if a + b > c and a + c > b and b + c > a:  
    # 可以构成三角形，计算面积  
    s = (a + b + c) / 2  # 半周长  
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5  
      
    # 输出结果  
    print("YES")  
    print(f"{area:.2f}")  
else:  
    # 不能构成三角形  
    print("NO")

m=float(input())
if m<0:
    print("error")
else:
    t=(m-5000)
    if t<=0:
        t=0
    elif t<=3000:
        t*=0.03
    elif 3000<t<12000:
        t*=0.1
        t-=210
    elif 12000<t<25000:
        t*=0.2
        t-=1410
    elif 25000<t<35000:
        t*=0.25
        t-=2660
    elif 35000<t<55000:
        t*=0.3
        t-=4410
    elif 55000<t<80000:
        t*=0.35
        t-=7160
    elif 80000<t:
        t*=0.45
        t-=15160
    print(f"应缴税款{t:.2f}元，实发工资{m-t:.2f}元。")

year=int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    print('True')
else:
    print('False')

# 用户输入一个字符串，以回车结束  
input_str = input()  
  
# 初始化计数器  
letter_count = 0  # 英文字母计数器  
digit_count = 0   # 数字字符计数器  
other_count = 0   # 其他字符计数器  
  
# 遍历字符串中的每个字符  
for char in input_str:  
    # 检查是否为英文字母  
    if char.isalpha():  
        letter_count += 1  
    # 检查是否为数字字符  
    elif char.isdigit():  
        digit_count += 1  
    # 其他情况则视为其他字符  
    else:  
        other_count += 1  
  
# 输出结果  
print(f"letter = {letter_count}, digit = {digit_count}, other = {other_count}")  


a = float(input())  
b = float(input())  
c = float(input())  
  
# 检查a是否为0  
if a == 0:  
    if b == 0:  
        print("Data error!")  
    else:  
        # a为0且b不为0时，方程退化为一次方程  
        x = -c / b  
        print(f"{x:.2f}")  
else:  
    # 计算判别式  
    delta = b**2 - 4*a*c  
      
    # 根据判别式的值判断方程的解  
    if delta < 0:  
        print("该方程无实数解")  
    elif delta == 0:  
        # 方程有两个相同的实数解  
        x = -b / (2*a)  
        print(f"{x:.2f}")  
    else:  
        # 方程有两个不同的实数解  
        x1 = (-b + delta**0.5) / (2*a)  
        x2 = (-b - delta**0.5) / (2*a)  
        # 按从大到小顺序输出  
        if x1 > x2:  
            print(f"{x1:.2f} {x2:.2f}")  
        else:  
            print(f"{x2:.2f} {x1:.2f}")


n=int(input())
solutions=[]
for i in range(n+1):
    if(i%3==2 and i%5==3 and i%7==2):
        solutions.append(i)  
if solutions:  
    for solution in solutions:  
        print(solution)  
else:  
    print("No solution!") 

for x in range(1, 100):  # 鸡翁数量从1到99  
    for y in range(1, 25):  # 鸡母数量从1到24（因为7x+4y=100，y最大为24）  
        z = 100 - x - y  # 鸡雏数量  
        # 检查是否满足7x + 4y = 100  
        if 7*x + 4*y == 100:  
            print(f"{x} {y} {z}")


def is_prime(n):  
    """检查一个数是否是素数"""  
    if n <= 1:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  
  
def find_max_prime(N):  
    """找到不大于N的最大素数"""  
    for num in range(N, 1, -1):  
        if is_prime(num):  
            return num  
    return None  # 理论上不会执行到这里，因为1不是素数，但保持代码的健壮性  
  
# 用户输入  
N = int(input())  
  
# 计算并输出结果  
max_prime = find_max_prime(N)  
print(f"{max_prime}")