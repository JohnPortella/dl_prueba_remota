import sqlite3

class Database:
    
    def __init__(self, name=None):
        
        self.conn = None
        self.cursor = None

        if name:
            self.open(name)
    
    def open(self,name):
        
        try:
            self.conn = sqlite3.connect(name)
            self.conn.row_factory = sqlite3.Row
            self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            print("Error connecting to database!")
    
    def close(self):
        
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def query(self,sql, is_select = False):
        self.cursor.execute(sql)               

        if is_select:
            values = self.cursor.fetchall() 
            list_accumulator = []            
            for item in values:                
                list_accumulator.append({k: item[k] for k in item.keys()})
            return list_accumulator
        





