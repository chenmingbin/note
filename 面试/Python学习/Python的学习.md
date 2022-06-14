# Python的学习

## day01 计算机基础和环境搭建

**课程目标：了解计算机基础知识并完成Python的环境搭建**

**课程概要：**

- 计算机基础
- 编程的本质
- Python的介绍
- Python环境的搭建

### 1.计算机基础

#### 1.1 基本概念

- 计算机的组成：

  ```
  计算机是由多个硬件组合而成，常见硬件有：CPU、硬盘、内存、显卡、电源等等....
  注意事项：这只是将硬件组合在一起，它们之间是无法进行协作
  ```

- 操作系统：

```
用于协调计算机的各个硬件，让硬件之间进行协调工作，以完成某个目标
常见的操作系统分类：
-Windows 优点：生态牛逼、工具多；缺点:略慢、收费
	- XP
	- WIN7
	- WIN10
	....
-Linux 优点：资源占用少、免费（用Linux当服务器）；缺点：工具少、告别游戏
	- Centos
	- Ubuntu
	- Redhat
	....
-Mac 优点：用户体验和交互；缺点：告别游戏
	....
```

- 软件（应用程序）

```
安装操作系统后，我们会在自己电脑上安装一些常用的软件，例如：QQ、微信等等....
```

- Linux-Python安装

```
第一步-安装：wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
第二步-解压：tar -zxvf Python-3.7.0.tgz
第三步-创建存放目录：mkdir /usr/local/python3
第四步-移动文件到存放目录：mv Python-3.7.0.tgz /usr/local/python3
第四步-进入py文件：cd /usr/local/python3/Python-3.7.0
第五步-执行配置文件：./configure --prefix=/usr/local/python3
第六步-编译安装：make && make install
第七步-建立软连接：ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
				ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3
	安装完毕.....
其他特殊情况：
	问题一：安装时报错ModuleNotFoundError: No module named '_ctypes'的解决办法
缺少文件-执行命令:yum install libffi-devel，安装完毕后重新编译即可
	问题二：安装时报错zipimport.ZipImportError: can't decompress data; zlib not available的解决方法
缺少文件-执行命令：yum -y install zlib*
进入目录：   	/usr/local/python3/Python-3.6.8/Modules下的Setup文件
找到：			 #zlib zlibmodule.c -I$(prefix)/include -L$(exec_prefix)/lib -lz
去掉注释保存退出并重新编译即可
```

#### 1.2 编程语言

软件：是由程序员使用 编程语言 开发出来的一大堆代码的集合。全球的编程语言有2500+多种，常见的编程语言：Java、C#、Python、PHP......

作文：是由学生使用 汉语、英语、法语、日语...写出来一大堆的文字的集合

​	本质上学习编程语言就是学习他的语法，根据语法再去编写相应的软件的功能

- Python语言中输出的语法规则：

  ```python
  print("输入需要打印的内容")
  ```

- Golang语言中输出的语法规则：

  ```go
  fmt.println("输入需要打印的内容")
  ```

  

#### 1.3 编译器/解释器

编译器/解释器，就是一个翻译官，将代码翻译成计算机能够识别的命令

```
A使用Python开发了一个软件				B使用Golang开发了一个软件
	Python解释器							Golang编译器
	 				操	作	系	统
	 			CPU	硬盘	网卡	内存	电源	.....
```

为什么有的叫解释器，有点的编译器？

- 解释器：实时翻译，拿到代码后，解释一句交给操作系统一句。
- 编译器：全文翻译，拿到代码后，会编译成一个临时文件（文件内都是计算机能够直接识别的命令）统一交给操作系统去读取



Python、PHP、Javascript、Puby...一般称为解释型语言

C、C++、Java...一般称为编译型语言



### 2.学习编程的本质

学习编程本质上就三件事：

- 选择一门编程语言，在自己的电脑上安装此安装语言相关的 编译器/解释器。
- 学习编程语言的语法规则，根据语法规则+业务背景 设计并开发你的软件(代码集合)
- 使用 编译器/解释器 去运行自己写的代码



### 3.Python的介绍



#### 3.1 语言的分类

- 翻译的维度

  - 解释型语言，Python、Ruby...
  - 编译型语言，C、C++、Golang...

