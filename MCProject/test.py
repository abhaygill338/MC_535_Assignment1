import psycopg2

def create_tables():
    try:
        connection = psycopg2.connect(user = "postgres",
				  password = "shubham",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "items_tracker")
        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE items_track
          (ITEMDATE TEXT PRIMARY KEY     NOT NULL,
          ITEMSLIST           TEXT    NOT NULL); '''

        cursor.execute(create_table_query)
        connection.commit()
        print("Table created successfully in PostgreSQL ")

    except (Exception, psycopg2.DatabaseError) as error :
        print ("PostgreSQL table exists:", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            #print("PostgreSQL connection is closed") 


def insert_item(date,data_item):
    connection = psycopg2.connect(user="postgres",
                                  password = "shubham",
				  host="127.0.0.1",
                                  port="5432",
                                  database="items_tracker")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO items_track (ITEMDATE,ITEMSLIST) VALUES (%s,%s)"""
    record_to_insert = (date ,data_item)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount

def data_based_on_cycle(days):
    connection = psycopg2.connect(user="postgres",
				  password = "shubham",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="items_tracker")
    cursor = connection.cursor()
    sql_select_query = """SELECT * from items_track"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    sql_select_query_2 = """SELECT * from items_track offset %s limit %s"""
    parameter = ((cursor.rowcount) - days ,days)
    cursor.execute(sql_select_query_2 , parameter)
    record = cursor.fetchall()
    #print(record)
    list=[]
    for row in record:
      #print("Id = ", row[0])
      list.append(row[1])

    return list
