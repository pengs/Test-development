#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
python编写：身份认证系统V1.0
加入了错误次数的判断，超过次数，程序退出
'''

operate = input('''  	================================== 
    =	欢迎进入到身份认证系统V1.0     
	= 1. 登录
	= 2. 退出
	= 3. 认证
	= 4. 修改密码
	==================================
	请输入你的操作数字(1/2/3/4):
''')

count =0
while count<3:
    count += 1 
    if operate not in '1234':
        print("操作数据输入错误")
        continue
    else:
        if operate == '2':
            print("Login Out")
            break
        elif operate == '4':
            new_password = input('请输入你的新密码:')
            print("新密码是:{}".format(new_password))
            break
        else:
            username = input('输入你的用户名:')
            password = input('输入你的密码:')
            if operate == '1':
                if username !='' and password !='':
                    print("Login Successful!")
                    break
                else:
                    print("用户名和密码不能为空")
            elif operate == '3':
                name = 'dapeng'
                passwd = '0123'
                if name == username and passwd == password:
                    print("认证成功")
                    break
                else:
                    print("用户名或密码错误")









