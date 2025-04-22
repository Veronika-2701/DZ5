from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os
import pytest

os.environ['DB_PASSWORD'] = 'passw'
password = os.environ.get('DB_PASSWORD')
connection_string = f"postgresql://postgres:{password}@localhost:5432/postgres"

db = create_engine(connection_string)

@pytest.fixture()
def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO student (\"user_id\", \"level\", \"education_form\", \"subject_id\") " \
    "VALUES (:user_id, :level, :education_form, :subject_id)")
    connection.execute(sql, {"user_id":20, "level":'Beginner', "education_form":'personal', "subject_id":2})

    sql_sel = text("SELECT user_id FROM student WHERE user_id = :user_id")
    us_id = connection.execute(sql_sel, {"user_id":20}).fetchall()

    sql_del = text("DELETE FROM student WHERE user_id = :user_id")
    connection.execute(sql_del, {"user_id":20})

    assert us_id == [(20,)]

    transaction.commit()
    connection.close()

def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql_ins = text("INSERT INTO student (\"user_id\", \"level\", \"education_form\", \"subject_id\") " \
    "VALUES (:user_id, :level, :education_form, :subject_id)")
    connection.execute(sql_ins, {"user_id":11, "level":'Beginner', "education_form":'personal', "subject_id":1})

    sql_upd = text("UPDATE student SET level = :level WHERE user_id = :user_id")
    connection.execute(sql_upd, {"level":'Elementary', "user_id":11})

    sql_sel = text("SELECT level FROM student WHERE user_id = :user_id")
    lvl = connection.execute(sql_sel, {"user_id":11}).fetchall()
    
    sql_del = text("DELETE FROM student WHERE user_id = :user_id")
    connection.execute(sql_del, {"user_id":11})

    assert lvl == [('Elementary',)]

    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql_ins = text("INSERT INTO student (\"user_id\", \"level\", \"education_form\", \"subject_id\") " \
    "VALUES (:user_id, :level, :education_form, :subject_id)")
    connection.execute(sql_ins, {"user_id":999, "level":'Elementary', "education_form":'group', "subject_id":5})
                       
    sql_sel = text("SELECT user_id FROM student WHERE user_id = :user_id")
    us_id = connection.execute(sql_sel, {"user_id":999}).fetchall()

    sql_del = text("DELETE FROM student WHERE user_id = :user_id")
    connection.execute(sql_del, {"user_id":999})

    assert us_id == [(999,)]

    transaction.commit()
    connection.close()
