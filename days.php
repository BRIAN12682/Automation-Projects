<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the event date from the form
    $event_date = $_POST["event_date"];

    // Calculate remaining days and time
    $current_date = date("Y-m-d");
    $remaining_time = strtotime($event_date) - strtotime($current_date);
    $remaining_days = floor($remaining_time / (60 * 60 * 24));
    $remaining_hours = floor(($remaining_time % (60 * 60 * 24)) / (60 * 60));
    $remaining_minutes = floor(($remaining_time % (60 * 60)) / 60);
    $remaining_seconds = $remaining_time % 60;

    // Display the remaining time
    echo "<h3>Remaining Time Until $event_date:</h3>";
    echo "<p>$remaining_days days, $remaining_hours hours, $remaining_minutes minutes, and $remaining_seconds seconds remaining.</p>";
}
?>
