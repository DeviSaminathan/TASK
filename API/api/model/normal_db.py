from model import DB_connect
import pymysql
class Master_db(DB_connect):

    def __init__(self):
        super().__init__()
    
    def called(self):
        self.db = pymysql.connect(host=self.host,password=self.password,database=self.database,user=self.user)
        self.cursor = self.db.cursor()
    
    def longdur(self):
    
        db = pymysql.connect(host="127.0.0.1",port=3308,user="root",password="devi",database="onito")
        cursor = db.cursor()
        getdata= "select * from movies ORDER BY runtimeMinutes DESC limit 10 ;"
        cursor.execute(getdata)
        data = cursor.fetchall()
        db.commit()
        db.close()
        return data

    
    def insertmovie(self,cons,title,primary,time,gen):
        try :
            db = pymysql.connect(host="127.0.0.1",port=3308,user="root",password="devi",database="onito")
            
            cursor = db.cursor()
            
            movieinsert = "insert into movies(tconst,titleType,primaryTitle,runtimeMinutes,genres) VALUES (%s,%s,%s,%s,%s)"
            
            cursor.execute(movieinsert,(cons,title,primary,time,gen))
            
            db.commit()
            db.close()
            return 1
        except:
            return 0

    def avgmov(self):
    
        db = pymysql.connect(host="127.0.0.1",port=3308,user="root",password="devi",database="onito")
        cursor = db.cursor()
        getdata= "select * from ratings where averageRating>6.0 order by averageRating DESC;"
        cursor.execute(getdata)
        data = cursor.fetchall()
        db.commit()
        db.close()
        return data    

    def movieavg(self,const):
    
        db = pymysql.connect(host="127.0.0.1",port=3308,user="root",password="devi",database="onito")
        cursor = db.cursor()
        getdata= "select * from movies where tconst= %s;"
        cursor.execute(getdata,(const))
        data = cursor.fetchone()
        db.commit()
        db.close()
        return data
       
    
        