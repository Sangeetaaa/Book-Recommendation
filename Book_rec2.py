
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
    avg_Rating = 0.0
    era = ""
    pacing =""
    language =""


    def __init__(self, Book_ID, Title, Author, Genre, SubGenre, Weights, Age_Group ,era ,pacing ,language):
        self.Book_ID = Book_ID
        self.Author = Author
        self.Title = Title
        self.Genre = Genre
        self.SubGenre = SubGenre
        self.Weights = Weights
        self.Age_Group = Age_Group
        self.era =era
        self.pacing =pacing
        self.language =language
        self.avg_Rating = 0.0


def verify_user(username, password):
    while True:
        reader = open("Users.csv")
        input_file = csv.DictReader(reader)
        for row in input_file:
            if row['UserName'] == username and row['Password'] == password:
                flag =1
                return True
        return False



def getBook_data(choice ,u_name,dict):
    while True:
        # print("Enter your name : ")
        # name = str(input())
        reader = open("Books.csv")
        input_file = csv.DictReader(reader)

        Book_data = []
        flag=0

        if choice == 1:
            # print("Enter the Author name : ")
            # author_name = str(input())
            for row in input_file:
                if row['Author'] == dict['Author_name'] and ((row['era']==dict['era']) or dict['era']=="") and ((row['Pacing']==dict['pace']) or dict['pace']=="")  and ((row['language']==dict['Language'])or dict['Language']=="") and ((row['Gender']==dict['Gender'])or dict['Gender']=="") and ((row['Age_Group']==dict['Age'])or dict['Age']==""):
                    flag = 2
                    obj = Book(row['Book_ID'], row['Title'], row['Author'], row['Genre'], row['SubGenre'],
                               row['Weights'], row['Age_Group'],row['era'],row['Pacing'],row['language'])
                    Book_data.append(obj)
            print(flag)
            if flag == 2:
                break
            else:
                print("No such author found.")
                print(dict['Author_name'])
                print(dict['era'])
                print(dict['pace'])
                print(dict['Language'])

                break


        elif choice == 2:
            # print("Enter the genre : ")
            # genre = str(input())
            for row in input_file:
                if row['Genre'] == dict['Genre'] and ((row['era'] == dict['era']) or dict['era'] == "") and (
                        (row['Pacing'] == dict['pace']) or dict['pace'] == "") and (
                        (row['language'] == dict['Language']) or dict['Language'] == "") and (
                        (row['Gender'] == dict['Gender']) or dict['Gender'] == "") and (
                        (row['Age_Group'] == dict['Age']) or dict['Age'] == ""):
                    flag = 2
                    obj = Book(row['Book_ID'], row['Title'], row['Author'], row['Genre'], row['SubGenre'],
                               row['Weights'], row['Age_Group'], row['era'], row['Pacing'], row['language'])
                    Book_data.append(obj)

            if flag == 2:
                break
            else:
                print("No book available for this genre.")
                print(dict['Genre'])
                break
        elif choice == 3:
            # print("Enter the genre  : ")
            # genre = str(input())
            # print("Enter the Author name : ")
            # author_name = str(input())
            for row in input_file:
                for row in input_file:
                    if row['Author'] == dict['Author_name'] and row['Genre'] == dict['Genre'] and ((row['era'] == dict['era']) or dict['era'] == "") and (
                            (row['Pacing'] == dict['pace']) or dict['pace'] == "") and (
                            (row['language'] == dict['Language']) or dict['Language'] == "") and (
                            (row['Gender'] == dict['Gender']) or dict['Gender'] == "") and (
                            (row['Age_Group'] == dict['Age']) or dict['Age'] == ""):
                        flag = 2
                        obj = Book(row['Book_ID'], row['Title'], row['Author'], row['Genre'], row['SubGenre'],
                                   row['Weights'], row['Age_Group'], row['era'], row['Pacing'], row['language'])
                        Book_data.append(obj)

            if flag == 2:
                break
            else:
                print("No book available for this data.")
                print(dict['Author_name'])
                break
    book_id=0
    if 'Book_name' in dict:
        reader = open("Books.csv")
        input_file = csv.DictReader(reader)
        for row in input_file:
            if row['Title']==dict['Book_name']:
                book_id=row['Book_ID']
                break
        reader1 = open("Users.csv")
        user_file = csv.DictReader(reader1)
        U_id=0
        for row in user_file:
            if row['UserName']==u_name:
                u_id=row['User_ID']
                break
        myCsvRow=str("\n")+str(u_id)+","+str(book_id)+","+str(dict['Rating'])
        reader2 = open("Rating.csv")
        Rating_file = csv.DictReader(reader2)
        with open('Rating.csv', 'a') as fd:
            fd.write(myCsvRow)
        reader2.close()
        reader1.close()
    reader.close()
    return Book_data

