from tkinter import *
from pymysql import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from tkinter import messagebox as msg
from lev_attendance import lev_attendance
from sal_cal import sal_cal

 
class registration(Frame):
    def __init__(self,register):
        super().__init__(register)
        
            
        self.erf=ttk.Label(self,text='Employee Registration Form',font=('calibri',14,'bold'))
        self.erf.grid(row=0,columnspan=2,pady=15)
        
        self.Empid=ttk.Label(self,text='Employee Id',font=('calibri',14,'bold'))
        self.Empid.grid(row=1,column=0)
        self.empt=ttk.Entry(self,justify='center')
        self.empt.grid(row=1,column=1)
        
        self.Empname=ttk.Label(self,text='Employee Name',font=('calibri',14,'bold'))
        self.Empname.grid(row=2,column=0)
        self.empntext=ttk.Entry(self,justify='center')
        self.empntext.grid(row=2,column=1)
        
        self.Emailid=ttk.Label(self,text='Employee Email',font=('calibri',14,'bold'))
        self.Emailid.grid(row=3,column=0)
        self.emailidt=ttk.Entry(self,justify='center')
        self.emailidt.grid(row=3,column=1)
        
        self.edept=ttk.Label(self,text='Employee Department',font=('calibri',14,'bold'))
        self.edept.grid(row=4,column=0)
        self.edeptt=ttk.Entry(self,justify='center')
        self.edeptt.grid(row=4,column=1)
        
        self.pack()
        
        '''self.sta=Label(self,text='Status',fg='dark orange',font=('calibri',14,'bold'))
        self.sta.grid(row=4,column=0)
        
        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        self.c1 = Checkbutton(self, text = "Married", variable = CheckVar1, fg='orange',font='bold')
        self.c1.grid(row=4,column=1)
        self.c2 = Checkbutton(self, text = "Single", variable = CheckVar2, fg='orange',font='bold')
        self.c2.grid(row=4,column=2)'''
        
           
        self.rbtn=ttk.Button(self,text='Register Employee',command=self.register_emp)
        self.rbtn.grid(row=5,columnspan=2)
        
        self.opt=ttk.Label(self,text='Do you want to check other options')
        self.opt.grid(row=6,columnspan=2,sticky=W+E)
        
        self.abtn=ttk.Button(self,text='Update leave and Attend.',command=self.lev_att)
        self.abtn.grid(row=7,column=0)
        
        self.rbtn=ttk.Button(self,text='Salary calculate',command=self.sal)
        self.rbtn.grid(row=7,column=1)
        
        
        
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=5,pad=10)
        self.rowconfigure(index=6,pad=10)
        self.rowconfigure(index=7,pad=10)
        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)
    
    def register_emp(self):
        con=connect(db='students',user='root',passwd='root',host='localhost')
        cur=con.cursor()
        try:
            empid=int(self.empt.get())
            ena=self.empntext.get()
            em=self.emailidt.get()
            ed=self.edeptt.get()
            i=cur.execute("insert into emp (empid,ename,email,empdepartment) values(%d,'%s','%s','%s') "%(empid,ena,em,ed))
            if i==1:
                con.commit()
                self.empt.delete(0,'end')
                self.empntext.delete(0,'end')
                self.emailidt.delete(0,'end')
                self.edeptt.delete(0,'end')
                self.empt.focus()
                msg.showinfo('Registration Information','Employee Registration Successful!')
        except:
            msg.showinfo('Error','Please enter correct entry !')
            
    def lev_att(self):
        root=tk.ThemedTk() # This is for Frame or structure where we all stuffs put and work... 
        root.get_themes()
        root.set_theme("radiance")
        root.iconbitmap(r'employee.ico')
        fr=lev_attendance(root)
        root.title('Leave and Attendance')
        root.geometry('350x200')
        root.mainloop()
    
    def sal(self):
        
        root=tk.ThemedTk() # This is for Frame or structure where we all stuffs put and work... 
        root.get_themes()
        root.set_theme("radiance")
        root.iconbitmap(r'employee.ico')
        fr=sal_cal(root)
        root.title('Salary Calculation')
        root.geometry('300x200')
        root.mainloop()  

root=tk.ThemedTk() # This is for Frame or structure where we all stuffs put and work... 
root.get_themes()
root.set_theme("radiance")
root.iconbitmap(r'employee.ico')
frm = registration(root)
root.title('Registration Form')
root.geometry('450x350')
root.mainloop()
        