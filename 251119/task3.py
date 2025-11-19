user_account = 'admin'
user_passwd = '123456'
account_input = input('请输入账号:')
passwd_input = input('请输入密码:')

if user_account == account_input and user_passwd == passwd_input:
    print('欢迎：', account_input)
    print('************教学管理系统************')
else:
    print('对不起，账号或密码错误！')
    print('请重新输入')
