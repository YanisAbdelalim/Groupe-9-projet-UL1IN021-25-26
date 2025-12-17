<?php
$host = 'localhost';
$db = 'jeu';
$user = 'root';
$pass = '';

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) die("Erreur de connexion: " . $conn->connect_error);

$nom_joueur = isset($_POST['nom_joueur']) ? $_POST['nom_joueur'] : '';
$score = isset($_POST['score']) ? intval($_POST['score']) : 0;

if ($nom_joueur && $score >= 0) {
    $stmt = $conn->prepare("INSERT INTO scores (nom_joueur, score, date_score) VALUES (?, ?, NOW()");
    $stmt->bind_param("si", $nom_joueur, $score);
    if ($stmt->execute()) echo "Score enregistré !";
    else echo "Erreur: " . $stmt->error;
    $stmt->close();
}

$conn->close();
?>

