import sqlite3 
import time  
import MyDb 


#My Client
class Client(): 
    
    def __init__(self,name,surname,clientID, password): 
        
        self.name = name 
        self.surname = surname
        self.clientID = clientID
        self.password = password 
        
    def __iter__(self):
        
        yield self.name
        yield self.surname
        yield self.password 
        yield self.clientID
    
    def __str__(self): 
        return "Client name: {}\nClient surname: {}\nClient ID: {}\nClient Password: {}\n".format(self.name,self.surname,self.clientID,self.password)   
    
    
    