# 1.判断下列逻辑语句的True,False
# 1: 1 > 2 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
"""
False or True or False and True and True or True
False or True or False and True or True
False or True or False or True
True or False or True
True or True
True
"""
# 2： not 2> 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
"""
not True and True or False and True and True or False
False and True or False and True and True or False
False or False and True or False
False or False or False
False
"""

# 2.求出下列逻辑语句的值
# 1： 8 or 3 and 4 or 2 and 0 or 9 and 7
"""
8 or 4 or 0 or 7
8 or 0 or 7
8 or 7
8
"""
# 2： 0 or 2 and 3 and 4 or 6 and 0 or 3
"""
0 or 3 and 4 or 0 or 3
0 or 4 or 0 or 3
4 or 0 or 3
4 or 3
4
"""

# 3.下列结果是什么
"""
6
3
False
3
True
True
0
3
0
2
"""

# 4.实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输入错误时显示剩余错误次数（提示：使用字符串格式化）
"""

num = 0
print("开始登录...")
while num < 3:
    num = num + 1
    name = input("请输入用户名：")
    pwd = input("请输入密码：")
    if name == "chen" and pwd == "123":
        print("登录成功")
        break
    else:
        text = "用户名或密码错误，剩余登录次数为{}次".format(3 - num)
        print(text)
print("登录关闭...")
"""
# 5.猜年龄游戏：
# 要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果才对了，打印恭喜信息并退出。

number = 100
flag_num = 0
print("开始游戏...")
while flag_num < 3:
    flag_num = flag_num + 1
    input_number = input("请输入数字：")
    if int(input_number) == number:
        print("猜对啦！")
        break
    else:
        print("猜错啦！")
print("关闭游戏...")


# 6.猜年龄游戏升级版
# 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如果才对了，就直接退出。

number = 100
flag_num = 0
print("开始游戏...")
while flag_num < 3:
    flag_num = flag_num + 1
    input_number = input("请输入数字：")
    if int(input_number) == number:
        print("猜对啦！")
        break
    else:
        print("猜错啦！")
        if flag_num == 3:
            input_bool = input("是否继续游戏(Y/N)？")
            if input_bool == "Y":
                flag_num = 0
            elif input_bool == "N":
                flag_num = 3
            else:
                print("内容输入错误")
print("关闭游戏...")