- 高低的维度

  - 低级编程语言，写出来的代码可以直接被计算机识别。

    ```
    机器语言，101 001 00001 00010，机器码，交给计算机去识别
    汇编语言，MOV、INC... 通过编写这种指令可以直接交给计算机去识别
    ```

  - 高级编程语言，写出来的代码无法直接被计算机识别，但可以通过某种方式将其转换给计算器可以识别的语言。

    ```
    C、C++、Java、Python....这类编程语言在在编写代码时几乎是写英语作文。
    交由相关编译器或解释器翻译成机器码，然后再交给计算机去执行。
    ```

  注意：现在基本上都使用高级编程语言



#### 3.2 Python

火爆的原因：

- 语法简洁&适合小白。
- 类库的强大。
- 开发效率高。



#### 3.3Python的解释器种类(了解)

想要学一门编程语言：安装Python解释器、学习语法并编写代码、使用解释器去执行编写好的代码

主流解释器：

- Cpython【主流】，底层是由C语言开发出来的Python解释器
- Jython，是由Java语言开发出来的Python解释器，方便与让Python和Java代码做集成
- LronPython，是基于C#语言开发出来的Python解释器，方便与让Python和C#代码做集成
- RubyPython
- PyPy，是对Cpython的优化，执行效率提高了，引入编译器的功能，本质上将Python代码进行编译，再去执行编译后的代码
- ....

注意：常说的Python解释器默认指的就是CPython解释器。



#### 3.4 CPython解释器的版本

CPython的解释器主要有两大版本：

- 2.X，目前最新的Python版本2.7.18 （2020后不再维护）
- 3.X，目前最新的Python版本3.9.0



### 4.环境搭建

- Python解释器，将程序员编写的Python代码翻译成计算机能够识别的指令
  - 主流CPython
  - 3.9.0版本

- 学习编程本质上的三件事
  - 安装CPython3.9.0版本解释器
  - 学习语法并写代码
  - 解释器去运行代码



#### 4.1 安装Python解释器

##### 4.1.1 windows系统

- Python官网下载Python解释器

  ```
  https://www.python.org/downloads/release/python-390/
  ```



#### 4.2 安装Pycharm编辑器

帮助我们快速写代码，用Pycharm可以大大的提高咱们写代码的效率，+解释器去运行代码





## day02 快速上手

**课程目标：学习Python最基础的语法知识，可以用代码快速实现一些简单的功能。**

**课程概要：**

- 初识编码（密码本）
- 编程初体验
- 输出
- 初识数据类型
- 变量
- 注释
- 输入
- 条件语句



### 1.编码

**计算机中所有的数据本质上都是以0和1的组合来存储的。**

![image-20220105141053528](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105141053528.png)

**在计算机中会将中文内存转换成0101010101......，最终存储到硬盘上。**

![image-20220105141252774](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105141252774.png)

**注意事项：以某个编码的形式进行保存文件，以后就要以这种编码去打开这个文件，否则会出现乱码。**



### 2.编程初体验

- 编码必须要保持：保存和打开要一致，否则会乱码。
- Python解释器默认是以UTF-8的格式读取文件。



### 3.输出

- 将结果或内容想要呈现给用户。

```python
print("看着风景美如画")输出：看着风景美如画
```

- 默认print在尾部会加换行符。

```python
print("看着风景美如画")print("本想吟诗赠天下")输出：看着风景美如画本想吟诗赠天下
```

- 想要不换行，可以这样

```python
print("看着风景美如画，",end="")print("本想吟诗赠天下。",end="")输出：看着风景美如画，本想吟诗赠天下。亦可以这样：print("看着风景美如画",end="，")print("本想吟诗赠天下",end="。")输出：看着风景美如画，本想吟诗赠天下。
```

##### 练习题

- 1.输出自己的名字

  ```python
  print("陈明彬")
  ```

- 2.换行输出（春眠不觉晓，处处闻啼鸟，夜来风雨声，花落知多少。）

  ```python
  print("春眠不觉晓，")print("处处闻啼鸟，")print("夜来风雨声，")print("花落知多少。")
  ```

