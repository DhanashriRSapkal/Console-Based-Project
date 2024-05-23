import pymysql as p
def getconnection():
    return p.connect(host='localhost',user='root',password='',database='mobiledeta')

def insert_data(t):
    con=getconnection()
    cur=con.cursor()
    sql = "insert into mobile values (%s, %s, %s)"
    cur.execute(sql,t)
    con.commit()
    print("data inserted")
    con.close()
    
def display_data():
    con = getconnection()
    cur = con.cursor()
    cur.execute("select * from mobile")
    elist = cur.fetchall()
    con.close()
    return elist

def delete_data(rn):
    con = getconnection()
    cur = con.cursor()
    cur.execute("delete from mobile where ID = %s",(rn,))
    con.commit()
    print("data deleted")
    con.close()

def update_data(t):
    con = getconnection()
    cur = con.cursor()
    cur.execute("update mobile set brand=%s , features=%s where ID = %s", (t))
    con.commit()
    print("data updated")
    con.close()
    
    
