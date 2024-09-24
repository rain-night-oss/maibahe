# 请补充你的代码
a=int(input())
b=int(input())
s=a*b
print(s)

# 请补充你的代码
a=float(input())
b=float(input())
s=a*b 
print(s)

# 请补充你的代码
a=eval(input())
b=eval(input())
s=a*b 
print(s)

# 请补充你的代码
length = float(input())  
width = float(input())  
area = round(length * width, 3)  
print(area)

# 请补充你的代码
a=eval(input())
b=eval(input())
s=a*b 
print(f'{s:.2f}')

# 请补充你的代码
a=float(input())
b=float(input())
s=a*b
print(f'长为{a}宽为{b}的矩形面积为{s:.2f}')

from audioop import error
import math

r=6371
S = 4 * math.pi * r**2 * 0.0001 
print(f'地球表面积为{S:.4f}万平方千米')

# 请补充你的代码
import math
r=6371
v=4/3*math.pi*r**3*0.0001
print(f'地球体积为{v:.4f}万立方千米')

# 请补充你的代码
import math  
  
# 地球半径，单位：千米，需要转换为米  
earth_radius_km = 6371  
earth_radius_m = earth_radius_km * 1000  
  
# 绳子延长后的周长（比地球周长多1米）  
new_circumference = 2 * math.pi * earth_radius_m + 1  
  
# 计算新的绳子围成的同心圆半径  
new_radius = new_circumference / (2 * math.pi)  
  
# 计算绳子与地球之间的空隙大小  
gap = new_radius - earth_radius_m  
  
# 格式化输出结果，保留小数点后3位  
print(f"空隙大小为{round(gap, 3)}米")  
  
# 老鼠身体截面直径，单位：米  
mouse_diameter_m = 0.1  # 10cm转换为米  
  
# 判断老鼠是否能从空隙中穿过  
if gap >= mouse_diameter_m / 2:  # 老鼠需要穿过的是直径的一半  
    print("老鼠可以从空隙中钻过")  
else:  
    print("老鼠无法通过空隙")


# 请补充你的代码
import math
earth_density = 5507.85  
earth_radius_km = 6371  
earth_radius_m = earth_radius_km * 1000 
earth_volume = (4/3) * math.pi * earth_radius_m**3 
earth_mass = earth_volume * earth_density
earth_mass_trillion_tons = earth_mass / (10**15)  # 1万亿吨 = 1e15吨  
earth_mass_trillion_tons_formatted = f"{earth_mass_trillion_tons:.1f}"  
print(f"地球质量约为{earth_mass_trillion_tons_formatted}万亿吨")
earth_mass_kg_formatted = f"{earth_mass:e}"  
print(f"地球质量约为{earth_mass_kg_formatted}千克")


'''
AB 是圆的一条弦，ABC形成一个弓形，在两行中分别输入AB和CD的长度，计算并输出该圆的半径，结果均严格保留小数点后2位有效数字，应用三角函数和反三角函数时查阅math模块文档或利用自动补全完成。
'''

import math

AB = float(input())  # 弦长度
CD = float(input())  # 弓高度
############Begin###############
# 半弦长
AD =AB/2

# 半径
OA =(AD*AD+CD*CD)/(2*CD)
print(f'{OA:.2f}')
############End###############

'''
AB 是圆的一条弦，ABC形成一个弓形，在两行中分别输入AB和CD的长度，计算输出弓形面积的大小，结果均严格保留小数点后2位有效数字，应用三角函数和反三角函数时查阅math模块文档或利用自动补全完成。
'''

import math

AB = float(input())  # 弦长度
CD = float(input())  # 弓高度

# 半弦长
AD = AB / 2
# 半径
OA = (AD ** 2 + CD ** 2) / (2 * CD)

# 圆心角
AOB = 2 * math.asin(AD / OA)
################Begin######################
# 弓形所在扇形的面积
s=AOB/(2*math.pi)*math.pi*OA**2
# 三角形面积
t=1/2*OA**2*math.sin(AOB)
# 弓形面积
area_of_arch = s-t