- 3.不换行输出（春眠不觉晓，处处闻啼鸟，夜来风雨声，花落知多少。）

  ```python
  print("春眠不觉晓", end=",")print("处处闻啼鸟", end=",")print("夜来风雨声", end=",")print("花落知多少", end="。")
  ```



### 4.初始数据类型

#### 4.1 整型(int)

![image-20220105144802230](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105144802230.png)



#### 4.2 字符串(str)

- 单行字符串

```python
print("我是Alex")print('我是Alex')print("我是'alex")print("中国北京昌平区")输出：我是Alex我是Alex我是'alex中国北京昌平区
```

- 多行字符串

```python
print("""中国北京昌平区""")print('''中国北京昌平区''')输出：中国北京昌平区中国北京昌平区
```

- 对于字符串：

- 加，两个字符串可以通过加号拼接起来。

```python
print("alex" + "是金角大王")输出：alex是金角大王
```

- 乘，让整型和字符串进行相乘，以实现让字符串重复出现N次并拼接起来。

```python
print(3 * "我想吃饺子")输出：我想吃饺子我想吃饺子我想吃饺子
```



#### 4.3 布尔类型(bool)

![image-20220105150248755](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105150248755.png)



#### 4.4 类型转换

上文数据类型int/str/bool有了初步了解，他们都有自己不同的定义方式。

- int，整型定义时，必须是数字且无引号，例如：5、8、9
- str，字符串定义时，必须用双引号括起来，例如："中国"、"edison"、"666"
- bool，布尔值定义时，只能写True和False

不同的数据类型都有不同的功能吗，例如：整型可以加减乘除 而 字符串只能加(拼接)和乘法。

如果想要做转换可遵循一个基本规则，想转换什么类型就让它包裹一些

例如：str(666)是可以将整型转换为字符串、int("888")是将字符串转换为整型



- 转换为整型：

```python
# 字符串转换为整型int("666")int("999")"6" + "9"的结果应该是："69"int("6") + int("9") 的结果是：6+9=15int("alex是sb") 报错# 布尔类型转换为整型int(True) 转换完等于1int(False) 转换完等于0
```



- 转换为字符串：

```python
# 整型转字符串str(345)str(666) + str(9) 结果为："6669"#布尔类型转字符串str(True)  "True"str(False) "False"
```



- 转换为布尔类型：

```python
# 整型转布尔bool(1)  Truebool(2)  Truebool(0)	 Flasebool(-10) True#字符串转布尔bool("alex")  Truebool("湿哒哒的")  Truebool("") Falsebool(" ") True
```



**三句话搞定类型转换：**

- 其他所有类型转换为布尔类型时，除了 空字符串、0 以外其他都是True。

- 字符串转整型时，只有那种"998"格式的字符串才可以转换为整型，其他都报错

- 想要转换为哪种类型，就用这类型的英文包裹一下就行。

  ```python
   str() int() bool()
  ```

  

##### **练习题**

![image-20220105151829280](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105151829280.png)



### 5.变量

变量，其实就是我们生活中起别名和外号，让变量名指向某个值，格式为：【变量名=值】，以后可以通过变量名来操作其对应的值。

```python
name = "陈明彬"
print(name)
输出：
“陈明彬”
```

```python
age = 18
name = "alex"
flag = 1 > 18
address = "北京昌平区" + "沙河"
addr = "北京昌平区" + "沙河" + name # 北京昌平区沙河alex 

print(addr) # 北京昌平区沙河alex
print(flag) # False
```

```python
age = 18
number = 1 == 2
```

注意：

- 给变量赋值`age = 18`
- 让age代指值`age=18`



#### 5.1 变量名的规范

```python
age = 18
name = "alex"
flag = 1 > 18
address = "北京昌平区" + "沙河"
```

三个规范：

- 变量名只能由字母、数字、下划线 组成

- 不能以 数字 开头

  ```python
  na9me9 = "alex"
  ```

- 不能用Python内置的关键字

```python
def = "alex"break = 123
```

两个建议：

- 下划线链接命名(小写)

  ```python
  father_name = "asdasd"brother_age = 19
  ```

- 见名知意

```py
name = "陈明彬"age = 18
```



##### **练习题**

![image-20220105154222297](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105154222297.png)



