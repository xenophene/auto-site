#!/usr/bin/python
from Tkinter import *
from website import Website
import tkFont

class App:
  def __init__(self):
    self.w = Website()
    self.root = Tk()
    self.root.title("Auto site - Enter the fields")
    self.my_font = tkFont.Font(family="Helvetica", size=11)

    self.frame = Frame(self.root, height=800, width=800, \
                       padx=50, pady=10)
    self.frame.pack()

    self.fields()
    self.buttons()

    self.root.mainloop()

  def addLabel(self, text, row=None, column=None):
    l = Label(self.frame, text=text, font=self.my_font)
    if (row is not None and column is not None):
      l.grid(row=row, column=column, sticky=E)
    else:
      l.grid(sticky=N+E)

  def addEntry(self, value, row, column):
    e = Entry(self.frame, font=self.my_font, width=40)
    e.insert(0, value)
    e.grid(row=row, column=column, columnspan=2, sticky=W)
    return e

  def fields(self):
    self.addLabel("Your name:")
    self.addLabel("Your college:")
    self.addLabel("Your degree:")
    self.addLabel("Brief description:")
    self.addLabel("Profile pic location:")
    self.addLabel("About Me:")
    self.addLabel("Academic Interests:")

    self.name = self.addEntry(self.w.getName(), 0, 1)
    self.college = self.addEntry(self.w.getCollege(), 1, 1)
    self.degree =  self.addEntry(self.w.getDegree(), 2, 1)
    self.description = Text(self.frame, font=self.my_font, height=3, \
                            wrap=WORD, width=40)
    self.description.insert(0.0, self.w.getDescription())
    self.description.grid(row=3, column=1, columnspan=2, sticky=W)

    self.img =  self.addEntry(self.w.getImg(), 4, 1)

    self.about_me = Text(self.frame, font=self.my_font, height=3, \
                         wrap=WORD, width=40)
    self.about_me.insert(0.0, self.w.getAboutMe())
    self.about_me.grid(row=5, column=1, columnspan=2, sticky=W)

    self.academic_interests = Text(self.frame, font=self.my_font, height=3, \
                                   wrap=WORD, width=40)
    self.academic_interests.insert(0.0, self.w.getAcademicInterests())
    self.academic_interests.grid(row=6, column=1, columnspan=2, sticky=W)


  def submit(self):
    self.w.setName(self.name.get())
    self.w.setCollege(self.college.get())
    self.w.setDegree(self.degree.get())
    self.w.setDescription(self.description.get(0.0, END))
    self.w.setAboutMe(self.about_me.get(0.0, END))
    self.w.setAcademicInterests(self.academic_interests.get(0.0, END))
    self.w.setImg(self.img.get())
    self.w.createWebsite()
    self.frame.quit()

  def buttons(self):
    col = 0
    row = 8
    self.quit = Button(self.frame, text="Quit", command=self.frame.quit)
    self.quit.grid(row=row, column=col, sticky=E)
    self.submit = Button(self.frame, text="Submit", command=self.submit)
    self.submit.grid(row=row, column=1, sticky=W)


if __name__ == '__main__':
  app = App()
