<!-- Create Logic:

Start session_start().

Check if(isset($_SESSION['views'])).

If yes, increment it ($_SESSION['views']++). If no, set it to 1.

Display: "You have refreshed this page X times."

Reset: Add a button "Reset Counter" that runs unset($_SESSION['views']) -->

<?php
    session_start();

    if(isset($_POST['reset'])) {
        unset($_SESSION['views']);
    }

    if(isset($_SESSION['views'])) {
        $_SESSION['views']++;
    } else {
        $_SESSION['views'] = 1;
    }
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Session counter</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                padding-top: 50px;
                text-align: center;
            }
            .counter-box {
                font-size: 24px;
                padding: 20px;
                border: 2px solid #333;
                display: inline-block;
                margin-bottom: 20px;
                background-color: #f9f9f9;
            }
            .count {
                color: #d35400;
                font-weight: bold;
                font-size: 40px;
            }

        </style>
    </head>
    <body>
        <h2>Page View Counter</h2>
        <div class="counter-box">
            You have refreshed this page<br>
            <span class="count"><?php echo $_SESSION['views'];?></span><br>
            times.
        </div>

        <br>

        <form method = "post">
            <button type="submit" name="reset">Reset Count</button>
        </form>
    </body>
</html>