from tkinter import *
from tkinter import scrolledtext, messagebox
import datetime

class Day:
    def __init__(self, main):
        self.today_lbl = Label(main,  font="Arial 18")
        self.today_lbl.grid(column=0, row=0)

        self.entry_text = Entry(font="Arial 12")
        self.entry_text.grid(column=0, row=1)

        self.button_add = Button(main, text="Добавить")
        self.button_add.grid(column=1, row=1)
        self.button_add.bind("<Button-1>", self.saveTask)

        self.txt = Listbox(main, width=40,height=20, font="Arial 12")
        self.txt.grid(column=0, row=2)

        self.today()

    def today(self):
        self.today_date = datetime.datetime.today().date()

        list_month = ["Января", "Февраля", "Марта", "Апреля",
         "Мая", "Июня", "Июля", "Августа", "Сентября",
        "Октября", "Ноября", "Декабря"]

        current_month = list_month[self.today_date.month - 1]

        self.today_date_str = str(self.today_date.day) + " " + current_month + " " + str(self.today_date.year)
        self.today_lbl.configure(text="Сегодня " + self.today_date_str + " и я:")

    def saveTask(self, event):
        if self.entry_text.get() != "":
            self.txt.insert(END, self.entry_text.get() + "\n")
            self.entry_text.delete(0, END)
        else:
            messagebox.showinfo("Ошибка", "Нельзя ввести пустое поле!")

def main():
    root = Tk()
    root.title("Дневник дел")
    root.geometry("450x500")
    start = Day(root)

    root.mainloop()

if __name__ == "__main__":
    main()