print(f'{area_of_arch:.2f}')
################End######################
python = 3
math = 4
english = 4
physical = 2
military_theory = 2
philosophy = 2
# 补充你的代码
a=int(input())
credits = (python + math + english + physical + military_theory + philosophy)
cost = a * credits
print(f'你本学期选修了{credits}个学分。')
print(f'你应缴纳的学费为{cost}元。')


python = 3
math = 4
english = 4
physical_education = 2
military_theory = 2
philosophy = 2
# 补充你的代码
tuition_per_credit = int(input("请输入每学分学费金额："))
total_credits =(python + math + english + physical_education + military_theory + philosophy)

total_tuition = total_credits * tuition_per_credit
per_living_expenses = int(input("请输入你每个月生活费："))
living_expenses = 5 * per_living_expenses
total_cost = living_expenses + total_tuition
student_loan = total_cost * 0.6
print(f'本学期你能够贷款{student_loan:.2f}元')

# 请补充你的代码
a=int(input("请输入第一个数字："))
b=int(input("请输入第二个数字："))
print(f'和：{a+b:.2f}')
print(f'差：{a-b:.2f}')
print(f'积：{a*b:.2f}')
print(f'商：{a/b:.2f}')

# 请补充你的代码
v=int(input("请输入当前速度（米/秒）："))
s=int(input("请输入障碍物距离（米）："))
a=float(input("请输入车辆最大制动加速度（米/秒²）："))
b= (v** 2) / (2 * a) 
print(f"制动距离为：{b:.2f} 米")
if b>=s:
    print("警告：车辆将会撞上障碍物！")
else:
    print("安全：车辆不会撞上障碍物。")



# 请补充你的代码
import math  
  
# 提示用户输入第一个点的纬度和经度  
lat1 = float(input("请输入第一个点的纬度（度）："))  
lon1 = float(input("请输入第一个点的经度（度）："))  
  
# 提示用户输入第二个点的纬度和经度  
lat2 = float(input("请输入第二个点的纬度（度）："))  
lon2 = float(input("请输入第二个点的经度（度）："))  
  
# 地球半径，单位公里  
r = 6371  
  
# 将纬度和经度差值转换为弧度  
dlat = math.radians(lat2 - lat1)  
dlon = math.radians(lon2 - lon1)  
  
# 使用Haversine公式  
a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2  
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))  
  
# 计算两点之间的距离  
distance = r * c  
  
# 格式化并输出距离，保留两位小数  
print(f"两点之间的距离为：{distance:.2f} 公里")


import math
m=int(input())
n=int(input())
radius_m = m / 2  
area_m = math.pi * radius_m ** 2  
radius_n = n / 2  
area_n = math.pi * radius_n ** 2  
from math import ceil  
count = ceil(area_m / area_n)  
print(count)


# 从输入中选择最大数的绝对值做为棱长计算正方体的体积
# 下面语句用于接收用空格分隔的多个输入，请不要修改
numbers_str = input()  
# 将输入的字符串按空格分割成列表，并将每个元素转换为浮点数  
numbers = list(map(float, numbers_str.split()))  
# print(width_ls)  # 取消注释可查看输入的数据
# 当输入为：2 50 26 88 40时，width_ls的值是[2.0, 50.0, 26.0, 88.0, 40.0]
# 不要直接从以上数据中人工选择，测试数据与示例不同，用函数获取
# 不能保证输入的最大值为正值，当最大值仍为负数时，取其绝对值做为棱长
max_abs=abs(max(numbers))
s=max_abs**3
print(f"volume = {s:.2f}立方米")
# 在下面补充你的代码，使之能用输入的最大值做棱长计算正方体的体积

import math  
  
# 输入两个用逗号分隔的正整数  
input_str = input()  
nums = [int(num) for num in input_str.split(',')]  
a, b = nums  
  
# 计算最大公约数和最小公倍数  
gcd_value = math.gcd(a, b)  
lcm_value = math.lcm(a, b)  
  
# 计算最大公约数的阶乘和最小公倍数的阶乘  
gcd_factorial = math.factorial(gcd_value)  
lcm_factorial = math.factorial(lcm_value)  
  
# 输出结果  
print(gcd_factorial)  
print(lcm_factorial)  
  