#### 5.2 变量内存指向关系

 ![image-20220105154531968](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105154531968.png)

![image-20220105154742263](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105154742263.png)

![image-20220105154823736](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105154823736.png)

##### 练习题

![image-20220105155028427](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105155028427.png)

![image-20220105160044097](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105160044097.png)

答案：

```python
"""1.total = 212.age = 18ming_age = age + 3liu_age = age + ming_age + 5print(ming_age,liu_age)3.nickname = "一米八大高个"username = "弟弟"4.nickname = "弟弟"username = "一米八大高个"5.text = "弟弟一米八大高个"6.text = "一米八大高个弟弟"7.data = "202020"value = 60"""
```



### 6.注释

写代码的时候，如果想要对某些内容进行注释处理，即：解释器忽略不会按照代码去运行。

- 单行注释

  ```python
  # 声明一个变量name = "alex"age = 19 # 这表示当前用户的年龄注意：快捷键 Ctrl+？	command+？
  ```

- 多行注释

  ```python
  #多行注释内容
  #多行注释内容
  #多行注释内容
  """
  多行注释内容
  多行注释内容
  多行注释内容
  """
  ```

  

### 7.输入

输入，可以实现程序和用户之间的交互。

```python
# 1.input("请输入用户名：") 是让用户输入内容。
# 2.将用户输入的内容赋值给name变量，方便用来扩展其他操作
name = input("请输入用户名：")

# 可以用来判断
if name == "alex":
    print("登录成功")
else:
    print("登录失败")
```

**特别注意**：用户输入的任何内容本质上都是字符串。

##### 练习题

1.提示输入姓名，然后给姓名后面拼接一个"烧饼"，最终打印结果。

```python
name = input("请输入姓名：")
new_name = name + "烧饼"
print(new_name)
```

2.提示输入 姓名、位置、行为，然后做拼接并打印：XX在XX做XX

```python
name = input("请输入姓名：")
address = input("请输入位置：")
flag = input("请输入行为：")
print(name+"在"+address+"做"+flag)
```

3.提示输入两个数字，计算两个数的和

```python
name_1 = input("请输入数字：")
name_2 = input("请输入数字：")
name_3 = int(name_1)+int(name_2)
print(name_3)
```



### 8.条件语句

 ```python
"""if 条件 :	条件成立之后执行的代码...else:	条件不成立之后执行的代码..."""
 ```



#### 8.1 基本条件语句

![image-20220105164427306](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105164427306.png)

![image-20220105164459914](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105164459914.png)

![image-20220105164613704](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105164613704.png)

 ![image-20220105164752510](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105164752510.png)

##### 练习题

1.提示用户输入用户名和密码，用户名等于"wupeiqi"且密码等于"uuu"就输出登录成功，否则输出登录失败

```python
username = input("请输入用户名：")password = input("请输入密码：")if username == "wupeiqi" and password == "uuu":    print("登录成功")else:    print("登录失败")
```

2.猜数字，提示用户输入一个数字，判断数字如果大于10，就输出猜错了，否则输出猜对了

```python
number = input("请输入数字：")data = int(number)if data > 10:    print("猜错了")else:    print("猜对了")
```

3.提示用户输入一个数字，判断是否为偶数，是偶数则输出 偶数，否则输出 奇数

```python
number = input("请输入数字：")if int(number) % 2 == 1:    print("奇数")else:    print("偶数")
```



#### 8.2 多条件判断

```python
if 条件A:    A成立，执行此缩进中的所有代码   	...elif 条件B:    B成立，执行此缩进中的所有代码    ...elif 条件C:    C成立，执行此缩进中的所有代码else:    上述ABC都不成立时执行所有代码 
```

![image-20220105170829798](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105170829798.png)

#### 8.3 条件嵌套

![image-20220105172228845](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105172228845.png)

![image-20220105172254160](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220105172254160.png)

### 今日作业

 **1.谈谈你了解的编码以及为什么会出现乱码的现象**

​	答：编码有UTF-8；因为保存时的编码格式与打开时的编码格式不一致。

**2.Python解释器默认编码是什么？如何修改？**

默认编码为UTF-8，在文件顶部

**3.用print打印出下面内容**

