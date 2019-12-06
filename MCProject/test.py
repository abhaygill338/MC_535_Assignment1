import psycopg2

postgres_insert_query = ""
def create_tables():
    try:
        connection = psycopg2.connect(user = "abhay",
				                          password = "9927001238",
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
    connection = psycopg2.connect(user="abhay",
                                  password = "9927001238",
				                          host="127.0.0.1",
                                  port="5432",
                                  database="items_tracker")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO items_track (ITEMDATE,ITEMSLIST) VALUES (%s,%s)"""
    record_to_insert = (date ,data_item)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount

def missing_items_present(list_items_frequent,latest_data):
  flag = False
  list_temp = []
  for i in range(0,len(list_items_frequent)):
    flag = False
    for j in range(0,len(latest_data)):
      if(list_items_frequent[i] == latest_data[j]):
        flag = True
        break
    if(flag == False):
      list_temp.append(list_items_frequent[i])

  return list_temp

def add_one_more_column():
    connection = psycopg2.connect(user="abhay",
                                  password = "9927001238",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="items_tracker")
    cursor = connection.cursor()
    cursor.execute('ALTER TABLE %s ADD COLUMN %s text' % ('items_track', 'missing_data_items'))
    connection.commit()
    count = cursor.rowcount

def adding_missing_element(list_items_frequent,days):
    connection = psycopg2.connect(user="abhay",
                                  password = "9927001238",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="items_tracker")
    cursor = connection.cursor()
    sql_select_query = """SELECT * from items_track"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    sql_select_query_2 = """SELECT * from items_track offset %s limit %s"""
    parameter = (max(0,(cursor.rowcount)-days),cursor.rowcount-max(0,(cursor.rowcount)-days))
    cursor.execute(sql_select_query_2 , parameter)
    record = cursor.fetchall()
    for row in record:
      latest_data = row[1].split(",")
      if(len(latest_data) == 0):
        data_item = ','.join(list_items_frequent)
        postgres_insert_query = """ UPDATE items_track SET missing_data_items = %s WHERE ITEMDATE = %s"""
        record_to_insert = (data_item,row[0])
        cursor.execute(postgres_insert_query, record_to_insert)
      if(len(latest_data) > 0):
        list_missing_ones = missing_items_present(list_items_frequent,latest_data)
        data_item = ','.join(list_missing_ones)
        postgres_insert_query = """ UPDATE items_track SET missing_data_items = %s WHERE ITEMDATE = %s"""
        record_to_insert = (data_item,row[0])
        cursor.execute(postgres_insert_query, record_to_insert)
    print("Table updated successfully")
    connection.commit()    

def data_based_on_cycle(days):
    connection = psycopg2.connect(user="abhay",
				                          password = "9927001238",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="items_tracker")
    cursor = connection.cursor()
    sql_select_query = """SELECT * from items_track"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    if(cursor.rowcount < 30):
      print("Number of rows required are less , there must be presence of more than 30 rows.")
    sql_select_query_2 = """SELECT * from items_track offset %s limit %s"""
    parameter = ((cursor.rowcount) - days ,days)
    cursor.execute(sql_select_query_2 , parameter)
    record = cursor.fetchall()
    list=[]
    for row in record:
      #print("Id = ", row[0])
      list.append(row[1])

    return list
