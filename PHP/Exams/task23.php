<!-- a script to check if an input is a valid email. -->
<!DOCTYPE html>
<html>
    <head>
        <title>Email Validator</title>
    </head>
    <body>
        <form method="post">
            Enter your email: 
            <input type="email" name="mail" required>
            <br><br>
            <button type="submit">Validate</button>
        </form>
        <br><br><hr><br>
        <?php
            if(isset($_POST['mail'])) {
                $mail = $_POST['mail'];

                $pattern = "/^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2, 4}$/";

                if(preg_match($pattern, $mail)) {
                    echo "Valid mail";
                } else {
                    echo "Invalid Mail";
                }
            }
        ?>
    </body>
</html>