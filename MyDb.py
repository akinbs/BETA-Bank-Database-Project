import sqlite3 
from tkinter import messagebox
from tkinter import * 




con = sqlite3.connect("Clients.db")
cursor = con.cursor()

#to connect to DB
def DatabseConnection():   
    cursor.execute("CREATE TABLE IF NOT EXISTS client(Name TEXT ,Surname TEXT ,Password TEXT,ClientID TEXT,UserLog TEXT)")  
    con.commit() 
    
#set value of client to first time   
def SetValue(name, surname,Password,UserID,Userlog):  
     cursor.execute("INSERT INTO client Values (?,?,?,?,?)", (name, surname,Password,UserID,Userlog))  
     con.commit() 
     
            
#logger funct        
def logger(event,client): 
    DatabseConnection() 
    cursor.execute("SELECT UserLog FROM client WHERE Name = ?", (client,))
    Nlog = cursor.fetchone()

    if Nlog is None:
        cursor.execute("INSERT INTO client (Name, UserLog) VALUES (?, ?)", (client, event))
    else:
        old_log = Nlog[0]
        new_log = old_log + "\n" + event
        cursor.execute("UPDATE client SET UserLog = ? WHERE Name = ?", (new_log, client))

    con.commit()

#Log record func       
def UserLog(client):
    DatabseConnection()
    cursor.execute("SELECT UserLog FROM client WHERE Name = ?", (client,))
    log = cursor.fetchone()
    

    if log is None:
        return []
    else:
        Mlog = log[0]
        hareketler = Mlog.split("\n")
        return hareketler   
        
        
#Search by client name
def SeacrhClient(NameValue): 
    cursor.execute("SELECT * FROM client WHERE Name = ?",(NameValue,)) 
    Mylist = cursor.fetchall()
    return Mylist 

#update existing client infos

    
            
#delete any info 
def DeleteValue(value, Dvalue): 
    cursor.execute("DELETE FROM client where "+{value}+" = ? ", (Dvalue)) 
    con.commit() 
    print({value}+ " value has been deleted" )
        
#disconnect    
def Disconnect(): 
    con.close()
     
    
     
    
        
 
        
            
        
         
         
         
     
        
    
    
    




