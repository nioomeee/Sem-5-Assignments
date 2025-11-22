<!-- HTML Form: Create a form with one text input: "Enter a Limit" (e.g., 20).

PHP:

Capture the limit using $_POST.

Use a do...while loop to print numbers from 1 to that Limit.

Logic: If the number is divisible by 5, print "High Five!". If it's 13, continue (skip it). If it reaches 50 (even if user typed 100), break force stop.

Output: An Unordered List (<ul>). -->

<!DOCTYPE html>
<head>
    <title>Loop</title>
</head>
<body>
    <h3>Loop control</h3>

    <form method = "post">
        <label>Enter the limit: </label>
        <input name = "limit" type = "number" min="1" required>
        <button type = submit>Go</button>
    </form>

    <hr>

    <?php
        if (isset($_POST['limit'])) {
            $limit = $_POST['limit'];
            $i = 1;

            echo "<h3> Printing numbers: </h3>";
            echo "<ul>";

            do {
                
                if ($i == 50) {
                    echo "<li>Exiting loop at 50</li>";
                    break;
                }

                if ($i == 13) {
                    $i++;
                    continue;
                }

                if ($i % 5 == 0) {
                    echo "<li>High Five!</li>";
                } else {
                    echo "<li>$i</li>";
                }

                $i++;

            } while ($i <= $limit);

            echo "</ul>";
        }
    ?>
</body>

</html>