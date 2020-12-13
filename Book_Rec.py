from collections import defaultdict

from experta import *
import csv
from tkinter import *
import tkinter.messagebox
from tkinter import simpledialog
from tkinter import ttk
import random
import time
import datetime

class Book:
    Book_ID = ""
    Title = ""
    Author = ""
    Genre = ""
    SubGenre = ""
    Weights = 0
    Age_Group = 0
    avg_Rating=0.0
    era=""

    def __init__(self, Book_ID, Title, Author, Genre, SubGenre, Weights, Age_Group):
        self.Book_ID = Book_ID
        self.Author = Author
        self.Title = Title
        self.Genre = Genre
        self.SubGenre = SubGenre
        self.Weights = Weights
        self.Age_Group = Age_Group
        self.avg_Rating=0.0



def getBook_data(choice,author_name,genre):
    while True:
        # print("Enter your name : ")
        # name = str(input())
        reader = open("Books.csv")
        input_file = csv.DictReader(reader)
        Book_data = []
        # choice = int(input())
        if choice == 1:
            # print("Enter the Author name : ")
            # author_name = str(input())
            for row in input_file:
                if row['Author'] == author_name:
                    flag = 1
                    obj = Book(row['Book_ID'], row['Title'], row['Author'], row['Genre'], row['SubGenre'],
                               row['Weights'], row['Publisher'])
                    Book_data.append(obj)

            if flag == 1:
                break
            else:
                print("No such author found.")
                continue


        elif choice == 2:
            # print("Enter the genre : ")
            # genre = str(input())
            for row in input_file:
                if row['Genre'] == genre:
                    flag = 1
                    obj = Book(row['Book_ID'], row['Title'], row['Author'], row['Genre'], row['SubGenre'],
                               row['Weights'], row['Publisher'])
                    Book_data.append(obj)

            if flag == 1:
                break
            else:
                print("No book available for this genre.")
                continue
        elif choice == 3:
            # print("Enter the genre  : ")
            # genre = str(input())
            # print("Enter the Author name : ")
            # author_name = str(input())
            for row in input_file:
                if row['Author'] == author_name and row['Genre'] == genre:
                    flag = 1
                    obj = Book(row['Book_ID'], row['Title'], row['Author'], row['Genre'], row['SubGenre'],
                               row['Weights'], row['Publisher'])
                    Book_data.append(obj)

            if flag == 1:
                break
            else:
                print("No book available for this data.")
                continue
    reader.close()
    return Book_data

def getPredicted_data(Book_data):

    for i in Book_data:
        count=1
        reader = open("Rating.csv")
        user_file = csv.DictReader(reader)
        for row in user_file:
            if i.Book_ID == row['Book_ID'] :
                count = count + 1
                i.avg_Rating = i.avg_Rating + float(row['Rating'])

        i.avg_Rating = float(i.avg_Rating) / count
        reader.close()

    Book_data.sort(key=lambda x: x.avg_Rating, reverse=True)
    return Book_data


class expert_system(KnowledgeEngine):
  @Rule(Fact(x=MATCH.y1,y=MATCH.mylist1,n=MATCH.n))
  def is_suitable(self,y1,mylist1,n):
      mylist1=[]
      if(len(y1)==0):
          print("no Book is found")
      elif(len(y1)==n):
          for row in y1:
              mylist1.append(Book(row.Book_ID,row.Title,row.Author,row.Genre,row.SubGenre,row.Weights,row.Publisher))
      else:
          for row in y1:
              mylist1.append(Book(row.Book_ID,row.Title,row.Author,row.Genre,row.SubGenre,row.Weights,row.Publisher))



    # return mylist


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.username = StringVar()
        self.lblTitle = Label(self.frame, text="Book Recommendation System", font=('Arial', 50, 'bold'),
                              bg='powder blue', fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblUserName = Label(self.LoginFrame1, text='Enter your name', font=('Arial', 20, 'bold'), bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblUserName.grid(row=0, column=0)
        self.txtUserName = Entry(self.LoginFrame1, font=('Arial', 20, 'bold'), textvariable=self.username)
        self.txtUserName.grid(row=1, column=0)

        self.btnLogin = Button(self.LoginFrame2, text="Submit", width=17, font=('Arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)
        self.btnReset = Button(self.LoginFrame2, text="Reset", width=17, font=('Arial', 20, 'bold'), command=self.Rest)
        self.btnReset.grid(row=3, column=1, pady=20, padx=8)
        self.btnExit = Button(self.LoginFrame2, text="Exit", width=17, font=('Arial', 20, 'bold'), command=self.iExit)
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)

    def Login_System(self):
        u = (self.username.get())
        print(u)
        name=u
        if u:
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow, u)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid Name")

    def Rest(self):
        self.username.set("")
        self.txtUserName.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.new_window)


class Window2:
    def __init__(self, master, str):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.ans = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + str + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Do you have any preference of Books? (Y/N)',
                             font=('Arial', 20, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)
        self.txtPref = Entry(self.LoginFrame1, font=('Arial', 20, 'bold'), width=6, textvariable=self.ans)
        self.txtPref.grid(row=0, column=1)
        self.name = str
        self.btnLogin = Button(self.LoginFrame2, text="Submit", width=17, font=('Arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text="Exit", width=17, font=('Arial', 20, 'bold'), command=self.iExit)
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)

    def Login_System(self):
        u = (self.ans.get())

        if u == 'Y' or u == 'y':
            self.newWindow = Toplevel(self.master)
            self.app = Window3(self.newWindow, self.name)
        elif u == 'N' or u == 'n':
            self.newWindow = Toplevel(self.master)
            self.app = Window4(self.newWindow, self.name)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid Response", parent=self.master)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login System", "Confirm if you want to Exit?", parent=self.master)
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.new_window)


