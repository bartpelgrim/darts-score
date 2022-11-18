from flask import Flask, render_template, request

from match import Match
from player import Player

app = Flask(__name__)
match = Match()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/enter_players', methods=['POST'])
def enter_players():
    result = request.form
    match.add_player(Player(result['player1']))
    match.add_player(Player(result['player2']))
    match.start()
    return render_template('match.html', player=match.game.active_player.name)


@app.route('/player_score', methods=['POST'])
def player_score():
    result = request.form
    valid_score = match.enter_score(int(result['player_score']))
    return render_template('match.html', player=match.game.active_player.name, error=not valid_score)


@app.route('/restart', methods=['POST'])
def restart():
    match.restart()
    return render_template('match.html', player=match.game.active_player.name)


@app.route('/undo', methods=['POST'])
def undo():
    match.undo_score()
    return render_template('match.html', player=match.game.active_player.name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
