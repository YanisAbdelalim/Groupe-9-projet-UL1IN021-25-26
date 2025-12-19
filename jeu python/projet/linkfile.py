from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__) #initialiser le serveur

@app.route("/")
def index():   #ouvre le fichier html quand on ouvre le site
    return render_template("ecran_titre.html")

@app.route("/start")
def start_game():  #ouvre le jeu pygame quand on clique sur le bouton start du site
    subprocess.Popen(["python", "reaction_game_v1.2.py"])  #subprocess permet de ne pas arrêter le fonctionnement du serveur pendant que le jeu se lance
    return "ok"

@app.route("/score", methods=["POST"])
def receive_score(): #recupere le score et le stocke dans le serveur
    global latest_score
    data = request.json
    latest_score = data["score"]
    return jsonify({"status": "ok"})

@app.route("/score", methods=["GET"])
def send_score():  #envoie le score stocké ici au site web quand il est demandé
    return jsonify({"score": latest_score})




if __name__ == '__main__':
    app.run(debug=True)
