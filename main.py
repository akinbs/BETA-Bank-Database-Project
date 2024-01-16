from tkinter import * 
from tkinter import messagebox
from MyDb import *  
from time import *  
from PIL import ImageTk, Image, ImageFilter

import uuid  
from tkinter import ttk 



#opening screen
SplashScreen = Tk() 
SplashScreen.config(bg="#000000", ) 
SplashScreen.geometry("1920x1080") 
SplashScreen.overrideredirect(True)  



#Opening screen img
DBImg = Image.open("PNG/financial company.png")  
ResizeDB = DBImg.resize((500,500),)
NewDBImg = ImageTk.PhotoImage(ResizeDB) 
DBLabel = Label(SplashScreen, image=NewDBImg, bg="black") 
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
        global username 
        username = UserEntry.get() 
        password = PassEntry.get() 
        global cl
        cl = SeacrhClient(username) 
        try:
            if username=="admin" and password=="admin": 
                AdminViewPage() 
            elif cl[0][0] == username and cl[0][2] == password: 
                screen.destroy()
                NormalViewPage() 
            else: 
                messagebox.showwarning("error","Name  or Password wrong !!")
        finally:
            print("logged in")
            
            
            
               
                
    #Admin View Page
    def AdminViewPage(): 
        
        try:
            screen.destroy()    
        except:  
            pass   
        
        #Admin Page    
        AdminScreen = Tk() 
        AdminScreen.geometry("1440x900")
        AdminScreen.title("A D M I N  V I E W")    
        AdminScreen.resizable(False,False)  
        AdminScreen.config(bg="white")  
        
        #Admin Page frames
        Add_Client = Frame(AdminScreen,width=400,height=400,bg="white",)  
        SearchByName = Frame(AdminScreen,width=400,height=400,bg="white",) 
        ChangeUserInfo = Frame(AdminScreen,width=400,height=400,bg="white",)
        ShowAllLog = Frame(AdminScreen,width=400,height=400,bg="white",)  
        
        #Grid layout
        Add_Client.grid(row=0,column=0,padx=160,pady=20) 
        SearchByName.grid(row=0,column=1,padx=160,pady=20) 
        ChangeUserInfo.grid(row=1,column=0,padx=160,pady=20) 
        ShowAllLog.grid(row=1,column=1,padx=160,pady=20) 
        
        #Add user section
        UserPng = Image.open("PNG/user.png") 
        ResizeUserPng = UserPng.resize((250,250), Image.ADAPTIVE)
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
            command=lambda: AddClient()
            ) 
        AddUserButton.place(relx=0.5,rely=0.9,anchor=CENTER) 
         
        
        #Search user section 
        SearchPng = Image.open("PNG/search.png") 
        ResizeSearchPng = SearchPng.resize((250,250),Image.ADAPTIVE) 
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
            command=lambda: SearchClientInfo() 
            ) 
        SearchUserButton.place(relx=0.44,rely=0.9,anchor=CENTER) 
        
        #Change User Info section 
        ChangePng = Image.open("PNG/social-media.png") 
        ResizeChangePng = ChangePng.resize((250,250),Image.ADAPTIVE) 
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
            command=lambda: ChangeUserPage()
            ) 
        ChangeUserButton.place(relx=0.5,rely=0.9,anchor=CENTER) 
        
        #See All database section 
        LogPng = Image.open("PNG/customer.png") 
        ResizeLogPng = LogPng.resize((250,250),Image.ADAPTIVE) 
        NewLogPng = ImageTk.PhotoImage(ResizeLogPng) 
        LogLabel = Label(ShowAllLog,image=NewLogPng,bg="white") 
        LogLabel.place(relx=0.44,rely=0.4,anchor=CENTER)   
        
        #Logs button 
        LogButton = Button(
            ShowAllLog,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=13,
            height=2,
            border=0,
            cursor="hand2", 
            text="Logs", 
            font=("Oswald", 16,"bold"), 
            command=lambda: UsersLogs()
            ) 
        LogButton.place(relx=0.44,rely=0.9,anchor=CENTER)
        
        #Add Client Page
        def AddClient():    
            AdminScreen.withdraw()  
            AddUserPage = Toplevel(AdminScreen)
            AddUserPage.geometry("1440x900")
            AddUserPage.title("A D D  U S E R")    
            AddUserPage.resizable(False,False)  
            AddUserPage.config(bg="white")  
            
            
            #Back button
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
            command=lambda: WhenClicked()
            ) 
            BackButton.place(x=0,y=0) 
            
            def WhenClicked(): 
                AddUserPage.withdraw()
                AdminScreen.deiconify() 
                
            #Add Client icon 
            MyPNG = Image.open("PNG/person.png") 
            ResizeMyPNG = MyPNG.resize((100,100), Image.ANTIALIAS) 
            global NewMyPNG
            NewMyPNG = ImageTk.PhotoImage(ResizeMyPNG) 
            MyPNGLabel = Label(AddUserPage, image=NewMyPNG, bg="white") 
            MyPNGLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
              
                    
            
            def on_enter(e): 
                NameEntry.delete(0,"end")
            def on_leave(e): 
                if NameEntry.get()=="": 
                    NameEntry.insert(0,"Name") 
            
            #Name entry
            NameEntry = Entry(AddUserPage,width=25,fg="black",border=0,bg="#F0BA1D",font=("Microsoft YaHei UI Light",10)) 
            NameEntry.place(relx=0.5,rely=0.3,anchor=CENTER) 

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
            SurNameEntry.place(relx=0.5,rely=0.4,anchor=CENTER)  
            
            
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
            PasswEntry.place(relx=0.5,rely=0.5,anchor=CENTER) 
            
            PasswEntry.insert(0,"Password")
            PasswEntry.bind("<FocusIn>",on_enter) 
            PasswEntry.bind("<FocusOut>",on_leave)
            
            
            
            #submit button
            SubmitButton = Button(AddUserPage, text="Submit",command=lambda: [SetValue(NameEntry.get(),SurNameEntry.get(),PasswEntry.get(),str(uuid.uuid4()),"No action"), WhenClicked()])
            SubmitButton.place(relx=0.5,rely=0.6,anchor=CENTER)  
            AddUserPage.mainloop()
        
        
        #Search Client Page
        def SearchClientInfo(): 
            AdminScreen.withdraw() 
            SearchScreen = Toplevel(AdminScreen) 
            SearchScreen.geometry("1440x900") 
            SearchScreen.title("S E A R C H ") 
            SearchScreen.resizable(False,False) 
            SearchScreen.configure(bg="white") 
            
            
            #Search Icon
            SearchClientPNG = Image.open("PNG/SearchClient.png") 
            ResizeSearchClientPNG = SearchClientPNG.resize((200,200),Image.ANTIALIAS) 
            NewPng = ImageTk.PhotoImage(ResizeSearchClientPNG) 
            PNGlabel = Label(SearchScreen,image=NewPng,bg="white") 
            PNGlabel.place(relx=0.5,rely=0.1,anchor=CENTER)  
            
            #Search label 
            Labelstyle = ttk.Style()
            Labelstyle.configure("TLabel", foreground="#1D79F0", font=("Arial", 14, "bold"))
            search_label = ttk.Label(SearchScreen, text="Search Client", style="TLabel", background="white")
            search_label.place(relx=0.5, rely=0.26, anchor="center")
            
            #Search Entry 
            Entrystyle = ttk.Style()
            Entrystyle.configure("TEntry", foreground="gray", font=("Arial", 12))
            Myentry = ttk.Entry(SearchScreen, width=35, style="TEntry",)
            Myentry.place(relx=0.5, rely=0.30, anchor="center") 
            
            #Search button  
            Sbuttonstyle = ttk.Style()
            Sbuttonstyle.configure("Modern.TButton",
                foreground="#1D79F0",
                background="#1D79F0",
                font=("Helvetica", 12, "bold"),
                padding=10)
            Mybutton = ttk.Button(SearchScreen, text="Search", style="Modern.TButton", command=lambda: SearchRecords())
            Mybutton.place(relx=0.46,rely=0.33)
            
            #table frame 
            TableFrame = Frame(SearchScreen,width=900,height=650,)  
            TableFrame.place(relx=0.22,rely=0.5) 
     
            #TreeView 
            TableStyle = ttk.Style() 
            TableStyle.configure("Treeview", 
                                 background="#D3D3D3", 
                                 foreground="black", 
                                 rowheight=25, 
                                 fieldbackground="#d3d3d3") 
            
            TableStyle.map("Treeview", 
                           background= [("selected","#347083")]
                           )
            
            #Scrollbar
            TableScroll = Scrollbar(TableFrame) 
            TableScroll.pack(side=RIGHT,fill=Y) 
            
            #Tree view
            TableTreeView = ttk.Treeview(TableFrame,yscrollcommand=TableScroll.set, selectmode="extended") 
            TableTreeView.pack() 
            TableScroll.config(command=TableTreeView.yview,) 
            
            #Tree columns
            TableTreeView["columns"] = ("First Name", "Last Name","RowID", "Password", "ID") 
            TableTreeView.column("#0",width=0, stretch=NO)  
            TableTreeView.column("First Name",anchor=W,width=140) 
            TableTreeView.column("Last Name",anchor=W,width=140) 
            TableTreeView.column("RowID",anchor=CENTER,width=100)  
            TableTreeView.column("Password",anchor=CENTER,width=140) 
            TableTreeView.column("ID",anchor=CENTER,width=300)  
            
            #Tree Headings
            TableTreeView.heading("#0", text="", anchor=W) 
            TableTreeView.heading("First Name", text="First Name",anchor=W)
            TableTreeView.heading("Last Name", text="Last Name", anchor=W)
            TableTreeView.heading("RowID", text="RowID", anchor=CENTER)
            TableTreeView.heading("Password", text="Password", anchor=CENTER)
            TableTreeView.heading("ID", text="ID", anchor=CENTER) 
            
            #Row colors
            TableTreeView.tag_configure("oddrow", background="white") 
            TableTreeView.tag_configure("evenrow", background="lightblue") 
            
            #Get info from database to Tree
            def GetClientInfoToTree():
                #ExistClient = []
                cursor.execute("SELECT rowid, * FROM client")
                global clients
                clients = cursor.fetchall() 
                global count 
                count = 0
                for i in clients: 
                    if count % 2 == 0: 
                        TableTreeView.insert(parent="",index="end", iid=count,text="",values=(i[1],i[2],i[0],i[3],i[4]), tags=("evenrow")) 
                    else: 
                        TableTreeView.insert(parent="",index="end", iid=count,text="",values=(i[1],i[2],i[0],i[3],i[4]), tags=("oddrow"))
                
                    count += 1
                """if len(clients) == 0:
                    messagebox.showwarning("ERROR", "THERE IS NO INFORMATION YET")
                else:
                    for i in clients:
                        client_info = (i[0], i[1], i[2], i[3])  
                        ExistClient.append(client_info)

                return ExistClient"""
            
            #Search by Name   
            def SearchRecords(): 
                LookRecord = Myentry.get() 
                for i in TableTreeView.get_children(): 
                    TableTreeView.delete(i) 
                cursor.execute("SELECT rowid, * FROM client WHERE Name = ?",(LookRecord,)) 
                Recordlist = cursor.fetchall()
                global count 
                count = 0
                for i in Recordlist: 
                    if count % 2 == 0: 
                        TableTreeView.insert(parent="",index="end", iid=count,text="",values=(i[1],i[2],i[0],i[3],i[4]), tags=("evenrow")) 
                    else: 
                        TableTreeView.insert(parent="",index="end", iid=count,text="",values=(i[1],i[2],i[0],i[3],i[4]), tags=("oddrow"))
                    
                    count += 1
            #back button
            BackButton = Button(
            SearchScreen,
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
            command=lambda: WhenClicked()
            ) 
            BackButton.place(x=0,y=0) 
            
            def WhenClicked(): 
                SearchScreen.withdraw()
                AdminScreen.deiconify() 
    
            GetClientInfoToTree()
            mainloop()
         
        #Change user info screen 
        def ChangeUserPage(): 
            AdminScreen.withdraw() 
            ChangeScreen = Toplevel(AdminScreen) 
            ChangeScreen.geometry("1000x500") 
            ChangeScreen.title("C H A N G E") 
            ChangeScreen.resizable(False,False) 
             
            #Table frame
            TreeFrame = Frame(ChangeScreen) 
            TreeFrame.pack(pady=10) 
    
            ChangeStyle = ttk.Style() 
            ChangeStyle.configure("Treeview", 
                                 background="#D3D3D3", 
                                 foreground="black", 
                                 rowheight=25, 
                                 fieldbackground="#d3d3d3") 
            
            ChangeStyle.map("Treeview", 
                           background= [("selected","#347083")]
                           )
            #Scrollbar
            TableScroll = Scrollbar(TreeFrame) 
            TableScroll.pack(side=RIGHT,fill=Y) 
            
            #Tree view
            TableTreeView = ttk.Treeview(TreeFrame,yscrollcommand=TableScroll.set, selectmode="extended") 
            TableTreeView.pack() 
            
            TableScroll.config(command=TableTreeView.yview,) 
            
            #Tree columns
            TableTreeView["columns"] = ("First Name", "Last Name","RowID", "Password", "ID") 
            TableTreeView.column("#0",width=0, stretch=NO)  
            TableTreeView.column("First Name",anchor=W,width=140) 
            TableTreeView.column("Last Name",anchor=W,width=140) 
            TableTreeView.column("RowID",anchor=CENTER,width=100)  
            TableTreeView.column("Password",anchor=CENTER,width=140) 
            TableTreeView.column("ID",anchor=CENTER,width=300)  
            
            #Tree headings
            TableTreeView.heading("#0", text="", anchor=W) 
            TableTreeView.heading("First Name", text="First Name",anchor=W)
            TableTreeView.heading("Last Name", text="Last Name", anchor=W)
            TableTreeView.heading("RowID", text="RowID", anchor=CENTER)
            TableTreeView.heading("Password", text="Password", anchor=CENTER)
            TableTreeView.heading("ID", text="ID", anchor=CENTER) 
            
            #Row colors
            TableTreeView.tag_configure("oddrow", background="white") 
            TableTreeView.tag_configure("evenrow", background="lightblue")  
            #Record Entry  and button
            DataFrame = LabelFrame(ChangeScreen, text="record") 
            DataFrame.pack(fill="x", expand="yes", padx=20)
            
            #First Name label
            FNLabel = Label(DataFrame, text="First Name")  
            FNLabel.grid(row=0,column=0,padx=10,pady=10)
            #Name entry
            FNEntry = Entry(DataFrame,) 
            FNEntry.grid(row=0,column=1,padx=10,pady=10)
            
            #Last Name label
            LNLabel = Label(DataFrame, text="Last Name")  
            LNLabel.grid(row=0,column=2,padx=10,pady=10)
            #Last name entry
            LNEntry = Entry(DataFrame,) 
            LNEntry.grid(row=0,column=3,padx=10,pady=10) 
            
            #Password label
            PWLabel = Label(DataFrame, text="Password")  
            PWLabel.grid(row=0,column=4,padx=10,pady=10)
            #Password entry
            PWEntry = Entry(DataFrame,) 
            PWEntry.grid(row=0,column=5,padx=10,pady=10) 
            
            #Submit button
            SubmitButton = Button(DataFrame, text="Submit",command=lambda: UpdateClientInfo()) 
            SubmitButton.grid(row=0,column=6, padx=10,pady=10) 
            
            #Select record
            def Select_record(e): 
                FNEntry.delete(0, END) 
                LNEntry.delete(0, END) 
                PWEntry.delete(0, END) 
                
                SelectedRow = TableTreeView.focus() 
                values = TableTreeView.item(SelectedRow, "values")
                
                FNEntry.insert(0, values[0]) 
                LNEntry.insert(0, values[1]) 
                PWEntry.insert(0, values[3])
            TableTreeView.bind("<ButtonRelease-1>", Select_record)
            
            #For update selected client infos
            def UpdateClientInfo(): 
                DatabseConnection()
                selected = TableTreeView.focus()
                ItemValues = TableTreeView.item(selected, "values")
                
                
                # Update record
                TableTreeView.item(selected, text="", values=(FNEntry.get(), LNEntry.get(),ItemValues[2],PWEntry.get(),ItemValues[4]))
                
                cursor.execute("""UPDATE client SET
                    Name = :first,
                    Surname = :last, 
                    Password = :pasw
                    

                    WHERE oid = :oid""",
                    {
                        'first': FNEntry.get(),
                        'last': LNEntry.get(), 
                        "pasw": PWEntry.get(),  
                        "oid": ItemValues[2],
                           
                    })
                
                # Commit changes
                con.commit()

                # Clear entry boxes
                FNEntry.delete(0, END)
                LNEntry.delete(0, END)
                PWEntry.delete(0, END)
                
 
                
            def GetClientInfoToTree():
                ExistClient = []
                cursor.execute("SELECT rowid, * FROM client")
                global clients
                clients = cursor.fetchall() 
                global count 
                count = 0
                for i in clients: 
                    if count % 2 == 0: 
                        TableTreeView.insert(parent="",index="end", iid=count,text="",values=(i[1],i[2],i[0],i[3],i[4]), tags=("evenrow")) 
                    else: 
                        TableTreeView.insert(parent="",index="end", iid=count,text="",values=(i[1],i[2],i[0],i[3],i[4]), tags=("oddrow"))
                
                    count += 1

                if len(clients) == 0:
                    messagebox.showwarning("ERROR", "THERE IS NO INFORMATION YET")
                else:
                    for i in clients:
                        client_info = (i[0], i[1], i[2], i[3])  
                        ExistClient.append(client_info)

                return ExistClient
            BackButton = Button(
            ChangeScreen,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=5,
            height=1,
            border=0,
            cursor="hand2", 
            text="Back", 
            font=("Oswald", 16,"bold"), 
            command=lambda: WhenClicked()
            ) 
            BackButton.place(x=0,y=0) 
            
            def WhenClicked(): 
                ChangeScreen.withdraw()
                AdminScreen.deiconify()
            GetClientInfoToTree()
            mainloop() 
        
        #Look user logs
        def UsersLogs(): 
            AdminScreen.withdraw() 
            DataScreen = Toplevel(AdminScreen) 
            DataScreen.geometry("1440x900") 
            DataScreen.title("L O G S") 
            DataScreen.resizable(False,False) 
            #search by name look for logs
            def SearchUser():
                user = search_entry.get()

                logs = UserLog(user)
                logs_tree.delete(*logs_tree.get_children())  

                for i, log in enumerate(logs, start=1):
                    if i % 2 == 0:
                        logs_tree.insert("", "end", text=str(i), values=(log,), tags=("even",))
                    else:
                        logs_tree.insert("", "end", text=str(i), values=(log,), tags=("odd",))


            

            search_label = Label(DataScreen, text="User Name:")
            search_label.pack()

            search_entry = Entry(DataScreen)
            search_entry.pack()

            search_butonu = Button(DataScreen, text="Search", command=lambda: SearchUser())
            search_butonu.pack()

            logs_tree = ttk.Treeview(DataScreen)
            logs_tree["columns"] = ("Log record")

            logs_tree.column("#0", width=50,  stretch=YES)
            logs_tree.column("Log", width=300,  stretch=YES)

            logs_tree.heading("#0", text="No")
            logs_tree.heading("Log", text="Log ") 
            
            logs_tree.tag_configure("even", background="lightblue")
            logs_tree.tag_configure("odd", background="white")

            logs_tree.pack() 
            scrollbar = ttk.Scrollbar(DataScreen, orient="vertical", command=logs_tree.yview)
            logs_tree.configure(yscrollcommand=scrollbar.set)

            scrollbar.pack(side="right", fill="y")
            logs_tree.pack(fill="both", expand=True)


        mainloop() 
        
    #Sign up screen
    def SignUpP(): 
        screen.withdraw() 
        SignUp = Toplevel(screen) 
        SignUp.geometry("1440x900")  
        SignUp.title("S I G N  U P")   
        SignUp.resizable(False ,False) 
        SignUp.configure(bg="#fff")
        #Back Button 
        BackButton = Button(
            SignUp,
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
            command=lambda: WhenClicked()
            ) 
        BackButton.place(x=0,y=0)
            
        def WhenClicked(): 
            SignUp.withdraw()
            screen.deiconify()
            
            
        #Sign up Icon 
        img= PhotoImage(file="PNG/add-friend.png") 
        ImgLabel= Label(SignUp, image=img,border=0,bg="white") 
        ImgLabel.place(x=50,y=90) 
        
        #Sign frame 
        SignFrame = Frame(SignUp, width=350,height=390,bg="#fff") 
        SignFrame.place(x=900,y=100)
        
        #Heading Label 
        Head = Label(SignUp,text="S I G N  U P",fg="#F0BA1D",bg="#fff",font=("Microsoft YaHei UI Light",24,"bold") ) 
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
            if PassW.get() == COnfirm.get() and PassW.get() != "Password" and COnfirm.get() != "Password": 
                password = PassW.get() 
                SetValue(username,surname,password,str(uuid.uuid4()),"No action")
                SignUp.destroy()
                screen.deiconify()
            elif PassW.get() != COnfirm.get(): 
                messagebox.showwarning("E R R O R","Password doesn't match ! ! ")  
            elif PassW.get() == "Password" or user.get()=="Name" or Sur.get() == "Surname" or COnfirm.get() == "Password": 
                messagebox.showwarning("E R R O R", "Fill all the blanks")
            else: 
                pass
        
        
        
        
        mainloop()
    
    
    #Normal View Page 
    def NormalViewPage():  
        NormalPageView = Tk() 
        NormalPageView.geometry("1440x900") 
        NormalPageView.title("N O R M A L  V I E W")  
        NormalPageView.configure(bg="white") 
        
        #NormalView Page frames
        AccDet = Frame(NormalPageView,width=400,height=400,bg="white",)  
        ShowUSerMoney = Frame(NormalPageView,width=400,height=400,bg="white",) 
        
        
        #Grid layout
        AccDet.grid(row=0,column=0,padx=160,pady=20) 
        ShowUSerMoney.grid(row=0,column=1,padx=160,pady=20) 
        
        
        #Account details  section
        AccPng = Image.open("PNG/profile.png") 
        ResizeAccPng = AccPng.resize((250,250), Image.ANTIALIAS) 
        NewAccPng = ImageTk.PhotoImage(ResizeAccPng) 
        AccPngLabel = Label(AccDet,image=NewAccPng,bg="white") 
        AccPngLabel.place(relx=0.5,rely=0.5,anchor=CENTER,) 
        
        #account detail button  
        AccButton = Button(
            AccDet,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=13,
            height=2,
            border=0,
            cursor="hand2", 
            text="Account Details", 
            font=("Oswald", 16,"bold"), 
            command= lambda: AccDetPage() 
            
            ) 
        AccButton.place(relx=0.5,rely=0.92,anchor=CENTER) 
        
        def AccDetPage(): 
            NormalPageView.withdraw()  
            AccScreen = Toplevel(NormalPageView)
            AccScreen.geometry("1440x900") 
            AccScreen.title("A C C O U N T  V I E W")  
            AccScreen.configure(bg="white") 
            logger("account information viewed",username)
            #Back button
            BackButton = Button(
            AccScreen,
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
            command=lambda: WhenClicked()
            ) 
            BackButton.place(x=0,y=0)
            
            def WhenClicked(): 
                AccScreen.withdraw()
                NormalPageView.deiconify() 
            # Kullanıcı hesap bilgileri
            account_frame = Frame(  
                AccScreen,
                bg="#F0F0F0",
                width=1340,
                height=800,
                padx=20,
                pady=20
            )
            account_frame.place(x=470, y=200)

            account_label = Label(
                account_frame,
                text="Account Infos",
                font=("Arial", 20, "bold"),
                bg="#F0F0F0",
                fg="#333333"
            )
            account_label.pack(pady=10)

            username_label = Label(
                account_frame,
                text="Username:",
                font=("Arial", 16),
                bg="#F0F0F0",
                fg="#333333"
            )
            username_label.pack(anchor=W)

            username_value = Label(
                account_frame,
                text=str(username),
                font=("Arial", 16),
                bg="#F0F0F0",
                fg="#666666"
            )
            username_value.pack(anchor=W)

            account_number_label = Label(
                account_frame,
                text="Account ID:",
                font=("Arial", 16),
                bg="#F0F0F0",
                fg="#333333"
            )
            account_number_label.pack(anchor=W)

            account_number_value = Label(
                account_frame,
                text=str(cl[0][3]),
                font=("Arial", 16),
                bg="#F0F0F0",
                fg="#666666"
            )
            account_number_value.pack(anchor=W)

            AccScreen.mainloop()   
            
        #Money section 
        MoneyPng = Image.open("PNG/money-bag.png") 
        ResizeMoneyPng = MoneyPng.resize((250,250),Image.ANTIALIAS) 
        NewMoneyPng = ImageTk.PhotoImage(ResizeMoneyPng) 
        MoneyLabel = Label(ShowUSerMoney,image=NewMoneyPng,bg="white") 
        MoneyLabel.place(relx=0.5,rely=0.5,anchor=CENTER) 
        
        #Money button 
        MoneyButton = Button(
            ShowUSerMoney,
            bg="#F0BA1D",
            fg="white",
            activebackground="white",
            activeforeground="#F0BA1D",
            width=13,
            height=2,
            border=0,
            cursor="hand2", 
            text="Money", 
            font=("Oswald", 16,"bold"), 
            command=lambda: MoneyPage() 
             
            ) 
        MoneyButton.place(relx=0.5,rely=0.92,anchor=CENTER) 
        def MoneyPage(): 
            NormalPageView.withdraw()  
            MScreen = Toplevel(NormalPageView)
            MScreen.geometry("1440x900") 
            MScreen.title("M O N E Y  V I E W")  
            MScreen.configure(bg="white") 
            logger("the money in the account has been viewed",username,)
            BackButton = Button(
            MScreen,
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
            command=lambda: WhenClicked()
            ) 
            BackButton.place(x=0,y=0)
            
            def WhenClicked(): 
                MScreen.withdraw()
                NormalPageView.deiconify()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        NormalPageView.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    #Icon label
    BankIcon = ImageTk.PhotoImage(Image.open("PNG/ZGRBank.png")) 
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