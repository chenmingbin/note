# 接口自动化测试框架day02



## 一.Pytest默认的测试用例规则

1.模块名必须以test_ 开头 或  test_ 结尾

2.测试类必须以Test开头

3.测试方法必须test_开头

4.发现测试用例：从多个py文件里面找到我们的测试用例

5.执行测试用例：按一定的顺序执行，并且生成报告

6.判断测试结果：断言

7.生成测试报告：allure报告



## 二.pytest详细介绍

1.pytest它是一个成熟的python单元测试框架

2.它能够和自动化测试工具，selenium、requests、appium结合实现自动化

3.skip跳过用例，reruns失败用例重跑，多线程

4.pytest和allure生成美观的测试报告

5.它结合jenkins实现持续集成

6.pytest有很多插件：

​		pytest 							 本身

​		pytest-html					生成html报告的插件

​		pytest-xdist					实现多线程

​		pytest-ordering			 改变测试用例的执行顺序

​		pytest-rerunfailures	 失败用例重跑

​		allure-pytest				  生成allure报告

​	可以把以上常用插件丢到requirements.txt文件里面 直接 “pip install requirements.txt”  一次性安装



## 三.pytest的运行方式

### 1.main()方法运行

```
if __name__ == '__main__':
    pytest.main()
```



### 2.命令行运行

pytest -vs		详细信息

-n					多线程

--reruns			失败用例重跑





### 3.pytest.ini 配置文件

[pytest]					# 注明这是pytest

addopts = vs -m "smoke or users"

testpaths = ./testcases

python_files = aaa_*.py

python_classes = Test*

python_functions = test*

markers = 

​		smoke:冒烟测试

​		users:用户管理用例

​	



## 4.pytest前后置

### 1.fixtrue

scope 			作用域			

params			数据驱动

autouse			自动执行

ids						数据驱动参数名

name				给fixture作用的函数重命名



2.

