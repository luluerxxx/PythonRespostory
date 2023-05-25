import pymysql
import tkinter as tk
import pandas as pd
from tkinter import messagebox
#创建链接
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', charset='utf8', db='mydatabase')

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()

        self.createWidgets()

    def createWidgets(self):
        self.topLabel = tk.Label(self, text='欢迎来到通讯录程序！', font=('Helvetica', 20, 'bold'))
        self.scoLabel = tk.Label(self, text='请您选择您要进行的操作：', font=('Helvetica', 13, 'bold'))
        self.topLabel.grid(row=0, column=0, columnspan=8)
        self.scoLabel.grid(row=1, column=0, columnspan=6)
        self.btnAdd = tk.Button(self, text='添加联系人', command=self.funcAdd)
        self.btnChange = tk.Button(self, text='修改联系人', command=self.funcCha)
        self.btnDel = tk.Button(self, text='删除联系人', command=self.funcDel)
        self.btnSear = tk.Button(self, text='查询联系人', command=self.funcSea)
        self.btnAdd.grid(row=2, column=0, pady=30)
        self.btnChange.grid(row=2, column=4, pady=30)
        self.btnDel.grid(row=3, column=0)
        self.btnSear.grid(row=3, column=4)
        self.btnOk = tk.Button(self, text='退出通讯录', command=self.funcOk)
        self.btnOk.grid(row=4, column=2, pady=10)

    def funcAdd(self):
        A = AddContact(self)

    def funcCha(self):
        C = ChangeContact(self)

    def funcDel(self):
        D = DelContact(self)

    def funcSea(self):
        S = SearContact(self)

    def funcOk(self):
        self.destroy()

# 创建一个添加联系人信息的类
class AddContact:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.geometry("500x300+500+200")
        self.topLabel = tk.Label(self.top, text='欢迎来到添加联系人页面！', font=('Helvetica', 20, 'bold'))
        self.topLabel.grid(row=0, column=1, columnspan=8)
        self.lalname = tk.Label(self.top, text='请输入姓名：')
        self.lalsex = tk.Label(self.top, text='请输入性别：')
        self.laltel = tk.Label(self.top, text='请输入电话号码：')
        self.lalvxnum = tk.Label(self.top, text='请输入微信号：')
        self.lalname.grid(row=1, column=0)
        self.lalsex.grid(row=2, column=0)
        self.laltel.grid(row=3, column=0)
        self.lalvxnum.grid(row=4, column=0)
        self.entryname = tk.Entry(self.top)
        self.entrysex = tk.Entry(self.top)
        self.entrytel = tk.Entry(self.top)
        self.entryvx = tk.Entry(self.top)
        self.entryname.grid(row=1, column=1)
        self.entrysex.grid(row=2, column=1)
        self.entrytel.grid(row=3, column=1)
        self.entryvx.grid(row=4, column=1)
        self.btnSave = tk.Button(self.top, text='保存', command=self.funcSave)
        self.btnSave.grid(row=5, column=0)

    def funcSave(self):
        name_a = self.entryname.get()
        sex_a = self.entrysex.get()
        tel_a = self.entrytel.get()

        if len(tel_a) == 13 and str.isdigit(tel_a) == 1:
            vx_a = self.entryvx.get()
            with conn.cursor() as cursor:
                sql = "INSERT INTO contact(name,sex,tel,vxnum) VALUES('%s','%s','%s','%s') "

                str2 = "恭喜您！添加联系人" + name_a + "的信息成功！"
                tk.messagebox.showinfo("通知页面", str2)
                cursor.execute(sql % (str(name_a), str(sex_a), str(tel_a), str(vx_a)))
                conn.commit()
                cursor.close()
        else:
            str1 = "请确认您输入的电话号码为13位有效数字！"
            tk.messagebox.showinfo("警告页面", str1)


