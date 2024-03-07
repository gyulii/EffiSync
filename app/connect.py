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

def load_config(filename, section='postgresql'):
    if not filename:
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
            records = cursor.fetchall()
            cursor.close()
            return records
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
    
def update_project(conn, old_project_name: str, new_project_name: str):
    try:
        cursor = conn.cursor()
        sql_update = 'UPDATE project SET id = %s WHERE  id = %s'
        cursor.execute(sql_update, (new_project_name, old_project_name))
        conn.commit()
        cursor.close()
        return ('project table is updated',)
    except psycopg2.errors.UniqueViolation as unique_error:
        conn.rollback()
        return (f"Error: ID {new_project_name} is already in the project table", f"Details: {unique_error}")
    except psycopg2.errors.StringDataRightTruncation as truncation_error:
        conn.rollback()
        return (f"Error: ID {new_project_name} is too long", f"Details: {truncation_error}")
    except psycopg2.errors.CheckViolation as short_name_error:
        conn.rollback()
        return (f"Error: ID {new_project_name} is shorter than 3 characters", f"Details: {short_name_error}")   

def remove_project(conn, project_name):
    try: 
        cursor = conn.cursor()
        sql_find_item = 'SELECT id FROM project WHERE id = (%s)'
        cursor.execute(sql_find_item, (project_name,))
        record = cursor.fetchall()

        if len(record) > 0:
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
    
def update_booking_text(conn, old_booking_text: str, new_booking_text: str):
    try:
        cursor = conn.cursor()
        sql_update = 'UPDATE booking_text SET id = %s WHERE  id = %s'
        cursor.execute(sql_update, (new_booking_text, old_booking_text))
        conn.commit()
        cursor.close()
        return ('booking_text table is updated',)
    except psycopg2.errors.UniqueViolation as unique_error:
        conn.rollback()
        return (f"Error: ID {new_booking_text} is already in the booking_text table", f"Details: {unique_error}")
    except psycopg2.errors.StringDataRightTruncation as truncation_error:
        conn.rollback()
        return (f"Error: ID {new_booking_text} is too long", f"Details: {truncation_error}")
    except psycopg2.errors.CheckViolation as short_name_error:
        conn.rollback()
        return (f"Error: ID {new_booking_text} is shorter than 3 characters", f"Details: {short_name_error}")   

def remove_booking_text(conn, booking_text):
    try: 
        cursor = conn.cursor()
        sql_find_item = 'SELECT id FROM booking_text WHERE id = (%s)'
        cursor.execute(sql_find_item, (booking_text,))
        record = cursor.fetchall()

        if len(record) > 0:
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
    
def update_employee(conn, old_employee: str, new_employee: str):
    try:
        cursor = conn.cursor()
        sql_update = 'UPDATE employee SET id = %s WHERE  id = %s'
        cursor.execute(sql_update, (new_employee, old_employee))
        conn.commit()
        cursor.close()
        return ('employee table is updated',)
    except psycopg2.errors.UniqueViolation as unique_error:
        conn.rollback()
        return (f"Error: ID {new_employee} is already in the employee table", f"Details: {unique_error}")
    except psycopg2.errors.StringDataRightTruncation as truncation_error:
        conn.rollback()
        return (f"Error: ID {new_employee} is too long", f"Details: {truncation_error}")
    except psycopg2.errors.CheckViolation as short_name_error:
        conn.rollback()
        return (f"Error: ID {new_employee} is shorter than 3 characters", f"Details: {short_name_error}")   

def remove_employee(conn, employee):
    try: 
        cursor = conn.cursor()
        sql_find_item = 'SELECT id FROM employee WHERE id = (%s)'
        cursor.execute(sql_find_item, (employee,))
        record = cursor.fetchall()
        
        if len(record) > 0:
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
    
## topic table base function

def get_topic_id(conn, project_id: str, booking_text_id: str): 
    cursor = conn.cursor()
    sql_find_item = 'SELECT id FROM topic WHERE project_id = (%s) AND booking_text_id = (%s)'
    cursor.execute(sql_find_item, (project_id, booking_text_id))
    record = cursor.fetchall()
    cursor.close()
    return record