# 注意：题目只要求输出最大公约数的阶乘，但根据示例输出，这里也输出了最小公倍数的阶乘  
# 若只需输出最大公约数的阶乘，则只需保留第一个print语句

# 补充你的代码
input_str = input().strip()  # 使用strip()去除首尾可能存在的空白字符  
  
# 根据空格将字符串切分为列表  
tokens = input_str.split()  
  
# 初始化总和变量  
total_sum = 0  
  
# 遍历列表中的每个元素  
for token in tokens:  
    # 尝试将元素转换为整数  
    try:  
        total_sum += int(token)  # 如果转换成功，则累加到总和  
    except ValueError:  
        # 如果转换失败（即不是数字字符串），则忽略并继续下一个循环  
        continue  
  
# 输出总和  
print(total_sum)


# 补充你的代码
input_str =input()
import ast  
  
try:  
    # 使用ast.literal_eval安全地解析字符串为Python列表  
    list_of_strings = ast.literal_eval(input_str.replace("'", '"'))  # 这里的.replace()是假设性的，实际中可能不需要  
  
    # 过滤并转换列表中的数字字符串  
    numbers = [int(s) for s in list_of_strings if s.strip().isdigit()]  
  
    # 打印转换后的数字列表（这是预期输出的一部分，但不是直接作为最终输出）  
    print(numbers)  # 输出: [123, 456, 789]  
  
    # 计算总和并打印  
    total_sum = sum(numbers)  
    print(total_sum)  # 输出: 1368  
  
except ValueError:  
    print("输入的字符串不是一个有效的列表表示。")  
except Exception as e:  
    print(f"发生了一个错误: {e}")

mileage, wait_time = map(int, input().strip().split(','))  
  
# 初始化车费  
fare = 0  
  
# 起步费  
if mileage <= 3:  
    fare += 13  
  
# 3~15公里的费用  
if 3< mileage <=15:  
    fare +=13+(mileage-3) *2.3
  
# 超过15公里的费用  
if mileage > 15:  
    fare += 13+12*2.3+(mileage - 15) * 2.3 * 1.5  
  
# 等待时间费用  
fare += wait_time  
  
# 输出车费，取整  
print(int(fare))

n = int(input())  
  
# 初始化平方和变量  
square_sum = 0  
  
# 循环计算每一项的平方并累加到square_sum中  
for i in range(1, n+1):  
    square_sum += i * i  
  
# 输出结果  
print(square_sum)

def fibonacci(n):  
    # 初始化斐波那契数列的前两项  
    if n <= 0:  
        return 0  
    elif n == 1 or n == 2:  
        return 1  
    # 使用循环计算斐波那契数列的第n项  
    a, b = 1, 1  
    for i in range(3, n + 1):  
        a, b = b, a + b  
    return b  
  
def main():  
    # 用户输入月份数  
    month = int(input())  
    # 计算该月的兔子总对数  
    rabbits = fibonacci(month)  
    # 如果月份数大于1，则计算前一个月与本月兔子数量的比值  
    if month > 1:  
        prev_month_rabbits = fibonacci(month - 1)  
        ratio = prev_month_rabbits / rabbits  
        # 输出结果，保留小数点后三位  
        print(f"{rabbits} {ratio:.3f}")  
    else:  
        # 如果月份数为1，则直接输出兔子对数和比值（这里比值无意义，但为了格式统一，输出0.000）  
        print(f"{rabbits} 0.000")  
  
if __name__ == "__main__":  
    main()

    def leibniz_of_pi(error):  
        """  
        使用莱布尼茨级数计算π的近似值。  
        :param error: 浮点数，作为迭代停止的阈值。  
        :return: π的近似值，浮点数。  
        """  
    pi_estimate = 0.0  # 初始化π的估计值  
    sign = 1  # 符号，初始为正  
    denominator = 1  # 分母，初始为1  
      
    while True:  
        term = sign / denominator  # 当前项的值  
        if abs(term) <= error:  
            break  # 如果当前项的绝对值小于等于阈值，则停止迭代  
        pi_estimate += term  # 将当前项加到π的估计值上  
          
        # 准备下一项  
        sign *= -1  # 交替符号  
        denominator += 2  # 分母增加2  
  
    # 由于莱布尼茨级数收敛到π/4，所以我们需要将结果乘以4来得到π的近似值  
    
  
