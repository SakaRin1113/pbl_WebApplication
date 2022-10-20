import MySQLdb


con = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="laugh_0406",
    db="pbl_22a",
    use_unicode=True,
    charset="utf8"
)
cur = con.cursor()

cur.execute("""
            INSERT INTO user_table
            (name,sex,height,weight,activity_level,admin)
            VALUE('John','M',172,53,2,3)
            """)

con.commit()

con.close()