def add_new_topic(conn, project_id: str, booking_text_id: str, necessary_hours = 0):
    try:
        record = get_topic_id(conn, project_id, booking_text_id)
        if len(record) == 0:
            cursor = conn.cursor()
            sql_insert = 'INSERT INTO topic (project_id, booking_text_id, necessary_hours) VALUES (%s, %s, %s)'
            cursor.execute(sql_insert, (project_id, booking_text_id, necessary_hours))
            conn.commit()
            cursor.close()
            state_msg = f'New topic is added with {booking_text_id} booking text for {project_id} project'
        else:
            state_msg = f'There is already a topic (id={record[0][0]}) with {booking_text_id} booking text for {project_id} project'
        return (state_msg,)
    except psycopg2.errors.UniqueViolation as unique_error:
        conn.rollback()
        return (f"Error: {booking_text_id} booking text for {project_id} project is already in the topic table", f"Details: {unique_error}")
    except psycopg2.errors.ForeignKeyViolation as foreign_key_error:
        conn.rollback()
        return (f"Error: A foreign key constraint is violated in the topic table", f"Details: {foreign_key_error}")

def update_topic_worked_hours(conn, project_id: str, booking_text_id: str, new_worked_hours):
    try:
        record = get_topic_id(conn, project_id, booking_text_id)
        if len(record) > 0:
            cursor = conn.cursor()
            id_to_update = record[0][0]
            print(type(id_to_update))
            sql_update = 'UPDATE topic SET worked_hours = %s WHERE  id = %s'
            cursor.execute(sql_update, (new_worked_hours, id_to_update))
            conn.commit()
            cursor.close()
            state_msg = 'topic table is updated'
        else:
            state_msg = f'Topic with {booking_text_id} booking text for {project_id} project is not in the topic table'
        return (state_msg,)
    except psycopg2.errors.InvalidTextRepresentation as type_error:
        conn.rollback()
        return (f'Error: working hours must be a number', f'Details: {type_error}')

def update_topic_necessary_hours(conn, project_id: str, booking_text_id: str, new_necessary_hours):
    try:
        record = get_topic_id(conn, project_id, booking_text_id)
        if len(record) > 0:
            cursor = conn.cursor()
            id_to_update = record[0][0]
            print(type(id_to_update))
            sql_update = 'UPDATE topic SET necessary_hours = %s WHERE  id = %s'
            cursor.execute(sql_update, (new_necessary_hours, id_to_update))
            conn.commit()
            cursor.close()
            state_msg = 'topic table is updated'
        else:
            state_msg = f'Topic with {booking_text_id} booking text for {project_id} project is not in the topic table'
        return (state_msg,)
    except psycopg2.errors.InvalidTextRepresentation as type_error:
        conn.rollback()
        return (f'Error: necessary hours must be a number', f'Details: {type_error}')


def update_topic_project_id(conn, old_project_id: str, booking_text_id: str, new_project_id: str):
    try:
        record = get_topic_id(conn, old_project_id, booking_text_id)
        if len(record) > 0:
            cursor = conn.cursor()
            id_to_update = record[0][0]
            print(type(id_to_update))
            sql_update = 'UPDATE topic SET project_id = %s WHERE  id = %s'
            cursor.execute(sql_update, (new_project_id, id_to_update))
            conn.commit()
            cursor.close()
            state_msg = 'topic table is updated'
        else:
            state_msg = f'Topic with {booking_text_id} booking text for {old_project_id} project is not in the topic table'
        return (state_msg,)
    except psycopg2.errors.ForeignKeyViolation as foreign_key_error:
        conn.rollback()
        return (f"Error: The project_id foreign key constraint is violated in the topic table", f"Details: {foreign_key_error}")
    
def update_topic_booking_text_id(conn, project_id: str, old_booking_text_id: str, new_booking_text_id: str):
    try:
        record = get_topic_id(conn, project_id, old_booking_text_id)
        if len(record) > 0:
            cursor = conn.cursor()
            id_to_update = record[0][0]
            print(type(id_to_update))
            sql_update = 'UPDATE topic SET project_id = %s WHERE  id = %s'
            cursor.execute(sql_update, (new_booking_text_id, id_to_update))
            conn.commit()
            cursor.close()
            state_msg = 'topic table is updated'
        else:
            state_msg = f'Topic with {old_booking_text_id} booking text for {project_id} project is not in the topic table'
        return (state_msg,)
    except psycopg2.errors.ForeignKeyViolation as foreign_key_error:
        conn.rollback()
        return (f"Error: The booking_text_id foreign key constraint is violated in the topic table", f"Details: {foreign_key_error}")

