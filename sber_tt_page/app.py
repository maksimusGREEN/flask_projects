from flask import Flask, render_template, g
from FDataBase import FDataBase
import os, sqlite3
from src import get_players_data
from flask_apscheduler import APScheduler

DATABASE = '/tmp/sberteam.db'
DEBUG = False
SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v08k'
USERNAME = 'vladimir'
PASSWORD = '123'
SCHEDULER_API_ENABLED = True

def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path,'sberteam.db')))


headings = ('№', 'ФИО', 'Рейтинг', 'Дата последнего турнира')
players_list = ['81844', '101970', '54312', '117961', '12499', '50127', '84215', '2418', '79013', '86618', '55733', '23020', '5323', '18041', '14906', '10683', '23499', '6623', '55062', '22722', '114302', '112570', '75480', '131056']

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

@app.teardown_appcontext
def close_db(error):
    '''Закрываем соединение с БД, если оно было установлено'''
    if hasattr(g, 'link_db'):
        g.link_db.close()

if __name__=='__main__':
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

# определение задачи
@scheduler.task('interval', id='update_db', seconds=7200)
def update_database():
    with app.app_context():
        db = get_db()
        dbase = FDataBase(db)
        dbase.clearTable()
        data = get_players_data(players_list)
        for row in data:
            dbase.fillTable(*row)

#app routing to url
@app.route("/")
def table():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('table.html', headings=headings, data=dbase.getPlayers())

if __name__=='__main__':
    app.run(debug=DEBUG)

