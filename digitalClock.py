from tkinter import *
import datetime

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    mi=time.strftime("%M")
    se=time.strftime("%S")
    am=time.strftime("%p")
    date=time.strftime("%d")
    month=time.strftime("%m")
    year=time.strftime("%y")
    day=time.strftime("%a")




    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=se)
    lab_am.config(text=am)
    
    lab_date.config(text=date)
    lab_mo.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)



    lab_hr.after(200,date_time)




clock=Tk()
clock.title('****DIGITAL-CLOCK****')
clock.geometry('1000x500')
clock.config(bg='#5DE2E7')

# time

lab_hr=Label(clock,text="00",font=("Time New Roman",60,"bold",),
             bg='#EFC3CA',fg="white")
lab_hr.place(x=120,y=45,height=110,width=100)

lab_hr_txt=Label(clock,text="HOUR",font=("Time New Roman",22,"bold",),
             bg='#EFC3CA',fg="white")
lab_hr_txt.place(x=120,y=190,height=40,width=100)




lab_min=Label(clock,text="00",font=("Time New Roman",60,"bold",),
             bg='#EFC3CA',fg="white")
lab_min.place(x=340,y=45,height=110,width=100)
lab_min_txt=Label(clock,text="MIN",font=("Time New Roman",22,"bold",),
             bg='#EFC3CA',fg="white")
lab_min_txt.place(x=340,y=190,height=40,width=100)


lab_sec=Label(clock,text="00",font=("Time New Roman",60,"bold",),
             bg='#EFC3CA',fg="white")
lab_sec.place(x=560,y=45,height=110,width=100)
lab_sec_txt=Label(clock,text="SEC",font=("Time New Roman",22,"bold",),
             bg='#EFC3CA',fg="white")
lab_sec_txt.place(x=560,y=190,height=40,width=100)




lab_am=Label(clock,text="00",font=("Time New Roman",50,"bold",),
             bg='#EFC3CA',fg="white")
lab_am.place(x=780,y=45,height=110,width=100)

lab_am_txt=Label(clock,text="AM/PM",font=("Time New Roman",22,"bold",),
             bg='#EFC3CA',fg="white")
lab_am_txt.place(x=780,y=190,height=40,width=100)




# date

lab_date=Label(clock,text="00",font=("Time New Roman",60,"bold",),
             bg='#EFC3CA',fg="white")
lab_date.place(x=120,y=270,height=110,width=100)

lab_date_txt=Label(clock,text="DATE",font=("Time New Roman",22,"bold",),
             bg='#EFC3CA',fg="white")
lab_date_txt.place(x=120,y=410,height=40,width=100)


lab_mo=Label(clock,text="00",font=("Time New Roman",60,"bold",),
             bg='#EFC3CA',fg="white")
lab_mo.place(x=340,y=270,height=110,width=100)
lab_mo_txt=Label(clock,text="MONTH",font=("Time New Roman",18,"bold",),
             bg='#EFC3CA',fg="white")
lab_mo_txt.place(x=340,y=410,height=40,width=100)




lab_year=Label(clock,text="00",font=("Time New Roman",60,"bold",),
             bg='#EFC3CA',fg="white")
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_txt=Label(clock,text="YEAR",font=("Time New Roman",22,"bold",),
             bg='#EFC3CA',fg="white")
lab_year_txt.place(x=560,y=410,height=40,width=100)



lab_day=Label(clock,text="00",font=("Time New Roman",35,"bold",),
             bg='#EFC3CA',fg="white")
lab_day.place(x=780,y=270,height=110,width=100)

lab_day_txt=Label(clock,text="DAY",font=("Time New Roman",21,"bold",),
             bg='#EFC3CA',fg="white")
lab_day_txt.place(x=780,y=410,height=40,width=100)









date_time()











clock.mainloop()