# 测试代码  
if __name__ == '__main__':  
    threshold = float(input())  
    print("{:.8f}".format(leibniz_of_pi(threshold)))  # 保留小数点后八位

    '''
利用梅钦公式计算圆周率的大小
'''
import math  
  
def machin_pi():  
    # 使用简化的梅钦公式计算π的近似值  
    pi_over_4 = 4 * math.atan(1/5) - math.atan(1/239)  
    return pi_over_4 * 4  
  
# 调用函数并打印结果，保留16位小数  
print(f"{machin_pi():.16f}")



def is_prime(n):  
    """检查一个数是否是素数"""  
    if n <= 1:  
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  
  
def find_largest_prime(N):  
    """找到不大于N的最大素数"""  
    for num in range(N, 1, -1):  
        if is_prime(num):  
            return num  
  
# 读取输入  
N = int(input())  
  
# 计算并输出结果  
print(find_largest_prime(N))

def is_prime(num):  
    """检查一个数是否为素数"""  
    if num <= 1:  
        return False  
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:  
            return False  
    return True  
  
def find_primes(n):  
    """找出n以内（包括n）的所有素数"""  
    primes = []  
    for num in range(2, n + 1):  
        if is_prime(num):  
            primes.append(num)  
    return primes  
  
# 读取输入  
n = int(input().strip())  
  
# 输出结果  
print(' '.join(map(str, find_primes(n))))


# 读取输入，输入格式为：行驶里程,等待时间  
mileage, wait_time = map(int, input().strip().split(','))  
  
# 初始化车费  
fare = 0  
  
# 起步费  
if mileage <= 3:  
    fare += 13  
  
# 3~15公里的费用  
if 3< mileage <=15:  
    fare +=13+(mileage-3) *2.3
  
# 超过15公里的费用  
if mileage > 15:  
    fare += 13+12*2.3+(mileage - 15) * 2.3 * 1.5  
  
# 等待时间费用  
fare += wait_time  
  
# 输出车费，取整  
print(int(fare))

def leibniz_of_pi(error):  
    
    pi_estimate = 0.0  # 初始化π的估计值  
    sign = 1  # 符号，初始为正  
    denominator = 1  # 分母，初始为1  
      
    while True:  
        term = sign / denominator  # 当前项的值  
        if abs(term) <= error:  
            break  # 如果当前项的绝对值小于等于阈值，则停止迭代  
        pi_estimate += term  # 将当前项加到π的估计值上  
          
        # 准备下一项  
        sign *= -1  # 交替符号  
        denominator += 2  # 分母增加2  
  
    # 由于莱布尼茨级数收敛到π/4，所以我们需要将结果乘以4来得到π的近似值  
    return pi_estimate * 4  
  
# 测试代码  
if __name__ == '__main__':  
    threshold = float(input())  
    print("{:.8f}".format(leibniz_of_pi(threshold)))  # 保留小数点后八位

    import math  
  
def cutting_circle(n):  
    """接收表示分割次数的整数n为参数，计算分割n次时正多边形的边数和圆周率值，返回边数和圆周率值"""  
    side_length = 1         # 初始边长  
    edges = 6               # 初始边数  
    # 每次分割，边数翻倍，边长通过正弦函数和半角公式来近似计算  
    for _ in range(n):  
        edges *= 2  
        
        side_length = 2 * math.sin(math.pi / edges)  
    # 圆周率近似为多边形周长除以直径（2）  
    pi = edges * side_length / 2  
    return edges, round(pi, 6)  # 返回边数和保留六位小数的圆周率值  
  
if __name__ == '__main__':  
    times = int(input())          # 割圆次数  
    edges, pi = cutting_circle(times)  
    print('分割{}次，边数为{}，圆周率为{}'.format(times, edges, pi))  
    print(f'math库中的圆周率常量值为{round(math.pi, 6)}')

    
  
def find_largest_prime(N):  
    """找到不大于N的最大素数"""  
    for num in range(N, 1, -1):  
        if is_prime(num):  
            return num  
  
# 读取输入  
N = int(input())  
  
