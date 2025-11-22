<!-- The "Reference" Test (Theory in Code)  
Create a webpage reference.php.

Create a function addFive($num) that uses Pass-by-Value.

Create a function addFiveRef(&$num) that uses Pass-by-Reference.

Pass a variable $x = 10 to both.

Print the value of $x before and after calling each function to prove to the 
examiner that you know the difference. -->

<!DOCTYPE html>
<head>
    <title>Reference Test</title>
    <style>
        body {
            font-family: sans-serif;
            padding: 20px;
        }
        .box {
            border: 1px solid #ccc;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <form method="post">
        <label>Enter a number: </label>
        <input type="number" name="num" required>
        <br><br>
        <button type="submit">Submit</button>
    </form>
    <br><br><hr><br><br>

    <?php 
        function addFive($num) {
            $num += 5;
            echo "Value inside the function: $num<br>";

        }

        function addFiveRef(&$num) {
            $num += 5;
            echo "Value inside the function: $num<br>";
        }
    ?>
    <div class="box">
        <h3>Test 1: Pass by value (No &)</h3>
        <?php
            if(isset($_POST['num'])) {
                $num = $_POST['num'];
                echo "Value before passing to functions: <strong>$num</strong><br>";

                addFive($num);
                echo "Value after passing to a function: <strong>$num</strong><br>";
                echo "<br><em>Result did not change. PHP sent a copy.</em>";
            }
        ?>
    </div>

    <div class="box">
        <h3>Test 2: Pass by reference</h3>
        <?php
            if(isset($_POST['num'])) {
                $num = $_POST['num'];
                echo "Value before passing to functions: <strong>$num</strong><br>";

                addFiveRef($num);
                echo "Value after passing to a function: <strong>$num</strong><br>";
                echo "<br><em>Result changed. PHP sent the original address.</em>";
            }
        ?>
    </div>
</body>
</html>