def remove_topic(conn, project_id: str, booking_text_id: str):
    try: 
        record = get_topic_id(conn, project_id, booking_text_id)
        if len(record) > 0:
            cursor = conn.cursor()
            id_to_remove = record[0][0]
            sql_delete = 'DELETE FROM employee WHERE id = (%s)'
            cursor.execute(sql_delete, (id_to_remove,))
            conn.commit()
            cursor.close()
            state_msg = f'Topic with {booking_text_id} booking text for {project_id} project is removed'
        else:
            state_msg = f'Topic with {booking_text_id} booking text for {project_id} project is not in the topic table'
        return (state_msg,)
    except psycopg2.errors.UndefinedFunction as undefined_error:
        conn.rollback()
        return (f'Error: project_id or booking_text_id is not a string', f'Details: {undefined_error}')
    
## topic_employee table base functions

def get_topic_employee_relation(conn, topic_id, employee_id: str): 
    cursor = conn.cursor()
    sql_get_topic_employee_relation = 'SELECT topic_id, employee_id FROM topic_employee WHERE topic_id = (%s) AND employee_id = (%s)'
    cursor.execute(sql_get_topic_employee_relation, (topic_id, employee_id))
    record = cursor.fetchall()
    cursor.close()
    return record

def get_topic_info(conn, topic_id):
    cursor = conn.cursor()
    sql_get_topic_info = 'SELECT project_id, booking_text_id FROM topic WHERE id = (%s)'
    cursor.execute(sql_get_topic_info, (topic_id,))
    record = cursor.fetchall()
    cursor.close()
    return record

def add_new_topic_employee_relation(conn, topic_id, employee_id: str):
    try:
        record = get_topic_employee_relation(conn, topic_id, employee_id)
        if len(record) == 0:
            cursor = conn.cursor()
            sql_insert = 'INSERT INTO topic_employee (topic_id, employee_id) VALUES (%s, %s)'
            cursor.execute(sql_insert, (topic_id, employee_id))
            conn.commit()
            cursor.close()
            state_msg = 'New topic_employee relation is added'
        else:
            topic_record = get_topic_info(conn, topic_id)
            project = topic_record[0][0]
            booking_text = topic_record[0][1]
            state_msg = f'The relation between the {booking_text} booking text for {project} project and {employee_id} employee is already in the database'
        return (state_msg,)        
    except psycopg2.errors.ForeignKeyViolation as foreign_key_error:
        conn.rollback()
        return (f"Error: The topic_id or the employee_id is wrong", f"Details: {foreign_key_error}")
    except psycopg2.errors.StringDataRightTruncation as truncation_error:
        conn.rollback()
        return (f"Error: ID {employee_id} is too long", f"Details: {truncation_error}")
    except psycopg2.errors.CheckViolation as short_name_error:
        conn.rollback()
        return (f"Error: ID {employee_id} is shorter than 3 characters", f"Details: {short_name_error}") 
    
def remove_topic_employee_relation(conn, topic_id, employee_id: str):
    try:
        record = get_topic_employee_relation(conn, topic_id, employee_id)
        topic_record = get_topic_info(conn, topic_id)
        project = topic_record[0][0]
        booking_text = topic_record[0][1]
        if len(record) > 0:
            topic_record = get_topic_info(conn, topic_id)
            project = topic_record[0][0]
            booking_text = topic_record[0][1]
            cursor = conn.cursor()
            sql_delete = 'DELETE FROM topic_employee WHERE topic_id = (%s) AND employee_id = (%s)'
            cursor.execute(sql_delete, (topic_id, employee_id))
            conn.commit()
            cursor.close()
            state_msg = f'The relation between the {booking_text} booking text for {project} project and {employee_id} employee is removed'
        else:
            state_msg = f'The relation between {topic_id} topic and {employee_id} employee is not in the topic_employee table'
        return (state_msg,)
    except psycopg2.errors.UndefinedFunction as undefined_error:
        conn.rollback()
        return (f'Error: employee_id is not a string', f'Details: {undefined_error}')

## test functions

if __name__ == '__main__':
    config = load_config(filename=path+r'\app\database.ini')
    conn = connect(config)
    state = remove_topic_employee_relation(conn, 11, 'Example')
    print_state(state)
    table_name = 'topic_employee'
    projects = list_all_items(conn, table_name)
    for project in projects:
        print(project)