import requests as req
import re
import tkinter as tk  # GUI 构建页面
import webbrowser

url = 'http://www.qmaile.com/'
responed = req.get(url)
responed.encoding = 'UTF-8'  # 将网页中的字符转码
# responed.encoding = responed.apparent_encoding  # 自动识别网页字符集
responeds = responed.text  # 获取网页代码

reg = re.compile('<option value="(.*?)" selected="">')
res = re.findall(reg, responeds)  # 参数一正则匹配内容，参数二目标文本正则皆返回列表类型[]

# 保存匹配到的数据
one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]

# 构建程序页面
# 用到了tkinter的Label标签,Radiobutton单选,Button按钮等组件
root = tk.Tk()
root.geometry('500x250')  # 小写x，不是*
root.title('在线获取影视资源')
L1 = tk.Label(root, text='播放接口:', font=12)  # 参数1:该label处于哪个窗口，参数2label的名称...其实就是属性设置
L1.grid()  # 设置组件位置，无参默认该字段行和列都是0

var = tk.StringVar()  # 存储用户选择接口url

r1 = tk.Radiobutton(root, text='播放接口1', variable=var, value=one)  # value的值将传给variable;即，将从网页解析接口one赋值给var
r1.grid(row=0, column=1)  # gui的行和列的下标都是从0开始的

r2 = tk.Radiobutton(root, text='播放接口2', variable=var, value=two)  # 单选框。可以针对每一个窗口的内容(按钮,单选多选)去设置属性(长宽高字体大小)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3', variable=var, value=three)
r3.grid(row=3, column=1)
r4 = tk.Radiobutton(root, text='播放接口4', variable=var, value=four)
r4.grid(row=4, column=1)
r5 = tk.Radiobutton(root, text='播放接口5', variable=var, value=five)
r5.grid(row=5, column=1)

L2 = tk.Label(root, text='播放链接:', font=12)  # 定义标签(描述)文字
L2.grid(row=6, column=0)  # Label会根据先后顺序会自动排序.但还是写一下好

el = tk.Entry(root, text='', width=55)  # 用户输入的文本框
el.grid(row=6, column=1)


def bf():  # 将获取的播放接口和用户输入的网址组合成一个url
    webbrowser.open(var.get() + el.get())


def clear():  # 清除文本框中从所有内容
    el.delete(0, "end")


b1 = tk.Button(root, text="播放", font=12, width=8, command=bf)  # 按钮 绑定播放事件
b1.grid(row=7, column=1)

b2 = tk.Button(root, text="清除", font=12, width=8, command=clear)
b2.grid(row=8, column=1)  # 位置为 第7行第2列,下标始于0

# 制作菜单
menubar = tk.Menu(root) # 实例化菜单项
helpmenu = tk.Menu(menubar, tearoff=0)  # 在这个菜单上生成子菜单(实例化)
menubar.add_cascade(label='帮助(H)', menu=helpmenu)   # 增加一个主要菜单选项(一级菜单)
helpmenu.add_command(label='帮助文档')   # (二级菜单)
helpmenu.add_command(label='作者信息')  # 把子菜单添加进去。没有实现调用函数，可以尝试实现，想怎么写都行
root.config(menu=menubar)   # 把菜单配置进去

root.mainloop()  # 在页面的属性设置ok后使主界面一直存在.如果在设置属性前调用，界面将会无法加载属性,因为属性还没被加载

