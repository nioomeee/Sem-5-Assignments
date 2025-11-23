<!-- The Prime Number Checker Create prime.php.

Form: Enter a single number.

Logic:

Write a script to check if the number is Prime (divisible only by 1 and itself).

Hint: You need a loop from 2 to $num - 1. If $num % $i == 0, it's not prime.

Output: "[Number] is a Prime Number" (Green) or "[Number] is NOT Prime" (Red). -->

<!DOCTYPE html>
<html>
    <head>
        <title>Prime Number Checker</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                padding-top: 50px;
                text-align: center;
            }
            .success {
                font-weight: bold;
                color: #5fcb00ff; 
                font-size: 18px;
            }
            .fail {
                font-weight: bold;
                color: #ff2929ff;
                font-size: 18px;
            }
            button {
                color: #000038ff;
                border-radius: 5px;
                border: 1px solid #ff9898ff;
                background-color: #63f7ffff;
                padding: 5px;
                font-size: 15px;
            }
        </style>
    </head>
    <body>
        <h2> Prime number checker </h2>
        <form method="post" action="">
            <label>Enter a number: </label>
            <input type="number" name="num" placeholder="e.g., 9" required>
            <br><br>
            <button type="submit">Check Prime</button>
        </form>
        <br><br><hr>
        <?php
            function isPrime($num) {
                if ($num <= 1) {
                    return false;
                }
                for ($i = 2; $i <= ($num/2); $i++) {
                    if ($num % $i == 0) {
                        return false;
                    }
                }
                return true;
            }
            if(isset($_POST['num'])) {
                $num = $_POST['num'];
                
                if(isPrime($num)) {
                    echo "<p class='success'>$num is a Prime Number.</p>";
                } else {
                    echo "<p class='fail'>$num is not a Prime Number.</p>";
                }
            }
        ?>
    </body>
</html>