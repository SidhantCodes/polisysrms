from tkinter import *
from tkinter import ttk, messagebox
import pyttsx3
import mysql.connector
from PIL import Image, ImageTk


def main():
    win = Tk()
    app = Loginwin(win)
    win.mainloop()


class Loginwin:
    def __init__(self, root):

        self.newindow = None
        self.newwindow = None
        self.app = None
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # txttspeech
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\sidha\CS_Project\wal1.jpg")
        lbl = Label(self.root, image=self.bg)
        lbl.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="#ff995c", relief=SUNKEN)
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\sidha\CS_Project\ur.png")
        img1 = img1.resize((90, 90), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="#ff995c", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        log = Label(frame, text="Login to your account", font=("e Enougha", 17), fg="white", bg="#ff995c")
        log.place(x=60, y=110)

        # label
        usernamelbl = Label(frame, text="Username", font=("e Enougha", 14), fg="white", bg="#ff995c")
        usernamelbl.place(x=60, y=155)

        self.txtuser = ttk.Entry(frame, font=("Times new roman", 15))
        self.txtuser.place(x=35, y=186, width=270)

        passwdlbl = Label(frame, text="Password", font=("e Enougha", 14), fg="white", bg="#ff995c")
        passwdlbl.place(x=60, y=225)

        self.txtpasswd = ttk.Entry(frame, show="*", font=("Times new roman", 15))
        self.txtpasswd.place(x=35, y=256, width=270)

        # iconimgs
        img2 = Image.open(r"C:\Users\sidha\CS_Project\ur.png")
        img2 = img2.resize((20, 20), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="#ff995c", borderwidth=0)
        lblimg2.place(x=638, y=325, width=25, height=25)

        img3 = Image.open(r"C:\Users\sidha\CS_Project\lock.png")
        img3 = img3.resize((20, 20), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="#ff995c", borderwidth=0)
        lblimg3.place(x=644, y=394, width=25, height=25)

        # loginbutton
        loginbttn = Button(frame, command=self.login, text="Login", font=("e Enougha", 15, "bold"), bd=3,
                        relief=GROOVE, cursor="hand2",
                        fg="#147145", bg="#e9efed", activeforeground="#147145", activebackground="#e9efed")
        loginbttn.place(x=110, y=300, width=110, height=40)

        # registernwebtn
        registerbtn = Button(frame, command=self.regwin, text="Register New User", font=("e Enougha", 10),
                             borderwidth=0,
                             fg="white", bg="#ff995c", activeforeground="white", activebackground="#ff995c",
                             cursor="hand2")
        registerbtn.place(x=37, y=380, width=100, height=25)

        # forgotpassbtn
        forgotpassbtn = Button(frame, command=self.forgpasswd, text="Forgot Passcode?",
                               font=("e Enougha", 10), borderwidth=0,
                               fg="white", bg="#ff995c", activeforeground="white", activebackground="#ff995c",
                               cursor="hand2")
        forgotpassbtn.place(x=35, y=360, width=100, height=25)

        # About Us
        aboutusbtn = Button(frame, command=self.abtus, text="About Us", font=("e Enougha", 11), borderwidth=0,
                            fg="white", bg="#ff995c", activeforeground="white", activebackground="#ff995c",
                            cursor="hand2")
        aboutusbtn.place(x=115, y=420, width=100, height=25)

    def abtus(self):

        if self.txtuser.get() == "" or self.txtpasswd.get() == "":
            self.engine.say("Please fill in your credentials first")
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please fill in your credentials first!")

        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Gmailsid2211",
                                           database="PoliSysRMS", charset="utf8")
            c = conn.cursor()
            c.execute("select * from registeruser where email=%s and password=%s",
                      (self.txtuser.get(), self.txtpasswd.get()))
            row = c.fetchone()
            if row is None:
                self.engine.say("Invalid Credentials")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Invalid Credentials")
            else:
                self.root3 = Toplevel()
                self.root3.title("About Us")
                self.root3.geometry("340x450+610+170")
                self.root3.resizable(False,False)

                self.bg3 = ImageTk.PhotoImage(file=r"C:\Users\sidha\CS_Project\abt.jpg")
                lb = Label(self.root3, image=self.bg3)
                lb.place(x=0, y=0, relwidth=1, relheight=1)

                c.execute("select fname from registeruser where email=%s", (self.txtuser.get(),))
                nm = c.fetchone()[0]

                l = Label(self.root3, text="Welcome " + str(nm), font=("e Enougha", 20), fg="white", bg="#056540")
                l.place(x=0, y=12, relwidth=1)

                t0 = Label(self.root3, text="We are", font=("e Enougha", 15), fg="white",
                           bg="#056540")
                t0.place(x=140, y=70)

                t1 = Label(self.root3, text="Fast.", font=("e Enougha", 15), fg="white",
                           bg="#056540")
                t1.place(x=148, y=100)

                t2 = Label(self.root3, text="Efficient.", font=("e Enougha", 15), fg="white",
                           bg="#056540")
                t2.place(x=135, y=150)

                t3 = Label(self.root3, text="Time Saving.", font=("e Enougha", 15), fg="white",
                           bg="#056540")
                t3.place(x=125, y=200)

                t4 = Label(self.root3, text="Highly Automated.", font=("e Enougha", 15), fg="white",
                           bg="#056540")
                t4.place(x=100, y=250)

                t5 = Label(self.root3, text="User Friendly UI.", font=("e Enougha", 15), fg="white",
                           bg="#056540")
                t5.place(x=105, y=300)

    def regwin(self):
        self.newindow = Toplevel(self.root)
        self.app = register(self.newindow)

    def login(self):
        if self.txtuser.get() == "" or self.txtpasswd.get() == "":
            self.engine.say("All fields are required")
            self.engine.runAndWait()
            messagebox.showerror("Error", "All fields are required to be filled!")

        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Gmailsid2211",
                                           database="PoliSysRMS", charset="utf8")
            cobj = conn.cursor()
            cobj.execute("select * from registeruser where email=%s and password=%s",
                         (self.txtuser.get(), self.txtpasswd.get()))
            row = cobj.fetchone()
            if row is None:
                self.engine.say("Invalid Username and Password")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Invalid Username and Password!")
            else:
                self.engine.say("Admin access only")
                self.engine.runAndWait()
                open_main = messagebox.askyesno("Permission", "Admin access only")
                if open_main > 0:

                    self.newwindow = Toplevel(self.newwindow)
                    self.app = Criminal(self.newwindow)

                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def resetpass(self):
        if self.ssqkey.get() == "Select":
            self.engine.say("Select the security question")
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please select the security question")
        elif self.saname_entry == "":
            self.engine.say("Invalid security answer")
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter valid security answer")
        elif self.newpassentry.get() == "":
            self.engine.say("Please enter the password")
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Gmailsid2211",
                                           database="PoliSysRMS", charset="utf8")
            cobj = conn.cursor()
            cobj.execute("select * from registeruser where email=%s and ssq=%s and ssa=%s",
                         (self.txtuser.get(), self.ssqkey.get(), self.saname_entry.get()))
            row = cobj.fetchone()
            if row is None:
                self.engine.say("Invalid credentials")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Invalid Credentials. Please enter correct answer.")
            else:
                cobj.execute("update registeruser set password=%s where email=%s",
                             (self.newpassentry.get(), self.txtuser.get()))
                conn.commit()
                conn.close()
                self.engine.say("Password has been successfully updated")
                self.engine.runAndWait()
                messagebox.showinfo("Success", "Your password has been successfully updated.")
                self.root2.destroy()

    def forgpasswd(self):
        if self.txtuser.get() == "":
            self.engine.say("Please enter the username")
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the username")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Gmailsid2211",
                                           database="PoliSysRMS", charset="utf8")
            cobj = conn.cursor()
            que = "select * from registeruser where email=%s"
            value = (self.txtuser.get(),)
            cobj.execute(que, value)
            row = cobj.fetchone()

            if row is None:
                self.engine.say("Invalid username")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Invalid Username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Reset Password")
                self.root2.geometry("340x450+610+170")
                self.root2.resizable(False, False)

                self.bg2 = ImageTk.PhotoImage(file=r"C:\Users\sidha\CS_Project\fgpass.jpg")
                lbl = Label(self.root2, image=self.bg2)
                lbl.place(x=0, y=0, relwidth=1, relheight=1)

                l = Label(self.root2, text="Forgot Password", font=("e Enougha", 20), fg="white", bg="#e67257")
                l.place(x=0, y=12, relwidth=1)

                # security question
                ssqname = Label(self.root2, text="Select Security Question", font=("e Enougha", 15), fg="white",
                                bg="#e67257")
                ssqname.place(x=50, y=80)

                self.ssqkey = ttk.Combobox(self.root2, font=("Times new roman", 12),
                                           state="readonly")
                self.ssqkey["values"] = ("Select", "Your Birth Place", "Your cadet code", "Your first place of posting")
                self.ssqkey.place(x=50, y=110, width=250)
                self.ssqkey.current(0)

                #  security answer
                saname = Label(self.root2, text="Security Answer", font=("e Enougha", 15), bg="#e67257",
                               fg="white")
                saname.place(x=50, y=150)

                self.saname_entry = ttk.Entry(self.root2, font=("e Enougha", 12))
                self.saname_entry.place(x=50, y=180, width=250)

                # new passcode
                newpass = Label(self.root2, text="Enter New password", font=("e Enougha", 15), bg="#e67257",
                                fg="white")
                newpass.place(x=50, y=220)

                self.newpassentry = ttk.Entry(self.root2, font=("Britannic Bold", 12))
                self.newpassentry.place(x=50, y=250, width=250)
                sbt = Button(self.root2, command=self.resetpass, text="Reset",
                             font=("e Enougha", 11), fg="white",
                             bg="#006a41")
                sbt.place(x=120, y=330, width=100)


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # txtspeech
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_cname = StringVar()
        self.var_Ename = StringVar()
        self.var_ssqname = StringVar()
        self.var_saname = StringVar()
        self.var_pwd = StringVar()
        self.var_cnfpwd = StringVar()
        # bgimg
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\sidha\CS_Project\register.jpg")
        bglbl = Label(self.root, image=self.bg)
        bglbl.place(x=0, y=0, relheight=1, relwidth=1)

        # lftimg
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\sidha\CS_Project\left.jpg")
        lftlbl = Label(self.root, image=self.bg1)
        lftlbl.place(x=120, y=100, width=470, height=550)

        # frame
        frame = Frame(self.root, bg="white")
        frame.place(x=591, y=100, width=800, height=550)

        registerlbl = Label(frame, text="REGISTER NEW OFFICER", font=("Britannic Bold", 20), fg="#006e44",
                            bg="white")
        registerlbl.place(x=20, y=20)

        # fname
        fname = Label(frame, text="First Name", font=("Britannic Bold", 15), bg="white", fg="#158453")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("Britannic Bold", 12))
        self.fname_entry.place(x=50, y=130, width=250)
        # lname
        lname = Label(frame, text="Last Name", font=("Britannic Bold", 15), bg="white", fg="#158453")
        lname.place(x=450, y=100)

        self.lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("Britannic Bold", 12))
        self.lname_entry.place(x=450, y=130, width=250)

        # contact-----------------------------------------------
        cname = Label(frame, text="Contact Number", font=("Britannic Bold", 15), bg="white", fg="#158453")
        cname.place(x=50, y=180)

        self.cname_entry = ttk.Entry(frame, textvariable=self.var_cname, font=("Britannic Bold", 12))
        self.cname_entry.place(x=50, y=210, width=250)

        # Email
        Ename = Label(frame, text="Email ID", font=("Britannic Bold", 15), bg="white", fg="#158453")
        Ename.place(x=450, y=180)

        self.ename_entry = ttk.Entry(frame, textvariable=self.var_Ename, font=("Britannic Bold", 12))
        self.ename_entry.place(x=450, y=210, width=250)

        # security question
        ssqname = Label(frame, text="Select Security Question", font=("Britannic Bold", 15), bg="white", fg="#158453")
        ssqname.place(x=50, y=260)

        self.ssqkey = ttk.Combobox(frame, textvariable=self.var_ssqname, font=("Britannic Bold", 12),
                                   state="readonly")
        self.ssqkey["values"] = ("Select", "Your Birth Place", "your cadet code", "your first place of posting")
        self.ssqkey.place(x=50, y=290, width=250)
        self.ssqkey.current(0)

        #  security answer
        saname = Label(frame, text="Security Answer", font=("Britannic Bold", 15), bg="white", fg="#158453")
        saname.place(x=450, y=260)

        self.saname_entry = ttk.Entry(frame, textvariable=self.var_saname, font=("Britannic Bold", 12))
        self.saname_entry.place(x=450, y=290, width=250)

        # -----------------------------------------------
        pwd = Label(frame, text="Password", font=("Britannic Bold", 15), bg="white", fg="#158453")
        pwd.place(x=50, y=340)

        self.pwd_entry = ttk.Entry(frame, show="*", textvariable=self.var_pwd, font=("Britannic Bold", 12))
        self.pwd_entry.place(x=50, y=370, width=250)

        # cnfpwd
        cnfpwd = Label(frame, text="Confirm Password", font=("Britannic Bold", 15), bg="white", fg="#158453")
        cnfpwd.place(x=450, y=340)

        self.cnfpwd_entry = ttk.Entry(frame, show="*", textvariable=self.var_cnfpwd, font=("Britannic Bold", 12))
        self.cnfpwd_entry.place(x=450, y=370, width=250)

        # registerbtn
        img = Image.open(r"C:\Users\sidha\CS_Project\rgbtn.png")
        img = img.resize((150, 30), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.reg_data, image=self.photoimage, borderwidth=0, cursor="hand2", bg="white",
                    activebackground="white")
        b1.place(x=250, y=430, width=280)

    # function declaration
    def reg_data(self):
        if self.var_fname.get() == "" or self.var_Ename.get() == "" or self.var_lname.get() == "" or self.var_cname.get() == "" or self.var_saname.get() == "" or self.var_ssqname.get() == "Select" or self.var_pwd.get() == "" or self.var_pwd.get() == "":
            self.engine.say("All fields are required")
            self.engine.runAndWait()
            messagebox.showerror("Error", "All fields are needed to be filled!", parent=self.root)
        elif self.var_pwd.get() != self.var_cnfpwd.get():
            self.engine.say("The password and confirm password fields inputs do not match")
            self.engine.runAndWait()
            messagebox.showerror("Error", "The password and confirm password field values do not match!",
                                 parent=self.root)
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="Gmailsid2211", database="PolisysRMS",
                                          charset="utf8")
            cobj = con.cursor()
            q = "select * from registeruser where email=%s"
            v = (self.var_Ename.get(),)
            cobj.execute(q, v)
            row = cobj.fetchone()
            if row is not None:
                self.engine.say("Try another email. User already exists")
                self.engine.runAndWait()
                messagebox.showerror("Error", "User already exists. Please try another email", parent=self.root)
            else:
                cobj.execute("insert into registeruser values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(), self.var_lname.get(), self.var_cname.get(), self.var_Ename.get(),
                    self.var_ssqname.get(), self.var_saname.get(), self.var_pwd.get()))

            con.commit()
            con.close()
            self.engine.say("Registered the user successfully")
            self.engine.runAndWait()
            messagebox.showinfo("Success", "Registered successfully", parent=self.root)
            self.root.destroy()


