import MySQLdb

def connect_db():
    con = MySQLdb.connect(host='localhost', database='bdc', user='root', password='')
    return con

def insert_record(con, rgroup_label, dage, dweight, dgroup_label, result):
    cr = con.cursor()
    cmd = """
    INSERT INTO bloodCheck (recipient, rage, rweight, donator, result)
    VALUES (%s, %s, %s, %s, %s)
    """
    args = (rgroup_label, dage, dweight, dgroup_label, result)
    cr.execute(cmd, args)
    con.commit()
