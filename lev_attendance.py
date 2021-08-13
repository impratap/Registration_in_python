from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
from tkinter import ttk
from ttkthemes import themed_tk as tk



class lev_attendance(Frame):
    def __init__(self,m):
        super().__init__(m)
        
        self.la=ttk.Label(self,text='Leave and Attendance',font=('calibri',14,'bold'))
        self.la.grid(row=0,columnspan=2,pady=15)
        
        self.Empid=ttk.Label(self,text='Employee Id',font=('calibri',14,'bold'))
        self.Empid.grid(row=1,column=0)
        self.emt=ttk.Entry(self,justify='center')
        self.emt.grid(row=1,column=1)
        
        self.leave=ttk.Label(self,text='Employee Leave',font=('calibri',14,'bold'))
        self.leave.grid(row=2,column=0)
        self.leavetext=ttk.Entry(self,justify='center')
        self.leavetext.grid(row=2,column=1)
        
        self.atten=ttk.Label(self,text='Employee Attendance',font=('calibri',14,'bold'))
        self.atten.grid(row=3,column=0)
        self.attent=ttk.Entry(self,justify='center')
        self.attent.grid(row=3,column=1)
        
        self.sbtn=ttk.Button(self,text='Submit',command=self.lev_att)
        self.sbtn.grid(row=4,columnspan=2)
        
        self.pack()
        
    def lev_att(self):
        lev=0
        att=0
        con=connect(host='localhost',db='students',user='root',passwd='root')
        cur=con.cursor()
        try:
            eid=int(self.emt.get())
            lev=int(self.leavetext.get())
            att=int(self.attent.get())
            i=cur.execute("update emp set eleave=%d, attendance=%d where empid=%d"%(lev,att,eid))
            if i==1:
                con.commit()
                self.emt.delete(0,'end')
                self.leavetext.delete(0,'end')
                self.attent.delete(0,'end')
                self.emt.focus()
                msg.showinfo('Update Information','Leave and Attendance updated!')
        except:
            msg.showinfo('Error','Please enter correct enter!')
            

