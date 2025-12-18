from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("ecran_titre.html")

@app.route("/start") #site home
def start_game():
    subprocess.Popen(["python", "reaction_game_v1.2.py"])
    return "ok"

@app.route("/score", methods=["POST"])
def receive_score():
    global latest_score
    data = request.json
    latest_score = data["score"]
    return jsonify({"status": "ok"})

@app.route("/score", methods=["GET"])
def send_score():
    return jsonify({"score": latest_score})




if __name__ == '__main__':
    app.run(debug=True)