- COMMENT INSTALLER LE JEU -
1) Télécharger et extraire le code du projet
2) Faire tourner LAMP sur le Raspberry. Placer les dossiers "leaderboard" et "leaderboard-only" dans le dossier "var/www/html"
3) Ouvrir sur un navigateur la page "http://localhost/phpmyadmin", éxécuter les commandes situées dans le fichier "commandes_sql.txt" dans le dossier leaderboard
4) Brancher la led rouge sur D22, la led bleu sur D5, la led verte sur D16, la led blanche sur D18, les deux touch sur D24 et D26, et le buzzer sur PWM
5) Se placer dans le dossier projet, et éxécuter le fichier "linkfile.py". Se rendre sur le lien renvoyé dans le terminal ("http://127.0.0.1:5000")
6) Tout est prêt. Vous pouvez jouer au jeu
