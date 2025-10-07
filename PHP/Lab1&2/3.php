<!-- Create a php program page that will perform given below definitions:
• Define a constant for your school name.
• Define variables for your name, class, and grade.
• Display them all using echo. -->
<!DOCTYPE html>
    <head>
        <title>School and stuff</title>
    </head>
    <body>
        <?php 
            define("SCHOOL_NAME", "Hiramani"); //this is the way to declare constants in php

            $name = "Shanti";
            $class = "11th";
            $grade = "A";

            echo "School : " . SCHOOL_NAME . "<br>";  //it's a constant so, no need for $
            echo "Name : " . $name . "<br>";
            echo "Class : " . $class . "<br>";
            echo "Grade : " . $grade . "<br>";
        ?>
    </body>
</html>