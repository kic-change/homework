# 已知条件
TotalWeight = 29.5
BigTruck = 4.0
SmallTruck = 2.5
LeftWeight = TotalWeight - BigTruck * 3 + SmallTruck
print('剩余的重量:', LeftWeight, '吨')
Times = LeftWeight / SmallTruck
print('还需要:', int(Times), '次，才能运完')
