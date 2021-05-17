from flask import Flask, Blueprint, render_template
import csv

def load_scores(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        players = []
        for line in reader:
            players.append(line)
    return players

def process_scores(players):
    dict_list = []
    for player in players:
        score_dict = {}
        score_dict["name"] = player["name"]
        score_dict["id"] = player["id"]
        score_dict["level"] = player["level"]
        score_dict["score"] = player["score"]
        dict_list.append(score_dict)
    return dict_list

def get_scores():
    filename = 'webapp/pvzscore.csv'
    data = load_scores(filename)
    scores = process_scores(data)
    return scores

pvz_bp = Blueprint("pvz",__name__)
app = Flask(__name__)
app.register_blueprint(pvz_bp)

@pvz_bp.route("/")
def home():
    return render_template("home.html")

@pvz_bp.route("/about")
def about():
    return render_template("about.html")

@pvz_bp.route("/scoreboard")
def score():
    scores = get_scores()
    return render_template("scoreboard.html", scores = scores)

@pvz_bp.route("/scoreboard/<int:player_id>")
def player(player_id):
    scores = get_scores()
    for score in scores:
        if score["id"] == str(player_id):
            return render_template("player.html", score = score)

@pvz_bp.route("/units")
def units():
    return render_template("units.html")

if __name__ == "__main__":
    app.run(debug=True)