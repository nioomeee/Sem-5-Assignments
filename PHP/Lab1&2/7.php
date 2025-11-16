<!-- Demonstrate the use of a variable with a string value and apply the 
.= (concatenationassignment) operator to add more text -->
<!DOCTYPE hml>
    <head>
        <title>String concatenation</title>
    </head>
    <body>
        <?php 
            $sentence = "PHP is ";
            $sentence .= "a powerful";
            $sentence .= " scripting";
            $sentence .= " language.";
            echo $sentence;
            echo "<br>";

        ?>
    </body>
</html>