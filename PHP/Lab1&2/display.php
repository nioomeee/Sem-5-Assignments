<!DOCTYPE html>
    <head>
        <title>Welcome Page</title>
    </head>
    <body>
        <?php 
            if($_SERVER["REQUEST_METHOD"] == "POST") {
                $name = htmlspecialchars($_POST['name']);
                $email = htmlspecialchars($_POST['mail']);

                echo "Thank you, $name, for registering with the email: $email";
            } else {
                echo "Invalid request";
            }
        ?>
    </body>
</html>