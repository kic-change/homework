# user_name = input('请输入账号：')  # 接收用户输入的账号
# password = input('请输入密码：')  # 接收用户输入的密码
# print('Register Success!\n 你的用户名是：', user_name, '你的密码是:', password, '\n登录成功！')
# a, b = 100, 20
# print(a, end='\n\n\n')
# print(b)

#
# str1 = "123456"
# print(str1)
# a = 100
# b = 20.0
# c = [1, 3, 5]
# d = (1, 3, 5)
# e = {'a', 18, 'female'}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
ConutThing1 = int(input('请输入金士顿 U 盘 8G 的购买数量：'))
EachPrice1 = float(input('请输入金士顿 U 盘 8G 的单价：'))
SumPrice1 = ConutThing1 * EachPrice1

ConutThing2 = int(input('请输入胜创 16GTF 卡的购买数量：'))
EachPrice2 = float(input('请输入胜创 16GTF 卡的单价：'))
SumPrice2 = ConutThing2 * EachPrice2

ConutThing3 = int(input('请输入读卡器的购买数量：'))
EachPrice3 = float(input('请输入读卡器的单价：'))
SumPrice3 = ConutThing3 * EachPrice3

ConutThing4 = int(input('请输入网线 2 米的购买数量：'))
EachPrice4 = float(input('请输入网线 2 米的单价：'))
SumPrice4 = ConutThing4 * EachPrice4

StoreSum = ConutThing1 + ConutThing2 + ConutThing3 + ConutThing4
TotalSumPrice = SumPrice1 + SumPrice2 + SumPrice3 + SumPrice4

discount = float(input('请输入折扣：'))
AfterDiscount = TotalSumPrice * discount

Received = float(input('请输入顾客付款金额：'))
Charged = Received - AfterDiscount

print('..................................')
print('单号:DH202301010001')
print('时间:2023-01-01 08:56:15')
print('..................................')
print('名称        数量   单价     金额')
print('金士顿 U 盘 8G  ', ConutThing1, EachPrice1, SumPrice1, sep='     ')
print('胜创 16GTF 卡 ', ConutThing2, EachPrice2, SumPrice2, sep='     ')
print('读卡器      ', ConutThing3, EachPrice3, SumPrice3, sep='     ')
print('网线 2 米     ', ConutThing4, EachPrice4, SumPrice4, sep='     ')
print('..................................')
print('总数：', StoreSum, end='       ')
print('总额：', TotalSumPrice)
print('折后总额：', AfterDiscount)
print('实收：', Received, end='    ')
print('找零：', Charged)
print('收银：收银员')
print('..................................')
