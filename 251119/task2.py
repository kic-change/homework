a = int(input('请输入数字:'))

if a < 0:
    print('数值非法，无法判断')
elif a % 2 == 1:
    print('a是奇数')
else :
    print('a是偶数')
