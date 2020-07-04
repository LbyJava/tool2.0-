import tkinter as tk
from tkinter import *
import tkinter.messagebox

import urllib.request
from http import cookiejar
from http import cookies
from urllib import parse
import json
import time

import os

#爬虫
def pacong(id,tokenww):
        tokenw = tokenww.split('\n')[0]
        url = 'https://crm.gooeto.com:808/api/Phone/GetCallRecord'
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
            'Token':tokenw
        }

        
        values = {
            'CellDate':'2020-07-03',
            'ManageName':'杨波',
            'CustomerName':'',
            'Type':'呼出',
            'Number':'',
            'pageIndex':1,
            'pageSize':'30'
        }

        data = urllib.parse.urlencode(values).encode('utf-8')
        request = urllib.request.Request(url, data, headers)

        html = urllib.request.urlopen(request).read().decode('utf-8')

        parsed_json = json.loads(html)

        text = json.loads(html)
        #print(text)
        return json.loads(html)

#按钮点击事件
def __repr__(self):
        return repr(self.__dict__)

def butonck():
    data = pacong(2,TokenText.get(1.0,END))
    Rows = data['Data']['Rows']
    for index in range(len(Rows)):
           print(index)
           Number = Rows[index]['Number']
           CustomerName = Rows[index]['CustomerName']
           ManageName = Rows[index]['ManageName']
           Duration = Rows[index]['Duration']
           if(Number!=None):
                   print(Number)
                   resultEntry.insert(1.0,Number)
                   resultEntry.insert(1.0,CustomerName)
                   resultEntry.insert(1.0,Duration)
                   resultEntry.insert(1.0,ManageName)
                   resultEntry.insert(1.0,'\n')
   
def ltime():
    userId = idEntry.get(1.0,END)
    userIdList = userId.split("\n");
    strCuttingNO(userIdList)
    #form.withdraw()
    # now it stays on the clipboard after the window is closed
    #

def strCutting(userIdList):
        for index in range(len(userIdList)):
                if(userIdList[index]!=''):
                        var = len(userIdList)-3-index
                        Data = pacong(userIdList[var],TokenText.get(1.0,END))
                        LastVisitDateList = Data['Data']['List'][0]['LastVisitDate']
                        LastVisitDateT = LastVisitDateList.split("T")[0];
                        LastVisitDate = LastVisitDateT.replace("-", "/");
                        srt= "客户编号/客户姓名 "+Data['Data']['List'][0]['Number']+'/'+Data['Data']['List'][0]['Name']+" 销售姓名："+Data['Data']['List'][0]['ManageUserName']+'\n'
                        resultEntry.insert(1.0,srt)
                        xiaoShouEntry.insert(1.0,LastVisitDate+'\n')

                        
def strCuttingNO(userIdList):
        for index in range(len(userIdList)):
                if(userIdList[index]!=''):
                        var = len(userIdList)-3-index
                        Data = pacong(userIdList[var],TokenText.get(1.0,END))
                        LastVisitDateList = Data['Data']['List'][0]['LastVisitDate']
                        LastVisitDateT = LastVisitDateList.split("T")[0];
                        LastVisitDate = LastVisitDateT.replace("-", "/");
                        xiaoShouEntry.insert(1.0,LastVisitDate+'\n')


#创建一个窗口对象
form= tk.Tk()
#设置窗口名称
form.wm_title("我的记事本")
#窗口大小 长高用小写x隔开
form.geometry("370x850")
#窗口基于屏幕的坐标 +x轴+y轴
form.geometry("+1150+0")
#创建输入框对象
idEntry=Text(form,width=10, height=20)
xiaoShouEntry = Text(form,width=20, height=20)
zhuGuanEntry = Text(form,width=30, height=1)
TokenText = Text(form,width=30, height=1)
#加入提示文本
cId=tk.Label(form,text="客户编号")
XiaoShou=tk.Label(form,text="最后更进日期")
zhuGuan=tk.Label(form,text="主管姓名")
#将创建的控件加入到窗口中
cId.grid(row=1, column=1,  columnspan=1)
idEntry.grid(row=2, column=1,  columnspan=1)
XiaoShou.grid(row=1, column=2,  columnspan=2)
xiaoShouEntry.grid(row=2, column=2,  columnspan=2)
zhuGuan.grid(row=4, column=1,columnspan=1)
zhuGuanEntry.grid(row=4, column=2,  columnspan=3)
miyao = tk.Label(form,text="键入秘钥")
miyao.grid(row=5, column=1,  columnspan=1)
TokenText.grid(row=5, column=2,  columnspan=3)
#创建一个按钮
c=tk.Button(form,text="确定",command=butonck)
c.grid(row=6, column=1, columnspan=1)

#创建一个按钮
timeb=tk.Button(form,text="查询最后更进日期",command=ltime)
timeb.grid(row=6, column=2, columnspan=1)

resultEntry=Text(form,width=60, height=50)
resultEntry.grid(row=7, column=1, columnspan=5)
form.wm_attributes('-topmost',1)
form.mainloop()

#r = Tk()

