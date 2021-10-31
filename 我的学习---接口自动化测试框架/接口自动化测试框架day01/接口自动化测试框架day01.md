# 接口自动化测试框架day01

————————————————————————————————————————————————————————————

## 一、接口测试以及接口自动化的行业

目前主流：（只适用于中小型的项目）

Postman+Newman+Git/Svn+Jenkins

Jmeter+Ant+Git/Svn+Jenkins

弊端：

1.敏捷开发时代，接口数量巨大，工具无法做到团队协作和版本控制。

2.功能写死了，对于一些复杂的接口（自定义加密以及签名接口）

3.项目里面有多重协议的接口：http、webservice、websocket、dubbo

4.拍错，定位问题不够便利

5.跟甲方对接时没有美观的HTML报告

6.多借口串联，数据库连接和日志监控都不能做

7.有些公司既要做接口自动化，又要做WEB自动化，接口+WEB结合。



## 二、Requests库简介

python第三方库，主要用于做接口自动化测试。

安装命令：pip install requests



Json.loa						把json转化成dict类型

Json.dumps				把dict类型转化成字符串

## 三、全面的认识requests库

```
requests.get()		get请求，通过params传参
	1.params传参：参数是dict类型
requests.post()		post请求，通过data或json传参
	1.使用data传参：参数是dict类型，那么请求头Content-Type：application/x-www-urlencoded.表示通过表单传参
		格式：a=1&b=2 --- 参数是str类型：Content-Type：Text/plain
	2.使用json传参：不管参数是dict或str、Content-Type：application/json
		格式：{“a”：“1”，“b”：“2”}
	总结：data传参只能传键值对的dict，要么就传str格式；json传参一般都是dict，可以是键值对也可以是非键值对。
		注：键值对：一个key对标一个value；非键值对：有list也有dict
	重要的请求头：
		Content-Type：传参的内容格式
			1.Content-Type：application/x-www-urlencoded --- 表单格式
			2.Content-Type：multipart/form-data --- 表单里面有文件上传
			3.Content-Type：text/plain --- 文本
			4.Content-Type：binary --- 二进制文件
		Accept：客户端接收的数据格式
		X-Requested-With：异步请求
		User-Agent：客户端的用户类型
		Cookie：Cookie信息
			
requests.put()		
requests.delete()
requests.request()		可以发送所有请求
```



## 四、全面的认识response

```
print(respones.json())			把返回值转化成一个dict对象
print(respones.text)			把返回值转化成文本
print(respones.content)			把返回值转化成字节类型
print(respones.status_code)		返回一个返回码
print(respones.reason)			返回信息
print(respones.cookies)			返回cookie信息
print(respones.encoding)		编码格式
print(respones.headers)			响应头
print(respones.request.method)	request包含所有请求数据
```



## 五、认识pytest

默认的