def getPredicted_data(Book_data):

    for i in Book_data:
        count =1
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
  @Rule(Fact(x=MATCH.y1 ,y=MATCH.mylist1 ,n=MATCH.n))
  def is_suitable(self ,y1 ,mylist1 ,n):
      if(len(y1)==0):
          print("no Book is found")
      elif(len(y1)==n):
          for row in y1:
              mylist1.append(row)
      else:
          for row in y1:
              mylist1.append(row)


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
        self.password = StringVar()
        self.lblTitle = Label(self.frame, text="Book Recommendation System", font=('Arial', 50, 'bold'),
                              bg='powder blue', fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblUserName = Label(self.LoginFrame1, text='UserName', font=('Arial', 20, 'bold'), bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblUserName.grid(row=0, column=0)
        self.txtUserName = Entry(self.LoginFrame1, font=('Arial', 20, 'bold'), textvariable=self.username)
        self.txtUserName.grid(row=0, column=1)
        self.lblPassword = Label(self.LoginFrame1, text='Password', font=('Arial', 20, 'bold'), bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.LoginFrame1, font=('Arial', 20, 'bold'), textvariable=self.password, show='*')
        self.txtPassword.grid(row=1, column=1)

        self.btnLogin = Button(self.LoginFrame2, text="Submit", width=17, font=('Arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)
        self.btnReset = Button(self.LoginFrame2, text="Reset", width=17, font=('Arial', 20, 'bold'), command=self.Rest)
        self.btnReset.grid(row=3, column=1, pady=20, padx=8)
        self.btnExit = Button(self.LoginFrame2, text="Exit", width=17, font=('Arial', 20, 'bold'), command=self.iExit)
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)

    def Login_System(self):
        u = (self.username.get())
        d = {'UserName' : u }
        p = (self.password.get())
        print(p)
        flag = verify_user(u, p)
        if flag:
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow, u,d)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid Credentials")

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
    def __init__(self, master, u,d):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.ans = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + d['UserName'] + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Preferred Age-Group',
                             font=('Arial', 20, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)
        self.d = d
        self.btnChild = Button(self.LoginFrame2, text="Child", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="child": self.Login_System(m))
        self.btnChild.grid(row=3, column=0, pady=20, padx=8)

        self.btnAdult = Button(self.LoginFrame2, text="adult", width=17, font=('Arial', 20, 'bold'), command=lambda m="adult": self.Login_System(m))
        self.btnAdult.grid(row=3, column=1, pady=20, padx=8)
        self.btnOld = Button(self.LoginFrame2, text="Old", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="Old": self.Login_System(m))
        self.btnOld.grid(row=3, column=2, pady=20, padx=8)

        self.btnSkip = Button(self.LoginFrame2, text="Skip", width=17, font=('Arial', 20, 'bold'), command=lambda m="": self.Login_System(m))
        self.btnSkip.grid(row=3, column=3, pady=20, padx=8)
        self.u=u
    def Login_System(self, age):
        print(age)
        self.d['Age'] = age
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow,self.u, self.d)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.new_window)



class Window3:
    def __init__(self, master,u, d):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.ans = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + d['UserName'] + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Your Gender',
                             font=('Arial', 20, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)

        self.d = d
        self.btnMale = Button(self.LoginFrame2, text="male", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="male": self.Login_System(m))
        self.btnMale.grid(row=3, column=0, pady=20, padx=8)

        self.btnFemale = Button(self.LoginFrame2, text="female", width=17, font=('Arial', 20, 'bold'), command=lambda m="female": self.Login_System(m))
        self.btnFemale.grid(row=3, column=1, pady=20, padx=8)
        self.btnNo = Button(self.LoginFrame2, text="Prefer Not to Say", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="others": self.Login_System(m))
        self.btnNo.grid(row=3, column=2, pady=20, padx=8)

        self.btnSkip = Button(self.LoginFrame2, text="Skip", width=17, font=('Arial', 20, 'bold'), command=lambda m="": self.Login_System(m))
        self.btnSkip.grid(row=3, column=3, pady=20, padx=8)
        self.u=u
    def Login_System(self, gender):
        print(gender)
        self.d['Gender'] = gender
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow, self.u,self.d)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.new_window)


