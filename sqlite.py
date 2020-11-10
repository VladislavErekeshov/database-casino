import sqlite3 as sl
from random import randint

global db
global sql

db = sl.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()
def reg():
    user_login = input('login: ')
    user_password = input('password: ')

    sql.execute(f"SELECT login FROM users WHERE login = '{user_login}'")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (user_login, user_password, 0))
        db.commit()

        print('вы зареганы')
    else:
        print('уже есть')

    for value in sql.execute("SELECT * FROM users"):
        print(value)



def casino():
    global user_login
    user_login = input('log in: ')
    


    #sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'")
    #balance = sql.fetchone()[0]

    sql.execute(f'SELECT login FROM users WHERE login = "{user_login}"')
    if sql.fetchone() is None:
        print('Такого логина не существует, зарегестрируйтесь')
        reg()
    else:
        while True:
            number = randint(1, 2)
            if input('Введите g чтоб играть, либо что-нибудь другое чтоб выйти: ') != 'g':
                print('Конец игры')
                break
            else:
                if number == 1:
                    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
                        balance = i[0]
                    sql.execute(f'UPDATE users SET cash = {balance + 1000} WHERE login = "{user_login}"')
                    db.commit()
                    print('you win')
                    print('your balance is: ', balance + 1000)
                else:
                    for i in sql.execute(f"SELECT cash FROM users WHERE login = '{user_login}'"):
                        balance = i[0]
                    sql.execute(f'UPDATE users SET cash = {balance - 1000} WHERE login = "{user_login}"')
                    db.commit()
                    print('you lose')
                    print('your balance is: ', balance - 1000)

            

def enter():
    #for i in sql.execute('SELECT login, cash FROM users'):
    #    print(i)

    sql.execute('SELECT login, cash FROM users')
    row = sql.fetchall()
    print(row)

def main():
    casino()
    enter()

main()