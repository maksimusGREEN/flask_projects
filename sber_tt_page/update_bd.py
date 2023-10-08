from src import get_players_data
from app import app, connect_db
from FDataBase import FDataBase

players_list = ['81844', '101970', '54312', '117961', '12499', '50127', '84215', '2418',\
                '79013', '86618', '55733', '23020', '5323', '18041', '14906', '10683',\
                '23499', '6623', '55062', '22722', '114302', '112570', '75480', '131056',\
                '81646', '3784', '5425', '19213', '1950', '27597', '14079', '25385', '121590', '25526', '93481']

db = connect_db()
dbase = FDataBase(db)
dbase.clearTable()
data = get_players_data(players_list)
for row in data:
    dbase.fillTable(*row)