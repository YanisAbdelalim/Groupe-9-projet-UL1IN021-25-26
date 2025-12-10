<?php
$host = 'localhost';
$db = 'jeu';
$user = 'root';
$pass = '';

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) die("Erreur de connexion: " . $conn->connect_error);

$sql = "SELECT nom_joueur, score FROM scores ORDER BY score DESC, date_saisie ASC";
$result = $conn->query($sql);

$scores = [];
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        $scores[] = $row;
    }
}

header('Content-Type: application/json');
echo json_encode($scores);

$conn->close();
?>
