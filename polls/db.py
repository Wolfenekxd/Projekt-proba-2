import psycopg2

def last_guestions():
  
    conn = psycopg2.connect(dbname="votingdb", user="myuser", password="mypass")
    cursor = conn.cursor()
    cursor.execute("SELECT Poll_question FROM public.polls_polls")
    questions = cursor.fetchall()

    return questions

def last_id(table_name):
    table = str(table_name)
    conn = psycopg2.connect(dbname="votingdb", user="myuser", password="mypass")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM" + table + "order by desc")
    last_id = cursor.fetchone()
    last_id = int(last_id[0])
    return last_id



    