from tkinter import *
import calendar, datetime

# ── Colors ──────────────────────────────────────────────
BG     = "#560a50"   # dark blue background
CARD   = "#480647"   # slightly lighter blue for month boxes
ACCENT = "#e945de"   # red for today and weekends
BLUE   = "#600f48"   # blue for month title bar
TEXT   = "#eaeaea"   # white-ish text
GRAY   = "#8892a4"   # gray for day headers

MONTHS = ["January","February","March","April","May","June", "July","August","September","October","November","December"]


today = datetime.date.today()
screen = Tk()
screen.title("Calendar App")
screen.geometry("450x300")
screen.config(background="ivory2")
def Show_Calendar():
    year = int(yearen.get())
    screen2 = Tk()
    screen2.title(f"Calendar Year: {year}")
    screen2.config(background=BG)
    #screen2.resizable(False, False)
    yearer2 = Label(screen2, text=f"{year}", bg=BG, fg= TEXT, font=("times", 34, "bold"))
    yearer2.pack()
    framex = Frame(screen2, bg=ACCENT, height= 2)
    framex.pack(fill = "x")
    framey = Frame(screen2, bg=BG,)
    framey.pack()
    for m in range(12):
        row = m // 3
        col = m%3
        card = Frame(framey, bg= CARD, highlightthickness= 1, highlightbackground = BLUE)
        card.grid(row= row, column= col)
        monthLabel = Label(framey, text = MONTHS[m], bg= BLUE, fg=TEXT, font=("times", 16, "bold"), width = 21)
        monthLabel.grid(row = 0, columnspan= 7)
    screen2.mainloop()

title = Label(screen, text="Calendar App", bg="ivory3", fg="black", font=("times", 32, "bold"))
enter_your_year = Label(screen, text="Enter Your year", bg="ivory3", fg="black", font=("times", 16, "bold"))
title.place(x= 90, y=0)
yearen = Entry(screen, font=("times", 16, "bold"))
submit = Button(screen, text="submit", font=("times", 16, "bold"), command=Show_Calendar)
enter_your_year.place(x= 50, y=100)
yearen.place(x= 210, y= 100)
submit.place(x= 200, y= 250)
screen.mainloop()