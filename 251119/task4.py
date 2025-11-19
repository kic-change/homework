user_age = int(input('请输入年龄:'))
if user_age < 18:
    print('您是未成年人')
elif user_age < 40:
    print('您是青年人')
elif user_age < 60:
    print('您是中年人')
else:
    print('您是老年人')
