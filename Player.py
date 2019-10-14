from selenium import webdriver
# 导入 Select 类
from selenium.webdriver.support.ui import Select
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

window = tk.Tk()
window.title("VIP视频解析，仅用于学习研究")
window.geometry("400x250") #窗口大小
window.resizable(0,0)  #固定窗口大小
ft1 = tkFont.Font(size=20, slant=tkFont.ITALIC) #字体样式
ft2 = tkFont.Font(size=15, slant=tkFont.ITALIC) #字体样式
#图片背景
photo=tk.PhotoImage(file="大圣娶亲(勿删).png")
thePhoto=tk.Label(window,image=photo,compound = tk.CENTER,fg = "white")
thePhoto.pack()

tk.Label(window,text="播放地址:",font=ft2).place(x=35,y=90)
var_url = tk.StringVar()
# var_url.set("默认值")
entry_url = tk.Entry(window,width=33,textvariable=var_url,borderwidth=2) #输入框
entry_url.place(x=140,y=90)
# entry_url.BackColor=Color.Transparent

#下拉列表
tk.Label(window,text="播放通道:",font=ft2).place(x=35,y=140)
var_vip = tk.StringVar()
list1 = ttk.Combobox(window,width=30,textvariable=var_vip,state='readonly')
list1.place(x=140,y=140)
#创建下拉列表的值
list1["value"] = (
    "①号通用vip引擎系统【稳定通用】",
    "②号通用vip引擎系统【稳定通用】",
    "③号通用vip引擎系统【稳定通用】",
    "④号通用vip引擎系统【超级稳定通用】",
    "⑤号通用vip引擎系统【稳定通用】"
)
# 设置默认值 索引从0开始
list1.current(0)
def vip_list(event):
    vip = list1.get()
    return vip

list1.bind("<<ComboboxSelected>>",vip_list)

def get_info():
    #获取输入播放地址
    input_url = var_url.get()
    driver = webdriver.Chrome()
    #自定义窗口大小
    # driver.set_window_size(0,0)
    # 最小化窗口
    driver.minimize_window()
    url = 'http://www.qmaile.com'
    driver.get(url)
    #获取通道下拉列表
    select = Select(driver.find_element_by_id("jk"))
    #vip播放通道
    vip = var_vip.get()
    select.select_by_visible_text(vip)

    #输入播放地址
    driver.find_element_by_id("url").send_keys(input_url)
    #点击全屏解析
    driver.find_element_by_xpath('//*[@id="bf"][2]').click()
    windows = driver.window_handles
    driver.close()
    driver.switch_to.window(windows[1])
    driver.maximize_window()

# 按钮
btn = tk.Button(window,text="开始播放",font=ft1,command=get_info)
btn.place(x=130,y=190)
window.mainloop()


