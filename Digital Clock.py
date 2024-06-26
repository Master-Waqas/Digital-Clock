from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")

    lab_hr.config(text = hr)
    lab_min.config(text = min)
    lab_sec.config(text = sec)
    lab_am.config(text = am)
    lab_date.config(text = date)
    lab_month.config(text = month)
    lab_year.config(text = year)
    lab_day.config(text = day)
    lab_hr.after(200, date_time)


clock = Tk()
clock.title("**** Digital Clock ****")
clock.geometry("1000x500")
clock.config(bg = "yellow")

# ************** Time
# Hour
lab_hr = Label(clock, text = "00", font = ("times new roman", 40, "bold"),
               bg = "red", fg = "white")
lab_hr.place(x = 120, y = 50, height = 110, width = 100)
lab_hr_txt = Label(clock, text = "Hour", font = ("times new roman", 20, "bold"),
               bg = "red", fg = "white")
lab_hr_txt.place(x = 120, y = 190, height = 40, width = 100)

#Minute
lab_min = Label(clock, text = "00", font = ("times new roman", 40, "bold"),
               bg = "red", fg = "white")
lab_min.place(x = 340, y = 50, height = 110, width = 100)

lab_min_txt = Label(clock, text = "Min", font = ("times new roman", 20, "bold"),
               bg = "red", fg = "white")
lab_min_txt.place(x = 340, y = 190, height = 40, width = 100)

#Second
lab_sec = Label(clock, text = "00", font = ("times new roman", 40, "bold"),
               bg = "red", fg = "white")
lab_sec.place(x = 560, y = 50, height = 110, width = 100)

lab_sec_txt = Label(clock, text = "Sec", font = ("times new roman", 20, "bold"),
               bg = "red", fg = "white")
lab_sec_txt.place(x = 560, y = 190, height = 40, width = 100)

#AM / PM
lab_am = Label(clock, text = "AM", font = ("times new roman", 40, "bold"),
               bg = "red", fg = "white")
lab_am.place(x = 780, y = 50, height = 110, width = 100)

lab_am_txt = Label(clock, text = "AM/PM", font = ("times new roman", 20, "bold"),
               bg = "red", fg = "white")
lab_am_txt.place(x = 780, y = 190, height = 40, width = 100)

# *********** Date


#Date
lab_date = Label(clock, text = "00", font = ("times new roman", 40, "bold"),
               bg = "red", fg = "white")
lab_date.place(x = 120, y = 270, height = 110, width = 100)
lab_date_txt = Label(clock, text = "Date", font = ("times new roman", 20, "bold"),
               bg = "red", fg = "white")
lab_date_txt.place(x = 120, y = 410, height = 40, width = 100)

#Month
lab_month = Label(clock, text = "00", font = ("times new roman", 40, "bold"),
               bg = "red", fg = "white")
lab_month.place(x = 340, y = 270, height = 110, width = 100)

lab_month_txt = Label(clock, text = "Month", font = ("times new roman", 20, "bold"),
               bg = "red", fg = "white")
lab_month_txt.place(x = 340, y = 410, height = 40, width = 100)

# Year
lab_year = Label(clock, text = "00", font = ("times new roman", 40, "bold"),
               bg = "red", fg = "white")
lab_year.place(x = 560, y = 270, height = 110, width = 100)

lab_year_txt = Label(clock, text = "Year", font = ("times new roman", 20, "bold"),
               bg = "red", fg = "white")
lab_year_txt.place(x = 560, y = 410, height = 40, width = 100)

# Day
lab_day = Label(clock, text = "AM", font = ("times new roman", 35, "bold"),
               bg = "red", fg = "white")
lab_day.place(x = 780, y = 270, height = 110, width = 100)

lab_day_txt = Label(clock, text = "Day", font = ("times new roman", 20, "bold"),
               bg = "red", fg = "white")
lab_day_txt.place(x = 780, y = 410, height = 40, width = 100)






date_time()
clock.mainloop()