# 计算并输出结果  
print(find_largest_prime(N))

def is_prime(num):  
    """检查一个数是否为素数"""  
    if num <= 1:  
        return False  
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:  
            return False  
    return True  
  
def find_primes(n):  
    """找出n以内（包括n）的所有素数"""  
    primes = []  
    for num in range(2, n + 1):  
        if is_prime(num):  
            primes.append(num)  
    return primes  
  
# 读取输入  
n = int(input().strip())  
  
# 输出结果  
print(' '.join(map(str, find_primes(n))))


# 请输入你的代码
# 初始信息  
initial_price = 15  # 初始股价  
shares = 5500  # 股票数量  
daily_increase_rate = 1.1  # 每日涨停率  
days = 15  # 涨停天数  
  
# 计算15天后的股价  
final_price = initial_price * (daily_increase_rate ** days)  
  
# 计算卖出总金额  
total_sell_amount = final_price * shares  
  
# 计算总成本  
total_cost = initial_price * shares  
  
# 计算获利  
profit = total_sell_amount - total_cost  
  
# 保留两位小数并打印结果  
print(f"{profit:.2f}")

# 补充你的代码
binary_num1 = input()  
binary_num2 = input()  
  
# 去除'0b'前缀（如果有的话），并将字符串转换为整数  
num1 = int(binary_num1, 2) if binary_num1.startswith('0b') else int(binary_num1, 2)  
num2 = int(binary_num2, 2) if binary_num2.startswith('0b') else int(binary_num2, 2)  
  
# 计算和  
sum_num = num1 + num2  
  
# 将结果转换回二进制字符串，并去除'0b'前缀  
binary_sum = bin(sum_num)[2:]  
  
# 输出结果  
print(binary_sum)

import math  
  
# 从用户那里接收三个实数  
a = float(input())  
b = float(input())  
c = float(input())  
  
# 计算判别式  
D = b**2 - 4*a*c  
  
# 计算两个解  
# 注意：由于题目保证D > 0，我们可以直接计算sqrt(D)  
x1 = (-b + math.sqrt(D)) / (2*a)  
x2 = (-b - math.sqrt(D)) / (2*a)  
  
# 按从大到小顺序输出解  
if x1 > x2:  
    print(f"{x1:.2f} {x2:.2f}")  
else:  
    print(f"{x2:.2f} {x1:.2f}")


import math  
  
# 地球半径  
radius = 6371 * 1000 # 单位：km  
  
# 1. 计算地球表面积  
surface_area = 4 * math.pi * radius * radius  
print(f'地球表面积为{surface_area:.2f}平方米')  # 注意单位转换（实际应为平方千米，但题目要求平方米）  
  
# 2. 计算地球体积  
volume = (4 * math.pi * radius ** 3) / 3  
print(f'地球体积为{volume:.2f}立方米')  
  
# 3. 计算地球赤道的周长  
circumference = 2 * math.pi * radius  
print(f'地球赤道周长为{circumference:.2f}米')  
  
# 4. 计算绳子与地球之间的空隙大小  
# 绳子延长1m后的新周长  
new_circumference = circumference + 1  
# 计算新的半径  
new_radius = new_circumference / (2 * math.pi)  
# 空隙大小 = 新半径 - 原半径  
gap = new_radius - radius  
print(f'空隙大小为{gap:.2f}米')  
  
# 5. 判断老鼠是否能通过空隙  
mouse_diameter = 0.1  # 老鼠身体截面圆柱最粗处直径，单位：米  
if gap > mouse_diameter / 2:  
    print('老鼠可以从空隙中钻过')  
else:  
    print('老鼠无法通过空隙')


import math


