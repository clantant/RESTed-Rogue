from flask import Flask

app = Flask(__name__)

@app.route('/quest/start', methods=['POST'])

@app.route('/quest/end', methods=['DELETE'])

@app.route('/player/move/<int:room_id>', methods=['GET'])

@app.route('/player/status', methods=['GET'])

if __name__ == "__main__":
	app.run(host='0.0.0.0')