class Window4:
    def __init__(self, master,u, d):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.ans = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + d['UserName'] + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Language You Prefer',
                             font=('Arial', 20, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)

        self.d = d


        self.btnHindi= Button(self.LoginFrame2, text="Hindi", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="hindi": self.Login_System(m))
        self.btnHindi.grid(row=3, column=0, pady=20, padx=8)

        self.btnEnglish = Button(self.LoginFrame2, text="english", width=17, font=('Arial', 20, 'bold'), command=lambda m="english": self.Login_System(m))
        self.btnEnglish.grid(row=3, column=1, pady=20, padx=8)

        self.btnSkip = Button(self.LoginFrame2, text="Skip", width=17, font=('Arial', 20, 'bold'), command=lambda m="": self.Login_System(m))
        self.btnSkip.grid(row=3, column=3, pady=20, padx=8)
        self.u=u

    def Login_System(self, language):
        self.d['Language']=language
        self.newWindow = Toplevel(self.master)
        self.app = Window5(self.newWindow,self.u, self.d)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.new_window)



class Window5:
    def __init__(self, master,u, d):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.ans = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " +d['UserName'] + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Era you prefer',
                             font=('Arial', 20, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)

        self.d = d
        self.u=u

        self.btnAncient= Button(self.LoginFrame2, text="ancient", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="ancient": self.Login_System(m))
        self.btnAncient.grid(row=3, column=0, pady=20, padx=8)
        self.btnMedieval = Button(self.LoginFrame2, text="Medieval", width=17, font=('Arial', 20, 'bold'), command=lambda m="medieval": self.Login_System(m))
        self.btnMedieval.grid(row=3, column=1, pady=20, padx=8)
        self.btnModern = Button(self.LoginFrame2, text="Modern", width=17, font=('Arial', 20, 'bold'), command=lambda m="modern": self.Login_System(m))
        self.btnModern.grid(row=3, column=2, pady=20, padx=8)
        self.btnSkip = Button(self.LoginFrame2, text="Skip", width=17, font=('Arial', 20, 'bold'), command=lambda m="": self.Login_System(m))
        self.btnSkip.grid(row=3, column=3, pady=20, padx=8)

    def Login_System(self, era):
        print(era)
        self.d['era']=era
        self.newWindow = Toplevel(self.master)
        self.app = Window6(self.newWindow,self.u, self.d)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window5(self.new_window)

class Window6:
    def __init__(self, master,u, d):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.ans = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + d['UserName'] + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Pace of books preferred',
                             font=('Arial', 20, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)

        self.d = d
        self.u=u

        self.btnSlow= Button(self.LoginFrame2, text="Slow", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="slow": self.Login_System(m))
        self.btnSlow.grid(row=3, column=0, pady=20, padx=8)
        self.btnMedium = Button(self.LoginFrame2, text="Medium", width=17, font=('Arial', 20, 'bold'), command=lambda m="Medium": self.Login_System(m))
        self.btnMedium.grid(row=3, column=1, pady=20, padx=8)
        self.btnFast = Button(self.LoginFrame2, text="fast", width=17, font=('Arial', 20, 'bold'), command=lambda m="fast": self.Login_System(m))
        self.btnFast.grid(row=3, column=2, pady=20, padx=8)
        self.btnSkip = Button(self.LoginFrame2, text="Skip", width=17, font=('Arial', 20, 'bold'), command=lambda m="": self.Login_System(m))
        self.btnSkip.grid(row=3, column=3, pady=20, padx=8)

    def Login_System(self, pace):
        print(pace)
        self.d['pace']=pace
        self.newWindow = Toplevel(self.master)
        self.app = Window7(self.newWindow,self.u, self.d)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window6(self.new_window)