def type_judge(geom_type):
    """接收一个字符串为参数，根据参数判断几何体类型
    若输入为二维图形，计算其面积
    若输入为三维图形，计算其面积与体积
    根据类型调用不同的函数进行运算。
    """
    if geom_type == '长方形':
        length, width = map(float, input().split())  # 空格分隔的输入切分为列表并映射为浮点数
        return square(length, width)                 # 调用函数计算长方形面积
    elif geom_type == '长方体':
        length, width, height = map(float, input().split())  # 空格分隔的输入切分为列表并映射为浮点数
        return cube(length, width, height)                   # 调用函数计算长方体表面积与体积
    elif geom_type == '圆形':
        radius = float(input())  # 输入转为浮点数
        return circle(radius)    # 调用函数计算圆面积
    elif geom_type == '球':
        radius = float(input())  # 输入转为浮点数
        return sphere(radius)    # 调用函数计算球表面积与体积
    elif geom_type == '圆柱体':
        radius, height = map(float, input().split())  # 空格分隔的输入切分为列表并映射为浮点数
        return cylinder(radius, height)  # 调用函数计算圆柱体表面积与体积
    elif geom_type == '圆锥':
        radius, height = map(float, input().split())  # 空格分隔的输入切分为列表并映射为浮点数
        return cone(radius, height)  # 调用函数计算圆锥表面积与体积
    elif geom_type == '正三棱柱':
        side, height = map(float, input().split())
        return tri_prism(side, height)
    else:
        return f'未找到{geom_type}计算方法'


def square(length, width):
    """计算长方形的面积"""
    area_of_square = length * width
    return f'长方形的面积为{area_of_square:.2f}'


def cube(length, width, height):
    """计算长方体的表面积和体积"""
    area_of_cube = length * width * 2 + width * height * 2 + length * height * 2
    volume_of_cube = length * width * height
    return f'长方体的表面积为{area_of_cube:.2f}, 体积为{volume_of_cube:.2f}'


def circle(radius):
    """接收圆的半径，返回圆形的面积，圆周率用math.pi"""
    # 对齐此位置补充你的代码
    area_of_circle = math.pi * radius ** 2  
    return f'圆形的面积为{area_of_circle:.2f}'

def sphere(radius):
    """接收球的半径，返回球的表面积和体积，圆周率用math.pi"""
    # 对齐此位置补充你的代码
    surface_area_of_sphere = 4 * math.pi * radius ** 2  
    volume_of_sphere = (4/3) * math.pi * radius ** 3  
    return f'球的表面积为{surface_area_of_sphere:.2f}, 体积为{volume_of_sphere:.2f}' 


def cylinder(radius, height):
    """接收圆柱体的底面半径和高，返回圆柱体的表面积和体积，圆周率用math.pi"""
    # 对齐此位置补充你的代码
    surface_area_of_cylinder = 2 * math.pi * radius * (radius + height)  
    volume_of_cylinder = math.pi * radius ** 2 * height  
    return f'圆柱体的表面积为{surface_area_of_cylinder:.2f}, 体积为{volume_of_cylinder:.2f}'


def cone(radius, height):
    """接收圆锥的底面半径和高，返回圆锥的表面积和体积，圆周率用math.pi"""
    # 对齐此位置补充你的代码
    slant_height = math.sqrt(radius ** 2 + height ** 2)  
    surface_area_of_cone = math.pi * radius * (slant_height + radius)  
    volume_of_cone = (1/3) * math.pi * radius ** 2 * height  
    return f'圆锥的表面积为{surface_area_of_cone:.2f}, 体积为{volume_of_cone:.2f}'  



# 参考前面的方法自定义一个函数计算正三棱柱的表面积与体积，
# 对齐此位置定义函数的语句

    """函数名为tri_prism，接受底边长和高两个参数side, height"""
    # 对齐此位置补充函数体代码




def tri_prism(side, height):  # 修改为接收正确的参数名  
    # 计算等边三角形的面积  
    triangle_area = (math.sqrt(3) / 4) * side**2  
    # 计算正三棱柱的侧面积  
    lateral_area = 3 * side * height  
    # 计算正三棱柱的表面积  
    total_surface_area = 2 * triangle_area + lateral_area  
    # 计算正三棱柱的体积  
    volume = triangle_area * height  
  
    # 格式化输出并返回结果  
    surface_area_str = "{:.2f}".format(total_surface_area)  
    volume_str = "{:.2f}".format(volume)  
    return f"正三棱柱的表面积为{surface_area_str}, 体积为{volume_str}"
  
if __name__ == '__main__':  
    type_of_geometry = input()  
    geometry = type_judge(type_of_geometry)  
    print(geometry)