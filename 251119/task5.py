student_score = float(input('请输入百米赛跑初赛成绩:'))
student_gender = input('请输入性别:')

if student_gender == '男':
    if student_score < 10.0:
        print('进入男子组决赛!')
    else:
        print('淘汰')
elif student_score < 10.0:
    print('进入女子组决赛!')
else:
    print('淘汰')
