<!DOCTYPE html>
    <head>
        <title>Greeting page</title>
    </head>
    <body>
        <?php
            $name = $_GET['name'];
            $age = $_GET['age'];

            echo "Hello $name, your age is $age!";
        ?>
    </body>
</html>