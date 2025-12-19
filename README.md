- COMMENT INSTALLER LE JEU
1) Télécharger et extraire le code du projet
2) Installer les modules python suivants: flask, pygame, request. Utiliser la commande "sudo apt install python3-nom_module"
3) Faire tourner LAMP sur le Raspberry. Placer les dossiers "leaderboard" et "leaderboard-only" dans le dossier "var/www/html"
4) Ouvrir sur un navigateur la page "http://localhost/phpmyadmin", éxécuter les commandes situées dans le fichier "commandes_sql.txt" dans le dossier leaderboard
5) Brancher la led rouge sur D22, la led bleu sur D5, la led verte sur D16, la led blanche sur D18, les deux touch sur D24 et D26, et le speaker plus sur PWM
6) Se placer dans le dossier projet, et éxécuter le fichier "linkfile.py". Se rendre sur le lien renvoyé dans le terminal ("http://127.0.0.1:5000")
7) Tout est prêt. Vous pouvez jouer au jeu

- COMMENT JOUER AU JEU
1) Pour jouer au jeu, cliquer sur jouer. La fenêtre pygame de la partie va s'ouvrir.
2) Une des 4 leds va s'illuminer. Les touches correspondantes sont S, D, F et G. Le touch branché sur D24 correspond à la touche F et le touch sur D26 correspond à la touche G.
3) Le score augmente quand on clique sur la bonne touche et diminue quand on rate.
4) Quand la partie est finie, entrer son nom pour valider le score puis revenir sur la page d'accueil.