```python
文能提笔安天下，
武能上马定乾坤，
心存谋略何人胜，
古今英雄唯是君。
```

答：

```python
print("文能提笔安天下，")
print("武能上马定乾坤，")
print("心存谋略何人胜，")
print("古今英雄唯是君。")
```



**4.变量名的命名规范和建议？**

答：不能以数字开头、不可使用标点符号(仅可使用下划线)、不能使用Python内置关键字

**5.如下哪个变量名是正确的？**

```python
name = '陈明彬'	# 对
_ = 'alex'	# 对
_9 = "老男孩"	# 对
9name = "宝浪"	#错
oldboy(edu = 666	#错
```

**6.设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了，如果比66小，则显示猜测的结果小了，只有等于66，显示猜测结果正确**

```python
number = input("请输入数字：")
if int(number) > 66:
    print("大了")
elif int(number) < 66:
    print("小了")
elif int(number) == 66:
    print("正确")
```

**7.提示用户输入"爸爸"，判断用户输入的对不对，如果对，提示真聪明，如果不对，提示你是傻逼么。**

```python
data = input("请输入关键字-爸爸")
if data == "爸爸":
    print("真聪明")
else:
    print("你是傻逼么")
```

**8.写程序，成绩有ABCDE5个等级，与分数的对应关系如下**

```python
A 90-100 B 80-89 C 60-79 D 40-59 E 0-39
```

**要求用户输入0-100的数字后，你能正确打印他的对应成绩等级**

```python
choice = input("请输入成绩：")
new_choice = int(choice)
if new_choice >= 90 and new_choice <= 100:    
    print("A")
elif new_choice >= 80 and new_choice <= 89:    
    print("B")
elif new_choice >= 60 and new_choice <= 79:    
    print("C")
elif new_choice >= 40 and new_choice <= 59:    
    print("D")
elif new_choice >= 0 and new_choice <= 39:    
    print("E")
else:
    print("输入错误，请重新输入")
```

```python
choice = input("请输入成绩：")
new_choice = int(choice)
if 90 <= new_choice <= 100:   
    print("A")
elif 80 <= new_choice <= 89:    
    print("B")
elif 60 <= new_choice <= 79:    
    print("C")
elif 40 <= new_choice <= 59:    
    print("D")
elif 0 <= new_choice <= 39:    
    print("E")
else:    
    print("输入错误，请重新输入")
```





## day03 Python基础

**课程目标：掌握Python基础中的必备语法知识。**

**课程概要：**

- 循环语句
- 字符串格式化
- 运算符(面试题)



### 1.循环语句

- while循环
- for循环(后期)

```python
while 条件:    条件成立时执行的代码    条件成立时执行的代码代码执行完毕后回到 条件 部分，看是否满足条件，满足条件则继续执行代码，否则跳出while循环
```

```python
print("123")while 条件:    ...    ...    ...print("456")注意：如果此时while条件一直处于被满足的情况下时，则print("456")永远不会被执行
```



#### 1.1 循环语句基本使用

示例1：

```python
print("开始")# 可以直接使用布尔值while True:	print("Alex是个小逗比")print("结束")# 输出：开始Alex是个小逗比Alex是个小逗比Alex是个小逗比Alex是个小逗比.... 因True一直成立，所以---死循环
```

示例2：

```python
print("开始")# 可以直接使用判断语句while 1 > 2:	print("Alex是个小逗比")print("结束")# 输出：开始结束因条件判断后为False，所以直接退出while循环继续往下走。
```

示例3：

```python
# 使用变量当条件
data = True
print("start")
while data:
    print("如果祖国收到侵犯，热血男儿当自强")
print("end")

# 输出：
start
如果祖国收到侵犯，热血男儿当自强
如果祖国收到侵犯，热血男儿当自强
如果祖国收到侵犯，热血男儿当自强
...因True一直成立，所以---死循环
```

示例4：

```python
print("开始")
flag = True
while flag:
    print("滚滚黄河，滔滔长江")
    flag = False
print("结束")

# 输出：
开始
滚滚黄河，滔滔长江
结束
```

示例5：

```python
print("开始")
num = 1
while num < 3:
    print("滚滚黄河，滔滔长江")
    num = 5
print("结束")

# 输出：
开始
滚滚黄河，滔滔长江
结束
```

