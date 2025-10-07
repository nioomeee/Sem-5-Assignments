<!-- Given two numbers $a = 25 and $b = 40, write conditions using:
• Greater than
• Less than
• Greater than or equal to
• Less than or equal to 
Display the result for each. -->

<!DOCTYPE hml>
    <head>
        <title>Assignment operators</title>
    </head>
    <body>
        <?php 
            $a = 25; 
            $b = 40; 

            echo "1st Number = $a <br>2nd Number = $b<br>";
            echo "<br>";

            echo "If 1st is greater than 2nd: <br>";
            
            if($a > $b) {
                echo "1st number is greater!<br>";
            } else {
                echo "2nd number is greter!<br>";
            }

            echo "<br>";

            echo "If 1st is less than 2nd <br>";

            if($a < $b) {
                echo "1st number is smaller than 2nd. <br>";
            } else {
                echo "2nd number is smaller than 1st <br>";
            }
            echo "<br>";


            echo "If 1st number is Greater than or equal to 2nd number: <br>";

            if($a >= $b) {
                echo "1st number is Greater than or equal to 2nd number <br>";
            } else {
                echo "2nd number is Greater than or equal to 1st number <br>";
            }
            echo "<br>";

            echo "If 1st number is less than or equal to 2nd number: <br>";

            if($a >= $b) {
                echo "1st number is less than or equal to 2nd number <br>";
            } else {
                echo "2nd number is less than or equal to 1st number <br>";
            }
            echo "<br>";

        ?>
    </body>
</html>