# 创建一个修改联系人信息的类
class ChangeContact:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.geometry("500x300+500+200")
        self.topLabel = tk.Label(self.top, text='欢迎来到修改联系人页面！', font=('Helvetica', 20, 'bold'))
        self.topLabel.grid(row=0, column=1, columnspan=8)
        self.lalname = tk.Label(self.top, text='联系人的姓名：')
        self.lalname2 = tk.Label(self.top, text='修改后的姓名：')
        self.lalsex = tk.Label(self.top, text='修改后的性别：')
        self.laltel = tk.Label(self.top, text='修改后的电话号码：')
        self.lalvx = tk.Label(self.top, text='修改后的微信号：')
        self.lalname.grid(row=1, column=0)
        self.lalname2.grid(row=2, column=0)
        self.lalsex.grid(row=3, column=0)
        self.laltel.grid(row=4, column=0)
        self.lalvx.grid(row=5, column=0)
        self.entryname = tk.Entry(self.top)
        self.entryname2 = tk.Entry(self.top)
        self.entrysex = tk.Entry(self.top)
        self.entrytel = tk.Entry(self.top)
        self.entryvx = tk.Entry(self.top)
        self.entryname.grid(row=1, column=1)
        self.entryname2.grid(row=2, column=1)
        self.entrysex.grid(row=3, column=1)
        self.entrytel.grid(row=4, column=1)
        self.entryvx.grid(row=5, column=1)
        self.btnSave = tk.Button(self.top, text='保存', command=self.funcSave)
        self.btnSave.grid(row=6, column=0)

    def funcSave(self):
        name_c = self.entryname.get()
        flag = 0
        name_c1 = self.entryname2.get()
        sex_c = self.entrysex.get()
        tel_c = self.entrytel.get()
        vx_c = self.entryvx.get()
        with conn.cursor() as cursor:
            sql = "UPDATE contact SET name= '{}',sex='{}',tel='{}',vxnum='{}'  WHERE name = '{}'".format(name_c1, sex_c,tel_c, vx_c,name_c)
            cursor.execute(sql)
            conn.commit()
            str3 = "恭喜您！修改联系人" + name_c1 + "的信息成功！"
            tk.messagebox.showinfo("通知页面", str3)
            cursor.close()





# 创建一个删除联系人的类
class DelContact:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.geometry("500x300+500+200")
        self.topLabel = tk.Label(self.top, text='欢迎来到删除联系人页面！', font=('Helvetica', 20, 'bold'))
        self.topLabel.grid(row=0, column=1, columnspan=8)
        self.lalname = tk.Label(self.top, text='请输入删除的联系人的姓名：')
        self.lalname.grid(row=1, column=0)
        self.entryname = tk.Entry(self.top)
        self.entryname.grid(row=1, column=1)
        self.btnOk = tk.Button(self.top, text='确认', command=self.funcSave)
        self.btnOk.grid(row=2, column=0)

    def funcSave(self):
        name_d = self.entryname.get()
        with conn.cursor() as cursor:
            sql = "DELETE FROM contact WHERE name = '{}'".format(name_d)
            cursor.execute(sql)
            conn.commit()
            str3 = "恭喜您！删除联系人" + name_d + "的信息成功！"
            tk.messagebox.showinfo("通知页面", str3)
            cursor.close()

# 创建一个查询联系人的类
class SearContact:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.geometry("500x300+500+200")
        self.topLabel = tk.Label(self.top, text='欢迎来到查询联系人页面！', font=('Helvetica', 20, 'bold'))
        self.topLabel.grid(row=0, column=1, columnspan=8)
        self.lalname = tk.Label(self.top, text='请输入删除的联系人的姓名：')
        self.lalname.grid(row=1, column=0)
        self.entryname = tk.Entry(self.top)
        self.entryname.grid(row=1, column=1)
        self.btnOk = tk.Button(self.top, text='确认', command=self.funcSave)
        self.btnOk.grid(row=2, column=0)

    def funcSave(self):
        name_s = self.entryname.get()
        with conn.cursor() as cursor:
            sql = "SELECT * FROM contact WHERE name= '{}'".format(name_s)
            cursor.execute(sql)
            results = cursor.fetchall()
            tk.messagebox.showinfo("信息页面", results)
            # print(results)
            cursor.close()

root = tk.Tk()
root.title('通讯录程序')
root.geometry("500x300+500+200")
app = Application(master=root)
app.mainloop()



