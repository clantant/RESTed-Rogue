from flask import Flask, request, session
from restgame import start, end
import os
import cPickle as pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or \
    '\xbb\x81\xd4ya\x17&NH\xa7\x1c{\x08Mo\xc9!\xcd\xf1\xc3\x81\x9e.P'
global DUNGEON

@app.route('/quest/start', methods=['POST'])
def start_dungeon():
    if not request.json or not 'name' in request.json:
        abort(400)
    DUNGEON = start(request.json['name'])
    session['rooms'] = DUNGEON.roomlist()
    session['player'] = DUNGEON.player
    print session['rooms']
#    session['DUNGEON'] = {'rooms' : DUNGEON.roomlist(), 'player' : DUNGEON.player}
    return DUNGEON.status()

@app.route('/quest/end', methods=['DELETE'])
def end_dungeon():
    rooms = session['rooms']
    player = session['player']
    DUNGEON = reinit_dungeon(rooms, player)
    end(DUNGEON)

@app.route('/player/move/<int:room_id>', methods=['GET'])
def move_player():
    rooms = session['rooms']
    player = session['player']
    DUNGEON = reinit_dungeon(rooms, player)
    DUNGEON.move(room_id)

@app.route('/player/status', methods=['GET'])
def return_status():
    print session['rooms']
    rooms = session['rooms']
    player = session['player']
    DUNGEON = reinit_dungeon(rooms, player)
    return DUNGEON.status()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