示例6：

```python
print("开始")
num = 1
while num < 5:
    print("滚滚黄河，滔滔长江")
    num = num + 1
print("结束")

# 输出：
开始
滚滚黄河，滔滔长江
滚滚黄河，滔滔长江
滚滚黄河，滔滔长江
滚滚黄河，滔滔长江
结束
```

```python
练习题：重复3次输出我爱我的祖国
# 解：
print("开始")
num = 1
while num < 4:    
    print("我爱我的祖国")    
num = num + 1
	print("结束")
```



#### 1.2 综合小案例

![image-20220106161319192](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220106161319192.png)



##### 练习题

1.补充代码实现

​	猜数字，设定一个理想数字比如：66，一直提示让用户输入数字，如果比66大，则显示猜测的结果大了，如果比66小，则显示猜测的结果小了，只有输入等于66，显示猜测结果正确，然后退出循环。

```python
number = 66
flag = True
while flag:
    ...
# 解：
number = 66
flag = True
while flag:
    input_number = input("请输入数字：")
    if int(input_number) == number:
        print("猜对啦")
        flag = False
    elif int(input_number) < number:
        print("猜小啦")
    else:
        print("猜大啦")
```

2.使用循环输出1~100所有整数

```python
number = 1
while number < 101:
    print(number)
    number = number + 1
```

3.使用循环输出1 2 3 4 5 6 8 9 10，即：10以内除7以外的整数。

```python
number = 0
while number < 10:
    number = number + 1
    if number == 7:
        continue
    print(number)
    
其他解法-1：
number = 1
while number < 11:
    if number == 7:
        pass
    else:
        print(number)
    number = number + 1

其他解法-2：
number = 1
while number < 11:
    if number != 7:
        print(number)
    number = number + 1
```

4.输出1~100内的所有奇数

```python
number = 0
while number < 100:
    if number % 2 == 1:
        print(number)
    number = number + 1
```

5.输出1~100内的所有偶数

```python
number = 0
while number < 100:
    number = number + 1
    if number % 2 == 0:
        print(number)
```

6.求1~100的所有整数的和

```python
total = 0
number = 1
while number < 101:
    total = total + number
    number = number + 1
    print(total)
```

7.输出10~1 所有整数

```python
number = 10
while number > 0:
    print(number)
    number = number - 1
```

思考题：求1~100以内的所有整数这样的结果：1 - 2 + 3 - 4 + 5 - 6 = ？



#### 1.3 break

break，用于在while循环中帮你终止循环。

```python
print("开始")
while True:
    print("1")
    break
    print("2")
print("结束")

# 输出：
开始
1
结束
```

示例1：

```python
print("开始")
while True:
    print("红旗飘飘，军号响。")
    break
    print("剑已出鞘，雷鸣电闪。")
    print("从来都是狭路相逢勇者胜")
print("结束")

# 输出:
开始
红旗飘飘，军号响。
结束
```

示例2：

```python
print("开始")
i = 1
while True:
    print(i)
    i = i + 1
	if i == 101:
        break
print("结束")

# 输出：
开始
1
2
3
...
100
结束
```

示例3：

```python
print("系统开始")
while True:
    user = input("请输入用户名：")
    pwd = input("请输入密码：")
    if user == 'chenmingbin' and pwd == '123':
        print("登录成功")
        break
    else:
        print("用户名或密码错误，登录失败")
print("系统结束")

# 输出：
系统开始
请输入用户名：
请输入密码：
登录成功
系统结束
```

所以，以后写代码的时候，想要结束循环可以通过两种方式实现，通过条件判断或break进行中断。



#### 1.4 Continue

Continue，在循环中用于 结束本次循环，开始下一次循环。

```python
print("开始")
while True:
    print(1)
    continue
    print(2)
    print(3)
print("结束")

# 输出：
开始
1
结束
```

![image-20220107153718991](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220107153718991.png)

![image-20220107153954572](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220107153954572.png)

#### 1.5 while else

![image-20220107154459407](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220107154459407.png)

![image-20220107154554242](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220107154554242.png)

### 2.字符串格式化

字符串格式化，使用跟便捷的形式实现字符串的拼接。

