from flask import Flask, request
import restgame import *

app = Flask(__name__)
global DUNGEON

@app.route('/quest/start', methods=['POST'])
def start_dungeon():
    if not request.json or not 'name' in request.json:
        abort(400)
    DUNGEON = start(request.json['name'])
    return DUNGEON.status()

@app.route('/quest/end', methods=['DELETE'])
def end_dungeon():
  end(DUNGEON)

@app.route('/player/move/<int:room_id>', methods=['GET'])
def move_player():
    DUNGEON.move(room_id)

@app.route('/player/status', methods=['GET'])
def return_status():
    return DUNGEON.status()

if __name__ == "__main__":
    app.run(host='0.0.0.0')

