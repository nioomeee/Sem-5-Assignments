<!-- Create age_calc.php.

Form: Two inputs: "Your Birth Date" and "A Future Event Date".

Logic:

Calculate the user's current age in Years.

Calculate exactly how many Days correspond to the gap between the two dates using date_diff().

Display: Show the result in a styled alert box. -->

<!DOCTYPE html>
<html>
    <head>
        <title>Age difference</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                padding: 20px;
                text-align: center;
            }
            .alert-box {
                background-color: #8df9ffff;
                color: #0d47a1;
                border: 2px solid #2196f3;
                padding: 20px;
                width: 50%;
                margin: 20px auto;
                border-radius: 10px;
                font-size: 18px;
            }
            .stat {
                font-weight: bold;
                font-size: 24px;
                color: #8b512bff;
            }
        </style>
    </head>
    <body>
        <form method="post" action="">
            <table>
                <tr>
                    <td>Enter your birth date:</td>
                    <td><input type="date" name="dob" required></td>
                </tr>
                <tr>
                    <td>Enter future date:</td>
                    <td><input type="date" name="future" required></td>
                </tr>
                <tr>
                    <td colspan="2"><button type="submit">Calculate</button></td>
                </tr>
            </table>
        </form>

        <?php
            if(isset($_POST['dob']) && isset($_POST['future'])) {
                $dob = date_create($_POST['dob']);
                $future = date_create($_POST['future']);
                $now = date_create('today');

                $age_diff = date_diff($dob, $now);
                $current_age = $age_diff->y;

                $gap_diff = date_diff($dob, $future);
                $total_days = $gap_diff->days;

                echo "<div class='alert-box'>";
                    echo "<h3>Analysis Report</h3>";
                    echo "You are currently <span class='stat'>$current_age</span> years old.<br><br>";
                    echo "Between your birth and event, <br>";
                    echo "<span class='stat'>$total_days</span> days will have passed!";
                echo "</div>";
            }
        ?>
    </body>
</html>