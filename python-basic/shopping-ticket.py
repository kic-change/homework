CountThing1 = int(input('请输入金士顿 U 盘 8G 的购买数量：'))  # 输入购买数量，这里是输入整数转为 int 类型（整型），选择 int 类型是因为没有 0.5 个东西
EachPrice1 = float(input('请输入金士顿 U 盘 8G 的单价：'))  # 输入单价，这里是输入浮点数转为 float 类型（浮点型），选择 float 类型是因为单价可以是小数
SumPrice1 = CountThing1 * EachPrice1  # 计算金额

CountThing2 = int(input('请输入胜创 16GTF 卡的购买数量：')) #此处同理，下略
EachPrice2 = float(input('请输入胜创 16GTF 卡的单价：'))
SumPrice2 = CountThing2 * EachPrice2

CountThing3 = int(input('请输入读卡器的购买数量：'))
EachPrice3 = float(input('请输入读卡器的单价：'))
SumPrice3 = CountThing3 * EachPrice3

CountThing4 = int(input('请输入网线 2 米的购买数量：'))
EachPrice4 = float(input('请输入网线 2 米的单价：'))
SumPrice4 = CountThing4 * EachPrice4

StoreSum = CountThing1 + CountThing2 + CountThing3 + CountThing4 # 计算总数量
TotalSumPrice = SumPrice1 + SumPrice2 + SumPrice3 + SumPrice4 # 计算总金额

discount = float(input('请输入折扣，如无折扣请输入 1.0：')) # 输入折扣转换
if discount != 1.0: # 判断是否为原价，1.0 是原价，其他折扣就对应一折二折三折这些折扣
    AfterDiscount = TotalSumPrice * discount
else:
    AfterDiscount = TotalSumPrice
Received = float(input('请输入顾客付款金额：'))  # 输入顾客付款金额
Charged = Received - AfterDiscount # 计算找零

# 以下是输出的购物小票，使用的是 format，正常情况下要用 sep='     '，但是这里用 format 方法会更方便
print('.........................................')
print('单号:DH202301010001')
print('时间:2023-01-01 08:56:15')
print('.........................................')
print('{:<15}{:>6}{:>8}{:>10}'.format('名称', '数量', '单价', '金额'))
print('{:<15}{:>6}{:>8.2f}{:>10.2f}'.format('金士顿 U 盘 8G', CountThing1, EachPrice1, SumPrice1))
print('{:<15}{:>6}{:>8.2f}{:>10.2f}'.format('胜创 16GTF 卡', CountThing2, EachPrice2, SumPrice2))
print('{:<15}{:>6}{:>8.2f}{:>10.2f}'.format('读卡器', CountThing3, EachPrice3, SumPrice3))
print('{:<15}{:>6}{:>8.2f}{:>10.2f}'.format('网线 2 米', CountThing4, EachPrice4, SumPrice4))
print('.........................................')
print('总数：{:>6}       总额：{:>10.2f}'.format(StoreSum, TotalSumPrice))
print('折后总额：{:>10.2f}'.format(AfterDiscount))
print('实收：{:>8.2f}    找零：{:>8.2f}'.format(Received, Charged))
print('收银：收银员')
print('.........................................')