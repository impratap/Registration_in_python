# Registration_in_python

This is a project for Employee Registration, Attendance and Leave record and Salary Calculation.

For this project I have used mysql for database...

We have three different file for registration, attendance & leave and salary calculation.

First we have registration.py for registraion...

for that we have used different library like.

from tkinter import *

from pymysql import *

from tkinter import ttk

from ttkthemes import themed_tk as tk

from tkinter import messagebox as msg

from lev_attendance import lev_attendance

from sal_cal import sal_cal

We have tkinter for GUI, pymysql for database, themed_tk for theme , messagebox for printing message, lev_attendence and sal_cal for using both these files...

After that created a class using frame from tkinter for label, button and text fields 
and than created a function for registraion 
and at last imported lev_attendence and sal_cal both files.

![regisd](https://user-images.githubusercontent.com/33418077/131963262-60e41baa-b514-404a-84c2-1195dc4da692.PNG)

if we enter wrong credentials or forget to enter data then it will through an error message.

![error](https://user-images.githubusercontent.com/33418077/131963928-3982b010-a9fe-4207-ab0a-4f9d085a448f.PNG)

Now in second file lev_attendence.py

I have imported some necessary library like 

from tkinter import *

from pymysql import *

from tkinter import messagebox as msg

from tkinter import ttk

from ttkthemes import themed_tk as tk

created a class for GUI like label, buton, and text fields and then a function for updation of Attendence and leave.

![la](https://user-images.githubusercontent.com/33418077/131966405-f6b993ba-3b1a-4a95-bbf6-bdc39df73c2f.PNG)

And the third and last file sal_cal.py for salary calculation

for that I have used some library like 

from tkinter import *

from pymysql import *

from tkinter import messagebox as msg

from tkinter import ttk

from ttkthemes import themed_tk as tk

And created a class using frame from tkinter for label, button and text fields and then a function for salary calculation...

![sal](https://user-images.githubusercontent.com/33418077/131966900-c73615d4-d318-4b4e-a056-82b6856c36ce.PNG)


