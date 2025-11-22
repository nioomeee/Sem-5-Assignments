<!-- The Intelligent Counter  
Create a webpage counter.php that accepts a Start Number, 
End Number, and a "Skip Number" from the user.

Use a loop to print numbers from Start to End.

Constraint: If the loop hits the "Skip Number", use continue to jump over it.

Constraint: If the loop reaches the number 50 (even if the user entered 100), use break to force stop.

Display: Show the numbers in a horizontal list separated by dashes (e.g., 1 - 2 - 4 - 5...). -->

<!DOCTYPE html>
<head>
    <title>Loop control</title>
    <style>
        body {
            font-family: "Segoe UI", Tahoma, Verdana, Geneva, sans-serif;
        }
        table {
            border-collapse: collapse;
        }
        td {
            padding: 10px;
            vertical-align: middle;
        }
        .result {
            font-family: monospace;
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            color: #333;
        }
    </style>
</head>
<body>
    <h2>Intelligent Counter</h2>
    <form method="post">
        <table>
            <tr>
                <td><strong>Enter starting number:</strong></td>
                <td><input type="number" name="start" placeholder="e.g., 1" min="0" required></td>
            </tr>
            <tr>
                <td><strong>Enter ending number:</strong></td>
                <td><input type="number" name="end" placeholder="e.g., 1" min="0" required></td>
            </tr>
            <tr>
                <td><strong>Enter number you want to skip:</strong></td>
                <td><input type="number" name="skip" placeholder="e.g., 1" min="0" required></td>
            </tr>
            <tr>
                <td><button type="submit">Start Counting</button></td>
            </tr>
        </table>
    </form>

    <hr>
    <div class="result">
        <?php
            if (isset($_POST['start'])) {
                $start = intval($_POST['start']);
                $end = intval($_POST['end']);
                $skip = intval($_POST['skip']);

                for ($i = $start; $i <= $end; $i++) {
                    if ($i == 50) {
                        echo " Stop (50)";
                        break;
                    }

                    if ($i == $skip) {
                        continue;
                    }

                    if ($i != $start) {
                        echo " - ";
                    }

                    echo $i;
                }
            }
        ?>
    </div>
</body>
</html>