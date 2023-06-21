from tkinter import * 
from tkinter import messagebox
from MyDb import *  
from time import *  
from PIL import ImageTk, Image 
import uuid  




#opening screen
SplashScreen = Tk() 
SplashScreen.config(bg="#000000", ) 
SplashScreen.geometry("1920x1080") 
SplashScreen.overrideredirect(True)  



#Opening screen img
DBImg = Image.open("financial company.png")  
ResizeDB = DBImg.resize((500,500),Image.ANTIALIAS) 
NewDBImg = ImageTk.PhotoImage(ResizeDB) 
DBLabel = Label(SplashScreen,image=NewDBImg,bg="black") 
DBLabel.place(relx=0.5,rely=0.5, anchor=CENTER)

      

#Login Screen
def LoginScreen():
    SplashScreen.destroy()
    screen = Tk()  
    screen.geometry("1440x600")
    screen.title("Z.G.R. BANK LOGİN") 
    screen.configure(background="white") 
    screen.resizable(False,False)  
   
    
    #LogIn func 
    def LogIn(): 
        username = UserEntry.get() 
        password = PassEntry.get() 
        
        cl = SeacrhClient(username) 
        print(cl)
        try:
            if username=="admin" and password=="admin": 
                AdminViewPage() 
            elif cl[0][0] == username and cl[0][2] == password: 
                screen.destroy()
                NormalViewPage() 
            else: 
                messagebox.showwarning("error","Name  or Password wrong !!")
        except: 
            messagebox.showwarning("error","Fill the blanks")
            
            
            
               
                
    #Admin View Page
    def AdminViewPage(): 
        try:
            screen.destroy() 
             
        except:  
            pass   
        finally:     
            AdminScreen = Tk() 
            AdminScreen.geometry("1440x900")
            AdminScreen.title("A D M I N  V I E W")    
            AdminScreen.resizable(False,False)  
            AdminScreen.config(bg="white")  
        
        
        
        #Admin Page frames
        Add_Client = Frame(AdminScreen,width=400,height=400,bg="white",)  
        SearchByName = Frame(AdminScreen,width=400,height=400,bg="white",) 
        ChangeUserInfo = Frame(AdminScreen,width=400,height=400,bg="white",)
        ShowAllDB = Frame(AdminScreen,width=400,height=400,bg="white",)  
        #Grid layout
        Add_Client.grid(row=0,column=0,padx=160,pady=20) 
        SearchByName.grid(row=0,column=1,padx=160,pady=20) 
        ChangeUserInfo.grid(row=1,column=0,padx=160,pady=20) 
        ShowAllDB.grid(row=1,column=1,padx=160,pady=20) 
        
        #Add user section
        UserPng = Image.open("user.png") 
        ResizeUserPng = UserPng.resize((250,250), Image.ANTIALIAS) 
        NewUserPng = ImageTk.PhotoImage(ResizeUserPng) 
        UserPngLabel = Label(Add_Client,image=NewUserPng,bg="white") 
        UserPngLabel.place(relx=0.5,rely=0.4,anchor=CENTER,) 
        
        #Add user button  
        AddUserButton = Button(
            Add_Client,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=13,
            height=2,
            border=0,
            cursor="hand2", 
            text="Add User", 
            font=("Oswald", 16,"bold"), 
            command=lambda:Add_Client()
            ) 
        AddUserButton.place(relx=0.5,rely=0.9,anchor=CENTER) 
        
        #Search user section 
        SearchPng = Image.open("search.png") 
        ResizeSearchPng = SearchPng.resize((250,250),Image.ANTIALIAS) 
        NewSearchPng = ImageTk.PhotoImage(ResizeSearchPng) 
        SearchLabel = Label(SearchByName,image=NewSearchPng,bg="white") 
        SearchLabel.place(relx=0.5,rely=0.4,anchor=CENTER) 
        
        #Search user button 
        SearchUserButton = Button(
            SearchByName,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=13,
            height=2,
            border=0,
            cursor="hand2", 
            text="Search User", 
            font=("Oswald", 16,"bold"),
            ) 
        SearchUserButton.place(relx=0.44,rely=0.9,anchor=CENTER) 
        
        #Change User Info section 
        ChangePng = Image.open("social-media.png") 
        ResizeChangePng = ChangePng.resize((250,250),Image.ANTIALIAS) 
        NewChangePng = ImageTk.PhotoImage(ResizeChangePng) 
        ChangeLabel = Label(ChangeUserInfo,image=NewChangePng,bg="white") 
        ChangeLabel.place(relx=0.5,rely=0.4,anchor=CENTER)  
        
        #Change user info button 
        ChangeUserButton = Button(
            ChangeUserInfo,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=13,
            height=2,
            border=0,
            cursor="hand2", 
            text="Change info", 
            font=("Oswald", 16,"bold"),
            ) 
        ChangeUserButton.place(relx=0.5,rely=0.9,anchor=CENTER) 
        
        #See All database section 
        DBPng = Image.open("customer.png") 
        ResizeDBPng = DBPng.resize((250,250),Image.ANTIALIAS) 
        NewDBPng = ImageTk.PhotoImage(ResizeDBPng) 
        DBLabel = Label(ShowAllDB,image=NewDBPng,bg="white") 
        DBLabel.place(relx=0.44,rely=0.4,anchor=CENTER)   
        
        #Database button 
        DButton = Button(
            ShowAllDB,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=13,
            height=2,
            border=0,
            cursor="hand2", 
            text="Database", 
            font=("Oswald", 16,"bold"),
            ) 
        DButton.place(relx=0.44,rely=0.9,anchor=CENTER)
        
        def Add_Client():   
            AdminScreen.destroy() 
            AddUserPage = Tk() 
            AddUserPage.geometry("1440x900")
            AddUserPage.title("A D D  U S E R")    
            AddUserPage.resizable(False,False)  
            AddUserPage.config(bg="white")  
            
            
            
            BackButton = Button(
            AddUserPage,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=10,
            height=1,
            border=0,
            cursor="hand2", 
            text="Back", 
            font=("Oswald", 16,"bold"), 
            command=AdminViewPage
            ) 
            BackButton.place(x=0,y=0)
            
            
            def on_enter(e): 
                NameEntry.delete(0,"end")
            def on_leave(e): 
                if NameEntry.get()=="": 
                    NameEntry.insert(0,"Name") 
            
            #Name entry
            NameEntry = Entry(AddUserPage,width=25,fg="black",border=0,bg="#F0BA1D",font=("Microsoft YaHei UI Light",10)) 
            NameEntry.pack(padx=40,pady=40) 

            NameEntry.insert(0,"Name")
            NameEntry.bind("<FocusIn>",on_enter) 
            NameEntry.bind("<FocusOut>",on_leave)
           
           
           
           
           
            def on_enter(e): 
                SurNameEntry.delete(0,"end")
            def on_leave(e): 
                if SurNameEntry.get()=="": 
                    SurNameEntry.insert(0,"Surname") 
            #Surname entry
            SurNameEntry = Entry(AddUserPage,width=25,fg="black",border=0,bg="#F0BA1D",font=("Microsoft YaHei UI Light",10)) 
            SurNameEntry.pack(padx=40,pady=40)  
            
            
            SurNameEntry.insert(0,"Surname")
            SurNameEntry.bind("<FocusIn>",on_enter) 
            SurNameEntry.bind("<FocusOut>",on_leave)
        
            
            
            
            def on_enter(e): 
                PasswEntry.delete(0,"end")
            def on_leave(e): 
                if PasswEntry.get()=="": 
                    PasswEntry.insert(0,"Surname") 
            #Password
            PasswEntry = Entry(AddUserPage,width=25,fg="black",border=0,bg="#F0BA1D",font=("Microsoft YaHei UI Light",10),show="*") 
            PasswEntry.pack(padx=40,pady=40) 
            
            PasswEntry.insert(0,"Password")
            PasswEntry.bind("<FocusIn>",on_enter) 
            PasswEntry.bind("<FocusOut>",on_leave)
            
            
            
            
            admin_button = Button(AddUserPage, text="Admin Button",command=lambda: SetValue(NameEntry.get(),SurNameEntry.get(),PasswEntry.get(),str(uuid.uuid4())))
            admin_button.pack() 
        
        

        mainloop()
    
    

    #Sign up screen
    def SignUpP(): 
        screen.destroy() 
        SignUp = Tk() 
        SignUp.geometry("1440x900")  
        SignUp.title("S I G N  U P")   
        SignUp.resizable(False ,False) 
        SignUp.configure(bg="#fff")
        
        
            
        #Sign up Icon 
        img= PhotoImage(file="add-friend.png") 
        ImgLabel= Label(SignUp, image=img,border=0,bg="white") 
        ImgLabel.place(x=50,y=90) 
        
        #Sign frame 
        SignFrame = Frame(SignUp, width=350,height=390,bg="#fff") 
        SignFrame.place(x=900,y=100)
        
        #Heading Label 
        Head = Label(text="S I G N  U P",fg="#F0BA1D",bg="#fff",font=("Microsoft YaHei UI Light",24,"bold") ) 
        Head.place(x=980,y=100) 
        
        #Username entry 
        def on_enter(e): 
            user.delete(0,"end") 
        def on_leave(e): 
            if user.get()=="": 
                user.insert(0,"Username") 
        
        user = Entry(SignFrame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light",10)) 
        user.place(x=30, y=80)
        user.insert(0,"Username")
        user.bind("<FocusIn>",on_enter) 
        user.bind("<FocusOut>",on_leave) 
        
        UserFrame = Frame(SignFrame, width=295,height=2,bg="black") 
        UserFrame.place(x=25,y=107) 
        
        
        
        #Surname Entry 
        def on_enter(e): 
            Sur.delete(0,"end") 
        def on_leave(e): 
            if Sur.get()=="": 
                Sur.insert(0,"Surname") 
        
        Sur = Entry(SignFrame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light",10)) 
        Sur.place(x=30, y=150)
        Sur.insert(0,"Surname")
        Sur.bind("<FocusIn>",on_enter) 
        Sur.bind("<FocusOut>",on_leave) 
        
        SurFrame = Frame(SignFrame, width=295,height=2,bg="black") 
        SurFrame.place(x=25,y=177)    
        
        #Password entry 
        def on_enter(e): 
            PassW.delete(0,"end") 
        def on_leave(e): 
            if PassW.get()=="": 
                PassW.insert(0,"Password") 
        
        PassW = Entry(SignFrame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light",10),show="*") 
        PassW.place(x=30, y=230)
        PassW.insert(0,"Password")
        PassW.bind("<FocusIn>",on_enter) 
        PassW.bind("<FocusOut>",on_leave) 
        
        PassWFrame = Frame(SignFrame, width=295,height=2,bg="black") 
        PassWFrame.place(x=25,y=260)  
        
        
        #Password Confirmation 
        def on_enter(e): 
            COnfirm.delete(0,"end") 
        def on_leave(e): 
            if COnfirm.get()=="": 
                COnfirm.insert(0,"Password") 
        
        COnfirm = Entry(SignFrame, width=25, fg="black", border=0, bg="white",font=("Microsoft YaHei UI Light",10),show="*") 
        COnfirm.place(x=30, y=300)
        COnfirm.insert(0,"Password")
        COnfirm.bind("<FocusIn>",on_enter) 
        COnfirm.bind("<FocusOut>",on_leave) 
        
        COnfirmFrame = Frame(SignFrame, width=295,height=2,bg="black") 
        COnfirmFrame.place(x=25,y=330)  
        
        #Sign Up 
        SignButton = Button(SignFrame, width=39,pady=7,text="Sign Up",bg="#F0BA1D",fg="white",border=0,command=lambda: Sign_Up())  
        SignButton.place(x=35,y=350)
           
          #Sign Command 
        def Sign_Up(): 
            
            username = user.get() 
            surname = Sur.get() 
            if PassW.get() == COnfirm.get(): 
                password = PassW.get() 
                SetValue(username,surname,password,str(uuid.uuid4()))
                SignUp.destroy()
                NormalViewPage()
            elif PassW.get() != COnfirm.get(): 
                messagebox.showwarning("E R R O R","Password doesn't match ! ! ")  
            else: 
                pass
        
        
        
        
        mainloop()
    

    #Normal View Page 
    def NormalViewPage():  
        NormalPageView = Tk() 
        NormalPageView.geometry("1440x900") 
        NormalPageView.title("N O R M A L  V I E W") 
        NormalPageView.mainloop()
    
    
    #Icon label
    BankIcon = ImageTk.PhotoImage(Image.open("ZGRBank.png")) 
    IconLabel = Label(screen,image=BankIcon,background="white") 
    IconLabel.place(x=70,y=50)    
    
    #Login frame
    LoginFrame = Frame(screen, width=900,height=800,bg="white") 
    LoginFrame.place(x=980,y=70) 
    
    #Log in label
    SignHead = Label(LoginFrame, text="Z G R  C O R P.",fg="#F0BA1D",bg="white",font=("Microsoft YaHei UI Light",30,"bold"))
    SignHead.place(x=60,y=5) 
    
    #User Enrty funcs
    def on_enter(e): 
        UserEntry.delete(0,"end") 
        
    def on_leave(e): 
        name = UserEntry.get() 
        if name == "": 
            UserEntry.insert(0,"Username")  
    #User name entry
    UserEntry = Entry(LoginFrame, width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10)) 
    UserEntry.place(x=70,y=80) 
    UserEntry.insert(0,"Username") 
    UserEntry.bind("<FocusIn>", on_enter) 
    UserEntry.bind("<FocusOut>",on_leave)
    MyFrame = Frame(LoginFrame, width=295,height=2,background="black",) 
    MyFrame.place(x=65,y=107) 
    
    def on_enter(e): 
        PassEntry.delete(0,"end") 
        
    def on_leave(e): 
        name = PassEntry.get() 
        if name == "": 
            PassEntry.insert(0,"password") 
    
    #Password entry
    PassEntry = Entry(LoginFrame, width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI Light",10),show="*") 
    PassEntry.place(x=70,y=150) 
    PassEntry.insert(0,"Password") 
    PassEntry.bind("<FocusIn>",on_enter) 
    PassEntry.bind("<FocusOut>", on_leave)
    PassFrame = Frame(LoginFrame, width=295,height=2,background="black",) 
    PassFrame.place(x=65,y=177) 
    
    #Log in button 
    LogButton = Button(LoginFrame, width=39,pady=7,text="Log in",bg="#F0BA1D",fg="white",border=0,command=LogIn) 
    LogButton.place(x=75,y=204)  
    
    
    #Sign up 
    SignLabel = Label(LoginFrame,text="Don't have an account?",fg="black",bg="white",font=("Microsoft YaHei UI Light",9)) 
    SignLabel.place(x=75,y=270) 
    SingUp =Button(LoginFrame,width=6,text="Sign up",border=0,bg="white",cursor="hand2",fg="#F0BA1D",command=SignUpP) 
    SingUp.place(x=215,y=270) 
    

    screen.mainloop()
    
  
   
DatabseConnection() 
#Splash scren timer 
SplashScreen.after(3000,LoginScreen)

        
mainloop()