import psycopg2
from configparser import ConfigParser
import os
import sys

## global

path = os.getcwd()

## general functions
def print_state(state):
    for msg in state:
        print(msg)

def connect(config):
    try:
        # Connect to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            #print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def load_config(filename='file', section='postgresql'):
    if filename == 'file':
        raise Exception('No database init file was added')
    parser = ConfigParser()
    parser.read(filename)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')
    return config

def list_all_items(conn, table_name):
    if table_name in ['employee', 'topic_employee', 'topic', 'project', 'booking_text']:
        try:
            cursor = conn.cursor()
            sql_select = f'SELECT * FROM {table_name}'
            cursor.execute(sql_select)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except psycopg2.errors.InFailedSqlTransaction as failed_transaction:
            return (f'Error: Last transacation was invalid', f'Details: {failed_transaction}')
    else:
        return (f'{table_name} is not in the database',)

## project table base functions

def add_new_project(conn, project_name: str):
    try:
        cursor = conn.cursor()
        sql_insert = 'INSERT INTO project (id) VALUES (%s)'
        cursor.execute(sql_insert, (project_name,))
        conn.commit()
        cursor.close()
        return ('New project is added',)
    except psycopg2.errors.UniqueViolation as unique_error:
        conn.rollback()
        return (f"Error: ID {project_name} is already in the project table", f"Details: {unique_error}")
    except psycopg2.errors.StringDataRightTruncation as truncation_error:
        conn.rollback()
        return (f"Error: ID {project_name} is too long", f"Details: {truncation_error}")
    except psycopg2.errors.CheckViolation as short_name_error:
        conn.rollback()
        return (f"Error: ID {project_name} is shorter than 3 characters", f"Details: {short_name_error}") 

def remove_project(conn, project_name):
    try: 
        cursor = conn.cursor()
        sql_find_item = 'SELECT id FROM project WHERE id = (%s)'
        cursor.execute(sql_find_item, (project_name,))
        row = cursor.fetchall()

        if len(row) > 0:
            sql_delete = 'DELETE FROM project WHERE id = (%s)'
            cursor.execute(sql_delete, (project_name,))
            conn.commit()
            state_msg = f'{project_name} project is removed'
        else:
            state_msg = f'{project_name} project is not in the project table'
        cursor.close()
        return (state_msg,)
    except psycopg2.errors.UndefinedFunction as undefined_error:
        conn.rollback()
        return (f'Error: ID {project_name} is not a string', f'Details: {undefined_error}')

## booking_text table base functions

def add_new_booking_text(conn, booking_text: str):
    try:
        cursor = conn.cursor()
        sql_insert = 'INSERT INTO booking_text (id) VALUES (%s)'
        cursor.execute(sql_insert, (booking_text,))
        conn.commit()
        cursor.close()
        return ('New booking text is added',)
    except psycopg2.errors.UniqueViolation as unique_error:
        conn.rollback()
        return (f"Error: ID {booking_text} is already in the booking_text table", f"Details: {unique_error}")
    except psycopg2.errors.StringDataRightTruncation as truncation_error:
        conn.rollback()
        return (f"Error: ID {booking_text} is too long", f"Details: {truncation_error}")
    except psycopg2.errors.CheckViolation as short_name_error:
        conn.rollback()
        return (f"Error: ID {booking_text} is shorter than 3 characters", f"Details: {short_name_error}") 

def remove_booking_text(conn, booking_text):
    try: 
        cursor = conn.cursor()
        sql_find_item = 'SELECT id FROM booking_text WHERE id = (%s)'
        cursor.execute(sql_find_item, (booking_text,))
        row = cursor.fetchall()

        if len(row) > 0:
            sql_delete = 'DELETE FROM booking_text WHERE id = (%s)'
            cursor.execute(sql_delete, (booking_text,))
            conn.commit()
            state_msg = f'{booking_text} booking_text is removed'
        else:
            state_msg = f'{booking_text} booking_text is not in the project table'
        cursor.close()
        return (state_msg,)
    except psycopg2.errors.UndefinedFunction as undefined_error:
        conn.rollback()
        return (f'Error: ID {booking_text} is not a string', f'Details: {undefined_error}')
    
## employee table base functions

def add_new_employee(conn, employee: str):
    try:
        cursor = conn.cursor()
        sql_insert = 'INSERT INTO employee (id) VALUES (%s)'
        cursor.execute(sql_insert, (employee,))
        conn.commit()
        cursor.close()
        return ('New employee is added',)
    except psycopg2.errors.UniqueViolation as unique_error:
        conn.rollback()
        return (f"Error: ID {employee} is already in the employee table", f"Details: {unique_error}")
    except psycopg2.errors.StringDataRightTruncation as truncation_error:
        conn.rollback()
        return (f"Error: ID {employee} is too long", f"Details: {truncation_error}")
    except psycopg2.errors.CheckViolation as short_name_error:
        conn.rollback()
        return (f"Error: ID {employee} is shorter than 3 characters", f"Details: {short_name_error}") 

def remove_employee(conn, employee):
    try: 
        cursor = conn.cursor()
        sql_find_item = 'SELECT id FROM employee WHERE id = (%s)'
        cursor.execute(sql_find_item, (employee,))
        row = cursor.fetchall()

        if len(row) > 0:
            sql_delete = 'DELETE FROM employee WHERE id = (%s)'
            cursor.execute(sql_delete, (employee,))
            conn.commit()
            state_msg = f'{employee} employee is removed'
        else:
            state_msg = f'{employee} employee is not in the project table'
        cursor.close()
        return (state_msg,)
    except psycopg2.errors.UndefinedFunction as undefined_error:
        conn.rollback()
        return (f'Error: ID {employee} is not a string', f'Details: {undefined_error}')

## test functions

if __name__ == '__main__':
    config = load_config(filename=path+r'\app\database.ini')
    conn = connect(config)
    employee = '#gng'
    state = remove_employee(conn, employee)
    print_state(state)
    table_name = 'employee'
    projects = list_all_items(conn, table_name)
    for project in projects:
        print(project)