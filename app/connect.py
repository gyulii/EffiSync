import psycopg2
from config import load_config
import os

def connect(config):
    try:
        # Connect to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def add_new_team_leader(conn):
    try:
        cursor = conn.cursor()
        new_id = 60
        sql_insert = f"""
                    INSERT INTO team_leader (id)
                    VALUES ({new_id})
                    """
        cursor.execute(sql_insert)
        conn.commit()
        cursor.close()
        print('new leader added')
    except psycopg2.errors.UniqueViolation as unique_error:
        print(f"Error: ID {new_id} is already in the team_leader table")
        print(f"Details: {unique_error}")

def remove_team_leader(conn):
    cursor = conn.cursor()
    id = 50
    sql_delete = """
                DELETE
                FROM team_leader 
                WHERE id = %s
                """
    cursor.execute(sql_delete, (id,))
    conn.commit()
    cursor.close()
    print(f'team leader removed with {id}')
    return

def list_all_team_leaders(conn):
    cursor = conn.cursor()
    sql_select = """
                    SELECT *
                    FROM team_leader    
                    """    
    cursor.execute(sql_select)
    rows = cursor.fetchall()
    cursor.close()
    return rows

if __name__ == '__main__':
    path = os.getcwd()
    config = load_config(filename=path+r'\app\database.ini')
    conn = connect(config)
    #add_new_team_leader(conn)
    #remove_team_leader(conn)
    team_leaders = list_all_team_leaders(conn)
    print(type(team_leaders), type(team_leaders[0]))
    for team_leader in team_leaders:
        print(team_leader[0])