class Window3:
    def __init__(self, master, str):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.username = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + str + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Select your way of preferneces', font=('Arial', 20, 'bold'), bd=22,
                             bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)
        self.name = str

        self.btnAuthor = Button(self.LoginFrame2, text="Author", width=17, font=('Arial', 20, 'bold'),
                                command=self.Author_System)
        self.btnAuthor.grid(row=3, column=0, pady=20, padx=8)

        self.btnGenre = Button(self.LoginFrame2, text="Genre", width=17, font=('Arial', 20, 'bold'),
                               command=self.Genre_System)
        self.btnGenre.grid(row=3, column=1, pady=20, padx=8)

        self.btnBoth = Button(self.LoginFrame2, text="Both", width=17, font=('Arial', 20, 'bold'), command=self.Both)
        self.btnBoth.grid(row=3, column=2, pady=20, padx=8)

    def Author_System(self):
        print()
        author_name = str(simpledialog.askstring("Author name", "Enter Author name", parent=self.master))
        genre=""
        if author_name:
            choice=1
            self.newWindow = Toplevel(self.master)
            self.app = Window4(self.newWindow, self.name,choice,author_name,genre)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid data")

    def Genre_System(self):
        genre = str(simpledialog.askstring("Genre name", "Enter Genre name", parent=self.master))
        author_name=""
        if genre:
            choice=2
            self.newWindow = Toplevel(self.master)
            self.app = Window4(self.newWindow, self.name,choice,author_name,genre)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid data")

    def Both(self):
        choice=3
        author_name = str(simpledialog.askstring("Author name", "Enter Author name", parent=self.master))
        if author_name:
            genre = str(simpledialog.askstring("Genre name", "Enter Genre name", parent=self.master))
            if not genre:
                tkinter.messagebox.showwarning("Login System", "Invalid data")
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Window4(self.newWindow, self.name,choice,author_name,genre)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid data")

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.new_window)


class Window4:
    def __init__(self, master, str,choice,author,genre):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.username = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + str + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        self.LoginFrame3 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame3.grid(row=3, column=0)

        self.lblRec = Label(self.LoginFrame1, text='Your Recommended List of Books:', font=('Arial', 20, 'bold'), bd=22,
                            bg='cadet blue', fg='Cornsilk')
        self.lblRec.grid(row=0, column=0)
        # scrollbar = Scrollbar(self.master)
        # scrollbar.pack(side=RIGHT, fill=Y)
        book_data = getBook_data(choice,author,genre)
        book_data = getPredicted_data(book_data)

        mylist = []
        engine = expert_system()
        engine.reset()
        engine.declare(Fact(x=book_data,y=mylist,n=4))
        engine.run()
        # self.lbl1 = Label(self.LoginFrame2, text="Book Title" + "     " + "Book Author", font=('Arial', 20, 'bold'), bd=22,
        #                  bg='cadet blue', fg='Cornsilk')
        # self.lbl1.grid(row=0, column=0)
        self.lbl1 = Label(self.LoginFrame2, text="Book Title", font=('Arial', 20, 'bold'),
                          bd=22, bg='cadet blue', fg='Cornsilk')
        self.lbl1.grid(row=1, column=0)
        self.lbl2 = Label(self.LoginFrame2, text="                     ", font=('Arial', 20, 'bold'),
                         bd=22, bg='cadet blue', fg='Cornsilk')
        self.lbl2.grid(row=1, column=1)
        self.lbl3 = Label(self.LoginFrame2, text="Book Author", font=('Arial', 20, 'bold'),
                          bd=22, bg='cadet blue', fg='Cornsilk')
        self.lbl3.grid(row=1, column=4)
        i=0
        for row in book_data:
            if i==4:
                break
            self.lbl = Label(self.LoginFrame3, text=row.Title+"     "+row.Author, font=('Arial', 20, 'bold'), bd=22,
                             bg='cadet blue', fg='Cornsilk')
            self.lbl.grid(row=i, column=0)
            i=i+1
        # i=0
        # for row in mylist:
        #     print(row.Title)
        #     self.lbl = Label(self.LoginFrame2, text=row.Title+"     "+row.Author, font=('Arial', 20, 'bold'), bd=22,
        #                      bg='cadet blue', fg='Cornsilk')
        #     self.lbl.grid(row=i, column=0)
        #     i = i + 1

        # for row in book_data:
        #     mylist.insert(END, row.Title)
        # mylist.pack(side=LEFT, fill=BOTH)
        # scrollbar.config(command=mylist.yview)
        # self.master.mainloop()


if __name__ == '__main__':
    root = Tk()
    application = Window1(root)
    root.mainloop()
# def main():
    # Book_data = getBook_data()
    # Book_data = getPredicted_data(Book_data)
    # root = Tk()
    # app = Window1(root)
    # root.mainloop()
    # for row in Book_data:
    #     print(row.Book_ID+"          "+row.Title + "        "+str(row.avg_Rating))

    # engine = expert_system()
#     # engine.reset()
#     # engine.declare(Fact(x=Book_data, n=4))
#     # engine.run()
# main()


