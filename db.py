import sqlite3

class Database:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            email text,
            gender text,
            contact text,
            address text
        );
        """
        self.cur.execute(sql)
        self.con.commit()
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?)",(name,age,doj,email,gender,contact,address))
        self.con.commit()
    # fetch all data from db
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows=self.cur.fetchall()
        # print(rows)
        return rows
    #delete a record in db
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()
    # update record in db
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employees set name=?,age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
                         (name, age, doj, email, gender, contact, address,id))
        self.con.commit()


o =Database("Employee.db")
o.insert("sam vishal","22","13-10-2024","ram@gmail.com","Male","4879239002","gandhi road")
o.remove(3)
o.fetch()
o.update("2","sam jameel","35","12-6-2012","samj@gmail.com","male","5788805490","sheynoy nagar")
J=Database("Employee.db")
J.insert("Joe","27","23-4-2015","joethe@gmail.com","female","568899043","anna nagar")
k=Database("Employee.db")
k.insert("maria","35","23-4-2016","queenmaria@gmail.com","female","5688890093","anna nagar")
l=Database("Employee.db")
l.insert("Rory","21","23-4-2019","roryg@gmail.com","female","568874837","anna nagar")
m=Database("Employee.db")
m.insert("Megan","25","23-4-2023","meganfox@gmail.com","female","5688923434","anna nagar")

