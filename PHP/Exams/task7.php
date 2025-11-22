<!-- The "Day Finder" Create day_finder.php.

Form: Ask the user to select a specific date (Input type date).

Logic:

Display that date in a "human" format: "15th August, 2025" (Use date() with format characters like jS F, Y).

Tell the user exactly which day of the week that was (e.g., "That was a Friday").

Bonus: If the date is today, print "Hey, that's today!" in green. -->

<!DOCTYPE html>
<html>
<head>
    <title>Day Finder</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            padding-top: 50px;
        }
        .today-msg {
            color: green;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <form method="post" action="">
        <label>Select a date: </label><br>
        <input type="date" name="user_date" required><br><br>
        <button type="submit">Analyze Data</button>
    </form>

    <?php
        date_default_timezone_set('Asia/Kolkata');
        if(isset($_POST['user_date'])) {
            $raw_date = $_POST['user_date'];
            $timestamp = strtotime($raw_date);

            // j(date), S(suffix like th), F(month), Y(year)
            $pretty_date = date('jS F, Y', $timestamp); 

            // l = full day name
            $day_name = date('l', $timestamp);

            echo "<h3>Results:</h3>";
            echo "<p><strong>Date: </strong>$pretty_date</p>";
            echo "<p><strong>That was a: </strong>$day_name</p>";

            if($raw_date == date('Y-m-d')){
                echo "<p class='today-msg'>Hey, that's today!</p>";
            }


        }
    ?>
</body>
</html>