class Window7:
    def __init__(self, master,u, d):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.ans = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + d['UserName'] + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Do you Prefer Fiction or Non-Fiction ?',
                             font=('Arial', 20, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)

        self.d=d

        self.btnFicition= Button(self.LoginFrame2, text="fiction", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="fiction": self.Login_System(m))
        self.btnFicition.grid(row=3, column=0, pady=20, padx=8)

        self.btnNon = Button(self.LoginFrame2, text="nonfiction", width=17, font=('Arial', 20, 'bold'), command=lambda m="nonfiction": self.Login_System(m))
        self.btnNon.grid(row=3, column=1, pady=20, padx=8)

        self.btnSkip = Button(self.LoginFrame2, text="Skip", width=17, font=('Arial', 20, 'bold'), command=lambda m="": self.Login_System(m))
        self.btnSkip.grid(row=3, column=3, pady=20, padx=8)
        self.u=u
    def Login_System(self, booktype):
        print(booktype)
        self.d['Book_type']=booktype
        self.newWindow = Toplevel(self.master)
        self.app = Window8(self.newWindow, self.u,self.d)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window7(self.new_window)




class Window8:
    def __init__(self, master, u,d):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.ans = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + d['UserName'] + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Do you Prefer any book?',
                             font=('Arial', 20, 'bold'), bd=22, bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)
        self.d=d
        self.btnLogin = Button(self.LoginFrame2, text="Yes", width=17, font=('Arial', 20, 'bold'),
                               command=lambda m="Yes": self.Login_System(m))
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text="No", width=17, font=('Arial', 20, 'bold'), command=lambda m="No": self.Login_System(m))
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)
        self.u=u
    def Login_System(self,str1):


        if str1 == 'Yes' or str1 == 'yes':
            self.newWindow = Toplevel(self.master)
            self.app = Window9(self.newWindow, self.u,self.d)
        else:
            self.newWindow = Toplevel(self.master)
            self.app = Window10(self.newWindow,self.u, self.d)

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window8(self.new_window)