class Criminal:
    def __init__(self, root):
        self.root3 = None
        self.root = root
        self.root.geometry('1550x800+0+0')
        self.root.title('First Information Report')

        # txtspeech
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

        # variables
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthmark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()

        lbl_title = Label(self.root, text="PoliSysRMS", font=('e Enougha', 40), bg='#ff6760', fg='#ffeb5a')
        lbl_title.place(x=0, y=0, width=1550, height=70)

        imglogo = Image.open('C:/Users/sidha/CS_Project/logo2.png')
        imglogo = imglogo.resize((65, 65), Image.ANTIALIAS)
        self.photologo = ImageTk.PhotoImage(imglogo)

        self.logo = Label(self.root, image=self.photologo, bg="#ff6760")
        self.logo.place(x=570, y=3, width=65, height=65)

        # imagebg
        imgframe = Frame(self.root, bd=2, relief=RIDGE, bg="#F2BF5E")
        imgframe.place(x=0, y=70, width=1550, height=800)

        imglogo2 = Image.open('C:/Users/sidha/CS_Project/banner.jpg')
        imglogo2 = imglogo2.resize((1550, 800), Image.ANTIALIAS)
        self.photologo2 = ImageTk.PhotoImage(imglogo2)

        self.logo2 = Label(self.root, image=self.photologo2, bg="#ff6760")
        self.logo2.place(x=0, y=70, width=1550, height=800)

        # MAIN FRAME
        Main_frame = Frame(self.root, bd=2, bg='#ff6760')
        Main_frame.place(x=10, y=200, width=1500, height=560)

        # UPPER FRAME
        upper_frame = LabelFrame(Main_frame, bd=0, relief=SUNKEN, text='Criminal Information',
                                 font=('e Enougha', 20), fg='white', bg='#ff6760')
        upper_frame.place(x=10, y=10, width=1480, height=270)

        # Label
        # Case ID
        caseid = Label(upper_frame, text='Case ID: ', font=('arial', 11, 'bold'), fg="white", bg="#e77357")
        caseid.grid(row=0, column=0, padx=2, sticky=W)

        caseentry = ttk.Entry(upper_frame, textvariable=self.var_case_id, width=22, font=('arial', 11, 'bold'))
        caseentry.grid(row=0, column=1, padx=2, sticky=W)

        # Criminal No
        lbl_criminal_no = Label(upper_frame, text="Criminal No: ", font=('arial', 12, 'bold'), fg="white", bg="#e77357")
        lbl_criminal_no.grid(row=0, column=2, sticky=W, padx=2, pady=5)

        lbl_criminal_entry = ttk.Entry(upper_frame, textvariable=self.var_criminal_no, width=22, font=("arial", 11, "bold"))
        lbl_criminal_entry.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        # Criminal name
        lbl_name = Label(upper_frame, font=('arial', 12, 'bold'), text="Criminal Name: ", fg="white", bg="#e77357")
        lbl_name.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=("arial", 11, "bold"))
        txt_name.grid(row=1, column=1, padx=2, pady=7)

        # Arrest Date
        lbl_arrestDate = Label(upper_frame, font=('arial', 12, 'bold'), text="Arrest Date: ", fg='white', bg="#e77357")
        lbl_arrestDate.grid(row=2, column=0, sticky=W, padx=2, pady=7)

        txt_arrestDate = ttk.Entry(upper_frame, textvariable=self.var_arrest_date, width=22, font=("arial", 11, "bold"))
        txt_arrestDate.grid(row=2, column=1, padx=2, pady=7)

        # Date Of Crime
        lbl_dateofCrime = Label(upper_frame, font=("arial", 12, "bold"), text="Date Of Crime: ", fg='white',
                                bg="#e77357")
        lbl_dateofCrime.grid(row=2, column=2, sticky=W, padx=2, pady=7)

        txt_dateofCrime = ttk.Entry(upper_frame, textvariable=self.var_date_of_crime, width=22,
                                    font=("arial", 11, "bold"))
        txt_dateofCrime.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # Address
        lbl_address = Label(upper_frame, font=("arial", 12, "bold"), text="Address: ", bg="#e77357", fg='white')
        lbl_address.grid(row=3, column=0, sticky=W, padx=2, pady=7)
        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=("arial", 11, "bold"))
        txt_address.grid(row=3, column=1, padx=2, pady=7)

        # Age
        lbl_age = Label(upper_frame, font=("arial", 12, "bold"), text="Age: ", bg="#e77357", fg='white')
        lbl_age.grid(row=3, column=2, sticky=W, padx=2, pady=7)
        txt_age = ttk.Entry(upper_frame, textvariable=self.var_age, width=22, font=("arial", 11, "bold"))
        txt_age.grid(row=3, column=3, padx=2, pady=7)

        # Occupation
        lbl_occupation = Label(upper_frame, font=("arial", 12, "bold"), text="Occupation: ", bg="#e77357", fg='white')
        lbl_occupation.grid(row=4, column=0, sticky=W, padx=2, pady=7)
        txt_occupation = ttk.Entry(upper_frame, textvariable=self.var_occupation, width=22, font=("arial", 11, "bold"))
        txt_occupation.grid(row=4, column=1, padx=2, pady=7)

        # Birthmark
        lbl_birthmark = Label(upper_frame, font=("arial", 12, "bold"), text="Birthmark: ", bg='#e77357', fg='white')
        lbl_birthmark.grid(row=4, column=2, sticky=W, padx=2, pady=7)
        txt_birthmark = ttk.Entry(upper_frame, textvariable=self.var_birthmark, width=22, font=("arial", 11, "bold"))
        txt_birthmark.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # Crime Type
        lbl_crimeType = Label(upper_frame, font=("arial", 12, "bold"), text="Crime Type: ", bg='#e77357', fg='white')
        lbl_crimeType.grid(row=0, column=4, sticky=W, padx=2, pady=7)
        txt_crimeType = ttk.Entry(upper_frame, textvariable=self.var_crime_type, width=22, font=("arial", 11, "bold"))
        txt_crimeType.grid(row=0, column=5, padx=2, pady=7)
        # Guadrian's Name
        lbl_guardianName = Label(upper_frame, font=("arial", 12, "bold"), text="Father's Name: ", bg='#e77357', fg='white')
        lbl_guardianName.grid(row=1, column=4, sticky=W, padx=2, pady=7)
        txt_guardianName = ttk.Entry(upper_frame, textvariable=self.var_father_name, width=22, font=("arial", 11, "bold"))
        txt_guardianName.grid(row=1, column=5, padx=2, pady=7)

        # gender
        lbl_gender = Label(upper_frame, font=("arial", 12, "bold"), text="Gender", bg='#e77357', fg='white')
        lbl_gender.grid(row=2, column=4, sticky=W, padx=2, pady=7)
        # wanted
        lbl_wanted = Label(upper_frame, font=('arial', 12, 'bold'), text="Most Wanted: ", bg='#e77357', fg='white')
        lbl_wanted.grid(row=3, column=4, sticky=W, padx=2, pady=7)

        # Button Gender
        frame_gender = Frame(upper_frame, bd=2, relief=RIDGE, bg='#e77357')
        frame_gender.place(x=745, y=85, width=100, height=27)
        male = Radiobutton(frame_gender, variable=self.var_gender, text='M', value='male', font=("arial", 7, 'bold'),
                           bg="#e77357", fg="white",
                           activebackground="#e77357", activeforeground="white")
        male.grid(row=0, column=0, pady=1, padx=5, sticky=W)

        female = Radiobutton(frame_gender, variable=self.var_gender, text='F', value='female',
                             font=("arial", 7, 'bold'), bg='#e77357',
                             fg="white", activebackground="#e77357", activeforeground="white")
        female.grid(row=0, column=1, pady=1, padx=5, sticky=W)

        # Button Wanted
        frame_wanted = Frame(upper_frame, bd=2, relief=RIDGE, bg='#e77357')
        frame_wanted.place(x=745, y=123, height=30)
        yes = Radiobutton(frame_wanted, variable=self.var_wanted, text='Yes', value='yes', font=("arial", 8, 'bold'),
                          bg='#e77357', fg="white",
                          activebackground="#e77357", activeforeground="white")
        yes.grid(row=0, column=0, pady=2, padx=5, sticky=W)
        no = Radiobutton(frame_wanted, variable=self.var_wanted, text='No', value='no', font=("arial", 8, 'bold'),
                         bg='#e77357', fg="white",
                         activebackground="#e77357", activeforeground="white")
        no.grid(row=0, column=1, pady=2, padx=5, sticky=W)

        # Buttons
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='#ff985b')
        button_frame.place(x=5, y=200, width=620, height=45)
        # Add button
        btn_add = Button(button_frame, command=self.add_data, text='SAVE', font=('arial', 13, 'bold'), width=14,
                         bg='#f44f47',
                         fg='white')
        btn_add.grid(row=0, column=0, padx=2, pady=3)
        # Update button
        btn_update = Button(button_frame, command=self.update, text='UPDATE', font=('arial', 13, 'bold'), width=14,
                            bg='#f44f47',
                            fg='white')
        btn_update.grid(row=0, column=1, padx=2, pady=3)
        # Delete button
        btn_delete = Button(button_frame, command=self.deletedata, text='DELETE', font=('arial', 13, 'bold'), width=14,
                            bg='#f44f47',
                            fg='white')
        btn_delete.grid(row=0, column=2, padx=2, pady=3)
        # Clear button
        btn_clear = Button(button_frame, command=self.cleardata, text='CLEAR', font=('arial', 13, 'bold'), width=14,
                           bg='#f44f47', fg='white')
        btn_clear.grid(row=0, column=3, padx=2, pady=3)

        # bgrimg
        bgimg = Image.open('C:/Users/sidha/CS_Project/logo2.png')
        bgimg = bgimg.resize((270, 270), Image.ANTIALIAS)
        self.photologo3 = ImageTk.PhotoImage(bgimg)

        self.logo3 = Label(self.root, image=self.photologo3, bg="#ff6760")
        self.logo3.place(x=1110, y=210, width=270, height=270)

        # LOWER FRAME
        lower_frame = LabelFrame(Main_frame, bd=2, text='Criminal Information Table',
                                 font=('e Enougha', 20), fg='white', bg="#f44f47")
        lower_frame.place(x=10, y=285, width=1470, height=270)

        # SEARCH FRAME
        search_frame = LabelFrame(lower_frame, bd=2, text='Search Criminal Record',
                                  font=('e Enougha', 16), fg='white', bg="#ff7b30")
        search_frame.place(x=0, y=5, width=1460, height=70)

        search_by = Label(search_frame, font=("arial", 11, "bold"), text="Search By: ", bg='#f44f47', fg='white')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        self.var_con_search = StringVar()
        combo_search_box = ttk.Combobox(search_frame, textvariable=self.var_con_search, font=('arial', 11, 'bold'),
                                        width=18, state='read')
        combo_search_box['value'] = ('Select Option', 'Case_ID', 'Criminal_Number')
        combo_search_box.current(0)
        combo_search_box.grid(row=0, column=1, sticky=W, padx=5)

        self.var_search = StringVar()
        search_txt = ttk.Entry(search_frame, textvariable=self.var_search, width=18, font=('arial', 13, 'bold'))
        search_txt.grid(row=0, column=2, sticky=W, padx=5)

        # Search button
        btn_search = Button(search_frame, command=self.search, text='Search', font=('arial', 13, 'bold'), width=14,
                            bg='#f44f47',
                            fg='white')
        btn_search.grid(row=0, column=3, padx=3, pady=5)
        # All button
        btn_all = Button(search_frame, command=self.fetchdata, text='Show All', font=('arial', 13, 'bold'), width=14,
                         bg='#f44f47',
                         fg='white')
        btn_all.grid(row=0, column=4, padx=3, pady=5)

        crimeagency = Label(search_frame, font=('e Enougha', 20), text='CRIMINAL(S) RECORD BOOK', bg='#ff7b30',
                            fg='white')
        crimeagency.grid(row=0, column=7, sticky=W, padx=30, pady=0)

        # Table Frame
        table_frame = Frame(lower_frame, bd=2)
        table_frame.place(x=7, width=1450, y=80, height=150)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.criminal_table = ttk.Treeview(table_frame, column=(
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'), xscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)

        self.criminal_table.heading('1', text='CaseID')
        self.criminal_table.heading('2', text='CrimeNo')
        self.criminal_table.heading('3', text='Criminal Name')
        self.criminal_table.heading('4', text='ArrestDate')
        self.criminal_table.heading('5', text='CrimeOfDate')
        self.criminal_table.heading('6', text='Address')
        self.criminal_table.heading('7', text='Age')
        self.criminal_table.heading('8', text='Occupation')
        self.criminal_table.heading('9', text='Birth Mark')
        self.criminal_table.heading('10', text='Crime Type')
        self.criminal_table.heading('11', text='Father Name')
        self.criminal_table.heading('12', text='Gender')
        self.criminal_table.heading('13', text='Wanted')

        self.criminal_table['show'] = 'headings'

        self.criminal_table.column('1', width=100)
        self.criminal_table.column('2', width=100)
        self.criminal_table.column('3', width=100)
        self.criminal_table.column('4', width=100)
        self.criminal_table.column('5', width=100)
        self.criminal_table.column('6', width=100)
        self.criminal_table.column('7', width=100)
        self.criminal_table.column('8', width=100)
        self.criminal_table.column('9', width=100)
        self.criminal_table.column('10', width=100)
        self.criminal_table.column('11', width=100)
        self.criminal_table.column('12', width=100)
        self.criminal_table.column('13', width=100)

        self.criminal_table.pack(fill=BOTH, expand=1)

        self.criminal_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetchdata()

    # add function
    def add_data(self):
        if self.var_case_id.get() == "" or self.var_criminal_no.get() == "":
            self.engine.say("Please fill the compulsory fields")
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please fill all the fields")
        else:
            try:
                conn3 = mysql.connector.connect(user="root", host="localhost", password="Gmailsid2211",
                                                database="polisysrms", charset="utf8")
                cobj = conn3.cursor()

                cobj.execute('insert into criminalrec values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_case_id.get(), self.var_criminal_no.get(), self.var_name.get(), self.var_arrest_date.get(),
                    self.var_date_of_crime.get(), self.var_address.get(), self.var_age.get(), self.var_occupation.get(),
                    self.var_birthmark.get(), self.var_crime_type.get(), self.var_father_name.get(),
                    self.var_gender.get(),
                    self.var_wanted.get()))
                conn3.commit()
                self.fetchdata()
                self.cleardata()
                conn3.close()
                self.engine.say("Data added to the database successfully")
                self.engine.runAndWait()
                messagebox.showinfo("Success", "Data successfully registered in the database.", parent=self.root)
            except Exception as es:
                self.engine.say("Error")
                self.engine.runAndWait()
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    # fetch data
    def fetchdata(self):
        conn = mysql.connector.connect(user="root", host="localhost", password="Gmailsid2211",
                                       database="polisysrms", charset="utf8")
        cobj = conn.cursor()
        cobj.execute('select * from criminalrec')
        data = cobj.fetchall()
        if len(data) != 0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.criminal_table.focus()
        content = self.criminal_table.item(cursor_row)
        data = content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_arrest_date.set(data[3])
        self.var_date_of_crime.set(data[4])
        self.var_address.set(data[5])
        self.var_age.set(data[6])
        self.var_occupation.set(data[7])
        self.var_birthmark.set(data[8])
        self.var_crime_type.set(data[9])
        self.var_father_name.set(data[10])
        self.var_gender.set(data[11])
        self.var_wanted.set(data[12])

    # update
    def update(self):
        global conn
        if self.var_case_id.get() is None:
            self.engine.say("All fields are required")
            self.engine.runAndWait()
            messagebox.showerror("Error", "All fields required.", parent=self.root)
        else:
            try:
                self.engine.say("Are you sure about the changes")
                self.engine.runAndWait()
                update = messagebox.askyesno('Update', 'Are you sure about the changes?', parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(user="root", host="localhost", password="Gmailsid2211",
                                                   database="polisysrms", charset="utf8")
                    cobj = conn.cursor()
                    cobj.execute(
                        "update criminalrec set Criminal_Number=%s,criminal_name=%s,date_of_arrest=%s,"
                        "date_of_crime=%s,address=%s,age=%s,occupation=%s,birthmark=%s,crime_type=%s,father_name=%s,"
                        "gender=%s,wanted=%s where Case_ID=%s",
                        (self.var_criminal_no.get(), self.var_name.get(), self.var_arrest_date.get(),
                         self.var_date_of_crime.get(), self.var_address.get(), self.var_age.get(),
                         self.var_occupation.get(), self.var_birthmark.get(), self.var_crime_type.get(),
                         self.var_father_name.get(), self.var_gender.get(), self.var_wanted.get(),
                         self.var_case_id.get()))
                    conn.commit()
                    self.fetchdata()
                    self.cleardata()
                    conn.close()
                    self.engine.say("Record has been successfully updated")
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Record successfully updated!", parent=self.root)

                else:
                    if not update:
                        return

            except Exception as es:
                self.engine.say("Error")
                self.engine.runAndWait()
                messagebox.showerror("Error", f'Due to {str(es)}', parent=self.root)

    # delete
    def deletedata(self):
        if self.var_case_id.get() is None:
            self.engine.say("Error")
            self.engine.runAndWait()
            messagebox.showerror("Error", "All fields required.", parent=self.root)
        else:
            try:
                self.engine.say("Are you sure about deletion of the record")
                self.engine.runAndWait()
                delete = messagebox.askyesno('Update', 'Are you sure about the deletion?', parent=self.root)
                if delete > 0:
                    conn2 = mysql.connector.connect(user="root", host="localhost", password="Gmailsid2211",
                                                    database="polisysrms", charset="utf8")
                    cobj = conn2.cursor()
                    cobj.execute('delete from criminalrec where Case_ID=%s', (str(self.var_case_id.get()),))

                    self.engine.say("Record deleted successfully")
                    self.engine.runAndWait()
                    messagebox.showinfo("Success", "Record successfully Deleted!", parent=self.root)
                    conn2.commit()
                    self.fetchdata()
                    self.cleardata()
                    conn2.close()
                else:
                    if not delete:
                        return

            except Exception as es:
                self.engine.say("Error")
                self.engine.runAndWait()
                messagebox.showerror("Error", f'Due to {str(es)}', parent=self.root)

    # clear
    def cleardata(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthmark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")

    # search
    def search(self):
        if self.var_con_search.get() == "":
            self.engine.say("Please fill in all the fields")
            self.engine.runAndWait()
            messagebox.showerror("Error", "All fields required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user="root", host="localhost", password="Gmailsid2211",
                                               database="polisysrms", charset="utf8")
                cobj = conn.cursor()

                cobj.execute('select * from criminalrec where ' + str(self.var_con_search.get()) + " like '%" + str(
                    self.var_search.get()) + "%'")
                row = cobj.fetchall()
                if len(row) != 0:
                    self.criminal_table.delete(*self.criminal_table.get_children())
                    for i in row:
                        self.criminal_table.insert("", END, values=i)
                conn.commit()

                conn.close()
            except Exception as es:
                self.engine.say("Error")
                self.engine.runAndWait()
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


if __name__ == '__main__':
    main()