<!DOCTYPE html>
    <head>
        <title>Stats Result</title>
        <style>
            .result-box {
                border: 2px solid #4caf50;
                background-color: #f9f9f9;
                padding: 20px;
                width: 300px;
                border-radius: 10px;
                font-family: 'Segoe UI', sans-serif;
            }
            .stat-item {
                font-size: 18;
                margin: 5px 0;
                border-bottom: 1 px dashed #ccc;
            } 
            a {
                text-decoration: none;
                display: inline-block;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <?php
            function calculate($n1, $n2) {
                $sum = $n1 + $n2;
                $diff = $n1 - $n2;
                $prod = $n1 * $n2;

                return [
                    "sum" => $sum,
                    "prod" => $prod,
                    "diff" => $diff
                ];
            }
            if (isset($_POST['num1']) && isset($_POST['num2'])) {
                $n1 = $_POST['num1'];
                $n2 = $_POST['num2'];

                $results = calculate($n1, $n2);

                echo "<h2> Results: </h2>";
                echo "<div class='result-box'>";
                    echo "<div class='stat-item'><strong>Sum: </strong>" . $results['sum'] . "</div>";
                    echo "<div class='stat-item'><strong>Product: </strong>" . $results['prod'] . "</div>";
                    echo "<div class='stat-item'><strong>Difference: </strong>" . $results['diff'] . "</div>";
                echo "</div>";
            } else {
                echo "<p style = 'color:red'>Error: No information received.</p>";
            }
        ?>

        <br>
        <a href="task4.php">Go back to the calculator</a>
    </body>
</html>