class Window9:
    def __init__(self, master,u, d):
        self.master = master
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.bookname = StringVar()
        self.rating = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + d['UserName'] + " !!", font=('Arial', 50, 'bold'), bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)
        self.d=d
        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblBookName = Label(self.LoginFrame1, text='Book Name', font=('Arial', 20, 'bold'), bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblBookName.grid(row=0, column=0)
        self.txtBookName = Entry(self.LoginFrame1, font=('Arial', 20, 'bold'), textvariable=self.bookname)
        self.txtBookName.grid(row=0, column=1)
        self.lblRating= Label(self.LoginFrame1, text='Rate it', font=('Arial', 20, 'bold'), bd=22,
                                 bg='cadet blue', fg='Cornsilk')
        self.lblRating.grid(row=1, column=0)
        self.txtRating = Entry(self.LoginFrame1, font=('Arial', 20, 'bold'), textvariable=self.rating)
        self.txtRating.grid(row=1, column=1)

        self.btnLogin = Button(self.LoginFrame2, text="Submit", width=17, font=('Arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=3, column=0, pady=20, padx=8)
        self.btnSkip = Button(self.LoginFrame2, text="Reset", width=17, font=('Arial', 20, 'bold'), command=self.Skip)
        self.btnSkip.grid(row=3, column=1, pady=20, padx=8)
        self.u=u
    def Login_System(self):
        book = (self.bookname.get())
        rating = (self.rating.get())
        self.d['Book_name']=book
        self.d['Rating'] = rating
        self.newWindow = Toplevel(self.master)
        self.app = Window10(self.newWindow, self.u,self.d)
        # u = (self.username.get())
        # p = (self.password.get())
        # print(p)
        # flag = verify_user(u, p)
        # if flag:
        #     self.newWindow = Toplevel(self.master)
        #     self.app = Window2(self.newWindow, u)
        # else:
        #     tkinter.messagebox.showwarning("Login System", "Invalid Credentials")

    def Skip(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window10(self.newWindow, self.u,self.d )

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window9(self.new_window)


class Window10:
    def __init__(self, master,u, dict):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.username = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + dict['UserName'] + " !!", font=('Arial', 50, 'bold'),
                              bg='powder blue',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=1, pady=40)

        self.LoginFrame1 = Frame(self.frame, width=1350, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=600, relief='ridge', bg='cadet blue', bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblPref = Label(self.LoginFrame1, text='Select your way of preferneces', font=('Arial', 20, 'bold'), bd=22,
                             bg='cadet blue', fg='Cornsilk')
        self.lblPref.grid(row=0, column=0)
        self.dict = dict

        self.btnAuthor = Button(self.LoginFrame2, text="Author", width=17, font=('Arial', 20, 'bold'),
                                command=self.Author_System)
        self.btnAuthor.grid(row=3, column=0, pady=20, padx=8)

        self.btnGenre = Button(self.LoginFrame2, text="Genre", width=17, font=('Arial', 20, 'bold'),
                               command=self.Genre_System)
        self.btnGenre.grid(row=3, column=1, pady=20, padx=8)

        self.btnBoth = Button(self.LoginFrame2, text="Both", width=17, font=('Arial', 20, 'bold'), command=self.Both)
        self.btnBoth.grid(row=3, column=2, pady=20, padx=8)
        self.u=u
    def Author_System(self):
        print()
        author_name = str(simpledialog.askstring("Author name", "Enter Author name", parent=self.master))
        genre = ""
        if author_name:
            choice = 1
            self.dict['Author_name'] = author_name
            self.newWindow = Toplevel(self.master)
            self.app = Window11(self.newWindow,choice,self.u, self.dict)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid data")

    def Genre_System(self):
        genre = str(simpledialog.askstring("Genre name", "Enter Genre name", parent=self.master))
        author_name = ""
        if genre:
            choice = 2
            self.dict['Genre'] = genre
            self.newWindow = Toplevel(self.master)
            self.app = Window11(self.newWindow,choice,self.u, self.dict)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid data")

    def Both(self):
        choice = 3
        author_name = str(simpledialog.askstring("Author name", "Enter Author name", parent=self.master))
        if author_name:
            genre = str(simpledialog.askstring("Genre name", "Enter Genre name", parent=self.master))
            if not genre:
                tkinter.messagebox.showwarning("Login System", "Invalid data")
            else:
                self.dict['Genre'] = genre
                self.dict['Author_name'] = author_name
                self.newWindow = Toplevel(self.master)
                self.app = Window11(self.newWindow, choice,self.u, self.dict)
        else:
            tkinter.messagebox.showwarning("Login System", "Invalid data")

    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window10(self.new_window)


class Window11:
    def __init__(self, master, choice,u, dict):
        self.master = master
        self.master.title("Book Recommendation System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg='powder blue')
        self.frame = Frame(self.master, bg='powder blue')
        self.frame.pack()
        self.username = StringVar()
        self.lblTitle = Label(self.frame, text="Welcome  " + dict['UserName'] + " !!", font=('Arial', 50, 'bold'),
                              bg='powder blue',
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
        self.lbl1 = Label(self.LoginFrame2, text="Book Title", font=('Arial', 20, 'bold'),
                          bd=22, bg='cadet blue', fg='Cornsilk')
        self.lbl1.grid(row=1, column=0)
        self.lbl2 = Label(self.LoginFrame2, text="                     ", font=('Arial', 20, 'bold'),
                          bd=22, bg='cadet blue', fg='Cornsilk')
        self.lbl2.grid(row=1, column=1)
        self.lbl3 = Label(self.LoginFrame2, text="Book Author", font=('Arial', 20, 'bold'),
                          bd=22, bg='cadet blue', fg='Cornsilk')
        self.lbl3.grid(row=1, column=4)
        # scrollbar = Scrollbar(self.master)
        # scrollbar.pack(side=RIGHT, fill=Y)
        book_data = getBook_data(choice,u,dict)
        book_data = getPredicted_data(book_data)
        i = 0
        for row in book_data:
            if i==4:
                break
            self.lbl = Label(self.LoginFrame3, text=row.Title + "     " + row.Author, font=('Arial', 20, 'bold'), bd=22,
                             bg='cadet blue', fg='Cornsilk')
            self.lbl.grid(row=i, column=0)
            i = i + 1



if __name__ == '__main__':
    root = Tk()
    application = Window1(root)
    root.mainloop()