#### 2.1 %

##### 2.1.1 基本格式化操作

```python
name = "wupeiqi"
text = "我叫%s,今年18岁" % "武沛齐"
print(text)
# 输出：
我叫武沛齐,今年18岁
```

```python
name = "武沛齐"
age = 18
text = "我叫%s,今年%d岁" % (name,age)
print(text)

# 输出：
我叫武沛齐,今年18岁
```

```python
message = "%(name1)s你什么时候过来，%(name2)s今天不在家" % {"name1":"死鬼","name2":"Alex"}
print(message)

# 输出：
死鬼你什么时候过来，Alex今天不在家
```

```python
text = "我叫%s,今年%d岁"
data1 = text % ("武沛齐",18)
data2 = text % ("陈明彬",18)
```

##### 2.1.2 百分比

```python
text = "%s，这个片我已经下载了90%%，居然特么的断网了" % "兄弟"
print(text)

一旦字符串格式化中出现百分比的显示，请一定要加 %% 以实现输出 %
```



#### 2.2 format(推荐)

```python
text = "我叫{0},今年18岁".format("武沛齐")
# 输出
我叫武沛齐，今年18岁

text = "我叫{0},今年{1}岁".format("武沛齐",18)
# 输出
我叫武沛齐，今年18岁

text = "我叫{0},今年{1}岁，真实的姓名叫{0}".format("武沛齐",18)
# 输出：
我叫武沛齐，今年18岁，真实的姓名叫武沛齐
```

```python
text = "我叫{},今年18岁".format("武沛齐")

text = "我叫{0},今年{}岁".format("武沛齐",18)

text = "我叫{0},今年{1}岁，真实的姓名叫{}".format("武沛齐",18,"武沛齐")
```

```python
text = "我叫{name},今年{age}岁".format(name = "武沛齐",age = 18)

text = "我叫{name},今年{age}岁，真实的姓名叫{name}".format(name = "武沛齐",age = 18)
```

```python
text = "我叫{0},今年{1}岁"
data1 = text.format("武沛齐",18)
data2 = text.format("陈明彬",18)
```



#### 2.3 f

```python
text = f"嫂子喜欢{'跑步'}，跑完之后满身大汗"
```

```python
action = "跑步"
text = f"嫂子喜欢{action}，跑完之后满身大汗"
print(text)

# 输出：
嫂子喜欢跑步，跑完之后满身大汗
```

```python
name = "mm"
age = 17
text = f"嫂子的名字叫{name},今年{age}岁"
print(text)

# 输出：
嫂子的名字叫mm,今年17岁
```

 ```python
 text = f"嫂子的名字叫喵喵,今年{19 + 2}岁"
 print(text)
 
 # 输出：
 嫂子的名字叫喵喵,今年21岁
 ```

```python
# python3.8新引入
text = f"嫂子的名字叫喵喵,今年{19 + 2 = }岁"
print(text)

# 输出：
嫂子的名字叫喵喵,今年19 + 2 = 21岁
```

  ![image-20220207160852155](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207160852155.png)



### 3.运算符

![image-20220207160940153](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207160940153.png)

```python
if 1 > 2:
	pass
while 1 > 2:
	pass
data = 1 == 2
```

![image-20220207161216115](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207161216115.png)

![image-20220207163346066](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207163346066.png)

#### 3.1 运算符优先级

![image-20220207163705086](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207163705086.png)

#### 3.2 面试题

 ![image-20220207165105730](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207165105730.png)

##### 练习题

![image-20220207165234630](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207165234630.png)

```python
or:
v1 = 1
v2 = -1
v3 = -1
v4 = 100
v5 = 10
v6 = "wupeiqi"

and:
v1 = 8
v2 = 0
v3 = 88
v4 = ''
v5 = ''
v6 = ''
v7 = 0
```



##### 面试题

![image-20220207174723455](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207174723455.png)

```python
not 8 = False
```



#### 总结：

1.while语句

2.break和continue关键字的作用

3.三种字符串格式化的方式

4.基本运算符（逻辑运算涉及的相关面试题）



#### 今日作业：

![image-20220207175132755](C:\Users\14667\AppData\Roaming\Typora\typora-user-images\image-20220207175132755.png)













