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

#'''
cur.execute("""
            CREATE TABLE pbl_22a.user_table
            (id MEDIUMINT NOT NULL AUTO_INCREMENT,
            name VARCHAR(30),
            sex CHAR(1),
            height int(1),
            weight int(1),
            activity_level int(1),
            admin int(1),
            PRIMARY KEY(id))
            """)

'''

cur.execute("""
            CREATE TABLE pbl_22a.meal_table
            (id MEDIUMINT NOT NULL AUTO_INCREMENT,
            meal_name VARCHAR(30),
            date DATE,
            PRIMARY KEY(id))
            """)



cur.execute("""
            CREATE TABLE pbl_22a.nutrious_table
            (id MEDIUMINT NOT NULL AUTO_INCREMENT,
            food_name VARCHAR(30),
            cal int(1),
            sugar int(1),
            protein int(1),
            lipid int(1),
            vitamine_c int(1),
            fe int(1),
            PRIMARY KEY(id))
            """)

'''

con.commit()

con.close()