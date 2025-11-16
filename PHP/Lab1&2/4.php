<!-- Take two numbers as PHP variables and perform basic arithmetic 
(add, subtract, multiply,divide) and display the results in an HTML list. -->
<!DOCTYPE html>
    <head>
        <title>Arithmetic list</title>
    </head>
    <body>
        <?php 
            $a = 20;
            $b = 40;

            $sum = $a + $b;
            $sub = $a - $b;
            $mul = $a * $b;
            $div = $a / $b;

            echo "<h3> Arithmetic operations: </h3> <br>";
            echo "<ul>";
            echo "<li> Addition: $sum  </li>";
            echo "<li> Subtraction: $sub  </li>" ;
            echo "<li> Multiplication: $mul   </li>";
            echo "<li> Division: $div  </li>";
            echo "</ul>"
        ?>
    </body>
</html>