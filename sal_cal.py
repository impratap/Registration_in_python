from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
from tkinter import ttk
from ttkthemes import themed_tk as tk

class sal_cal(Frame):
    def __init__(self,m):
        super().__init__(m)
        
       
        
        self.la=ttk.Label(self,text='Salary Information',font=('calibri',14,'bold'))
        self.la.grid(row=0,columnspan=2,pady=15)
        
        self.Empid=ttk.Label(self,text='Employee Id',font=('calibri',14,'bold'))
        self.Empid.grid(row=1,column=0)
        self.emt=ttk.Entry(self,justify='center')
        self.emt.grid(row=1,column=1)
        
        self.sal=ttk.Label(self,text='Salary Rate',font=('calibri',14,'bold'))
        self.sal.grid(row=2,column=0)
        self.salt=ttk.Entry(self,justify='center')
        self.salt.grid(row=2,column=1)
        
        self.sbtn=ttk.Button(self,text='Submit',command=self.salary)
        self.sbtn.grid(row=3,columnspan=2) 
        self.pack()
        
    def salary(self):
        salaries=0
        con=connect(host='localhost',db='students',user='root',passwd='root')
        cur=con.cursor()
        try:
            eid=int(self.emt.get())
            cur.execute("select attendance from emp where empid=%d"%(eid))
            result=cur.fetchone()
            rate=int(self.salt.get())
            salaries=result[0]*rate
            self.emt.delete(0,'end')
            self.salt.delete(0,'end')
            self.emt.focus()
            msg.showinfo('Salary',salaries)
            i=cur.execute("update emp set salary=%d where empid=%d "%(salaries,eid))
            if i==1:
                con.commit()
                msg.showinfo('Information','Salary updated !')
        except:
            msg.showinfo('Error','Please enter correct enter!')
        
