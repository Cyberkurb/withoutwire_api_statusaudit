import mysql.connector

#standard website db connection
def connectrs():
    return mysql.connector.connect(
            host="MySQL Server Address",
            user="User name",
            password='Password',
            database="database_name"
            )
            
def wowstatusupdates(ordernumber, wowstatus, warehouse):
    conn = connectrs()
    cursor = conn.cursor(dictionary=True,buffered=True)

    record_sets = {
        'ordernumber': ordernumber,
        'wowstatus': wowstatus,
        'warehouse': warehouse 
    }
    
    sql_i = ("INSERT INTO wow_or_status SET "
            "ordernumber = %(ordernumber)s, "
            "date_updated = now(), "
            "wow_status = RTRIM(%(wowstatus)s), "
            "warehouse = RTRIM(%(warehouse)s) "
            "ON DUPLICATE KEY UPDATE "
            "date_updated = now(), "
            "wow_status = RTRIM(%(wowstatus)s), "
            "warehouse = RTRIM(%(warehouse)s);")
            
    #this script doesn't take into account any errors and uses the order number as the Key, so that it is just quickly updating the request.
    cursor.execute(sql_i, record_sets)
    conn.commit()

    cursor.close()
    conn.close()
    return "add_update"
