import sqlite3 
from tkinter import messagebox
from tkinter import * 
import Client_Class



con = sqlite3.connect("Clients.db")
cursor = con.cursor()

#to connect to DB
def DatabseConnection():   
    cursor.execute("CREATE TABLE IF NOT EXISTS client(Name TEXT ,Surname TEXT ,Password TEXT,ClientID TEXT)") 
    con.commit() 
    
#set value of client to first time   
def SetValue(name, surname,Password,clientID):  
     cursor.execute("INSERT INTO client Values (?,?,?,?)", (name, surname,Password ,clientID))  
     con.commit() 
     
            
            
#view info about client        
           
def GetClientInfo():
    ExistClient = []
    cursor.execute("SELECT * FROM client")
    clients = cursor.fetchall()

    if len(clients) == 0:
        messagebox.showwarning("ERROR", "THERE IS NO INFORMATION YET")
    else:
        for i in clients:
            client_info = (i[0], i[1], i[2], i[3])  # Müşteri bilgilerini doğrudan ekleyin
            ExistClient.append(client_info)

    return ExistClient
            
            
         
       
        
        
#Search by client name
def SeacrhClient(NameValue): 
    cursor.execute("SELECT * FROM client WHERE Name = ?",(NameValue,)) 
    Mylist = cursor.fetchall() 
    return Mylist 

#update existing client infos
def UpdateValues(ValueList, ChangeList):
    cursor.execute("SELECT * FROM client") 
    MyList = cursor.fetchall()
    while len(ChangeList)> 0:
        for i in ValueList: 
            cursor.execute("UPDATE client set "+{ValueList[i]}+" = ? WHERE "+{ValueList[i]}+ " = ?", (ChangeList[i],ValueList[i]))  
            ChangeList.pop(i)
            con.commit() 
            
#delete any info 
def DeleteValue(value, Dvalue): 
    cursor.execute("DELETE FROM client where "+{value}+" = ? ", (Dvalue)) 
    con.commit() 
    print({value}+ " value has been deleted" )
        
#disconnect    
def Disconnect(): 
    con.close()
     
    
     
    
        
 
        
            
        
         
         
         
     
        
    
    
    




