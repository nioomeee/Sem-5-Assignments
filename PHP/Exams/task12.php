<!-- The Fibonacci Generator

Form: Enter a "Limit" (e.g., 10).

Logic:

Print the first N numbers of the Fibonacci Series (0, 1, 1, 2, 3, 5, 8...).

Logic: $n3 = $n1 + $n2. Then swap the variables ($n1=$n2, $n2=$n3).

Display: Print them as a horizontal list separated by arrows (->). -->

<!DOCTYPE html>
<html>
    <head>
        <title>Fibonacci Generator</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                padding-top: 50px;
                text-align: center;
            }
            .arrow {
                color: #e67e22;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <h2>Fibonacci Series Generator</h2>
        <form method="post" action="">
            <label>Enter a limit: </label>
            <input type="number" placeholder="e.g., 10" name="limit" required>
            <br><br>
            <button type="submit">Generate</button>
        </form> 
        <br><br><hr>
        <?php
            function fibonacci ($n) {
                if($n == 0) return 0;
                if ($n == 1) return 1;

                return fibonacci($n-1) + fibonacci($n-2);
            }
            if (isset($_POST['limit'])) {
                $limit = intval($_POST['limit']);
                echo "<h3> Series: </h3>";
                for ($i = 0; $i <= $limit; $i++) {
                    if($i > 0){
                        echo "<span class='arrow'> -> </span>";
                    }
                    echo fibonacci($i);
                }
            }
        ?>
    </body>
</html>