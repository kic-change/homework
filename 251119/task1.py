age1 = int(input('请输入张明的年龄:'))
age2 = int(input('请输入张平的年龄:'))
print('张明:', age1)
print('张平:', age2)
if age1 == age2:
    print('张明和张平一样大，同年出生')
elif age1 > age2:
    print('张明比张平大')
else:
    print('张平比张明大')

print('两人都姓张')
