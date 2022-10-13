import re

ls='''
.        匹配换行符以外的任意字符
\w       匹配字母或数字或下划线
\s       匹配任意的空白符
\d       匹配数字
\n       匹配一个换行符
\t       匹配一个制表符
^        匹配一个字符串的开始
$        匹配字符串的结尾
\W       匹配非字母或数字或下划线
\D       匹配非数字
\S       匹配非空白符
a|b      匹配字符a或字符b
()       匹配括号内的表达式，也表示一个组
[...]    匹配字符组中的字符
[^...]   匹配除了字符组中的所有字符
'''
ls2='''
*     重复零次或更多次
+     重复一次或更多次
？    重复零次或一次
{n}   重复n次
{n,}  重复n次或更多次
{n,m} 重复n次到m次
'''
ls3='''
.*    贪婪匹配（匹配最长的一条）
.*?   惰性匹配（匹配最短的一条）
'''
# findall:匹配字符串中所有符合正则的内容
lst = re.findall(r"\d+", "我的电话号码是10086，我女朋友的电话号码是:10010")
for i in lst:
    print(i)
print(lst[0],lst[1])

# finditer 和findall差不多，只不过返回的是迭代器
it = re.finditer(r"\d+", "我的电话号码是10086，我女朋友的电话号码是:10010")
for i in it:
    print(i.group())

# search:找到一个结果就返回，返回的是一个match对象，拿数据需要.group()
s = re.search(r"\d+", "我的电话号码是10086，我女朋友的电话号码是:10010")
print(s.group())

#预加载正则表达式当正则表达式过长时，我们可以使用预加载正则表达式，将要寻找的正则表达式格式储存住，
# 调用时可以用不同的字符串，相当于用一种匹配格式匹配多次字符串，不用我们每次都去编写匹配格式，
# 而且将匹配格式和待匹配语句分开写代码看起来更加整洁。
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号码是10086，我女朋友的电话号码是:10010")
print(ret)
for i in ret:
    print(i.group())

ret = obj.findall("我的电话号码是10086，我女朋友的电话号码是:10010")
print(ret)

#可以单独从正则匹配内容中单独匹配内容
s = '''
<div class='赘婿'><span id='女主'>宋轶</span></div>
<div class='赘婿'><span id='男主'>郭麒麟</span></div>
'''
# re.S让.可以匹配换行符
obj = re.compile(r"<div class='.*?'><span id='.*?'>.*?</span></div>", re.S)
ret = obj.finditer(s)
for i in ret:
    print(i.group())

#
s2 = '''
<div class='赘婿'><span id='女主'>宋轶</span></div>
<div class='赘婿'><span id='男主'>郭麒麟</span></div>
'''
# re.S让.可以匹配换行符
obj2 = re.compile(r"<div class='(?P<class>.*?)'><span id=(?P<id>'.*?')>(?P<name>.*?)</span></div>", re.S)
ret2 = obj2.finditer(s2)
for i in ret2:
    print(i.group("class"),end="")
    print(i.group("id"))
    print(i.group("name"))


