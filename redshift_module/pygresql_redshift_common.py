import pg


def get_connection(host,port,db_name,user,password_for_user):
    rs_conn_string = "host=%s port=%s dbname=%s user=%s password=%s" % (
        host, port, db_name, user, password_for_user)

    rs_conn = pg.connect(dbname=rs_conn_string)
    return rs_conn


def query(con,query):
    res = con.query(query)
    return res
