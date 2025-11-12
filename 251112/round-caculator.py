# import math

# 1.输入圆的半径,以 r 表示
r = float(input("请输入圆的半径："))

# 2.计算过程

# 不引入外部库的情况下用 Pi 表示Π,取 3.14
pi = 3.14

# 直径
l = 2 * r

# 面积
s = pi * r ** 2

# 使用 math 库
# s = math.pi * r ** 2            


# 3.输出
print("圆的直径为：", l)
print("圆的面积为：", s)
