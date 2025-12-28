from src import get_players_data
from app import app, connect_db
from FDataBase import FDataBase

players_list = ['81844', '101970', '54312', '117961', '12499', '84215', '2418', '112262', '131716', '183162', \
                '79013', '86618', '55733', '23020', '5323', '18041', '14906', '10683', '93481', '118615', \
                '23499', '55062', '22722', '112570', '75480', '131056', '4975', '102638', '164647', \
                '24878', '3784', '5425', '1950', '27597', '14079', '25385', '121590', '97789', '124092', \
                '19931', '135229', '25292', '128214', '64673', '25552', '110513', '1789', '71948']

db = connect_db()
dbase = FDataBase(db)
dbase.clearTable()
data = get_players_data(players_list)
for row in data:
    dbase.fillTable(*row)