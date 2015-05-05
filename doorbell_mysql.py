try:
    import MySQLdb as db 
except ImportError:
    print "Requires python_mysqldb"
        
import sys

def save(cfg,img):
	print "Writing to mysql..."
	con=0
	try:
	    con = db.connect(cfg["mysql_server"], cfg["mysql_user"], cfg["mysql_password"], cfg["mysql_database"])
	        
	    sql="INSERT INTO bells (doorbellid,imgpath,message) VALUES (" + cfg["mysql_doorbell_id"] + ",'" + img + "','" + cfg["message"] + "');"
	    #print "SQL: " + sql
	    cur=con.cursor()
	    cur.execute(sql)
	    result = con.use_result()
	        
	except db.Error as e:
	    print "Error %d: %s" % (e.args[0], e.args[1])

	finally:
	    
	    if con:
	        con.close()