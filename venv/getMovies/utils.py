import requests as req
import re
import tkinter as tk  # GUI 构建页面

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
root = tk.Tk()
root.geometry('500x250')
root.title('在线获取影视资源')
L1 = tk.Label(root, text='播放接口:', font=12)  # 参数1组件处于哪个窗口，参数2组件的名称...其实就是属性设置
L1.grid()  # 设置组件位置，无参默认该字段行和列都是0
r1 = tk.Radiobutton(root, text='播放接口1')
r1.grid(row=0, column=1)  # gui的行和列的下标都是从0开始的

r2 = tk.Radiobutton(root, text='播放接口2')  # 可以针对每一个窗口的内容(按钮,单选多选)去设置属性(长宽高字体大小)
r2.grid(row=1, column=1)
r3 = tk.Radiobutton(root, text='播放接口3')
r3.grid(row=3, column=1)
r4 = tk.Radiobutton(root, text='播放接口4')
r4.grid(row=4, column=1)
r5 = tk.Radiobutton(root, text='播放接口5')
r5.grid(row=5, column=1)

L2 = tk.Label(root, text='播放链接:', font=12)
L2.grid(row=6, column=0)  # Label会根据先后顺序会自动排序.但还是写一下好

el = tk.Entry(root, text='', width=55)
el.grid(row=6, column=1)

b1 = tk.Button(root, text="播放", font=12) # 播放按钮
b1.grid(row=7, column=1)


root.mainloop()  # 在页面的属性设置ok后使主界面一直存在.如果在设置属性前调用，界面将会无法加载属性,因为属性还没被加载
