<!-- Write a PHP program using $a = 15. Apply each assignment operator (+=, -=, *=, /=,%=) 
step by step and print the value of $a after each operation. -->

<!DOCTYPE hml>
    <head>
        <title>Assignment operators</title>
    </head>
    <body>
        <?php 
            $a = 15;

            echo "Start: $a <br>";

            $a += 5;
            echo "After += 5: $a <br>";

            $a -= 2;
            echo "After -= 2: $a <br>";

            $a *= 3;
            echo "After *= 3: $a <br>";

            $a /= 2;
            echo "After /= 2: $a <br>";

            $a %= 3;
            echo "After %= 3: $a <br>";
        ?>
    </body>
</html>