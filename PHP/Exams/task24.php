<!-- Problem:

Phone: Must be exactly 10 digits.

Bio: Extract all hashtags (words starting with #). -->

<!DOCTYPE html>
<html>
    <head>
        <title>Regex matchings</title>
    </head>
    <body>
        <form method="post" action="">
            Enter your phone number:
            <input type="text" name="phone" required><br><br>
            Enter your bio:
            <textarea name="bio" required></textarea><br><br>
            <button type="submit">Ananlyze</button><br><br>
        </form>
        <hr><br>
        <?php
            if(isset($_POST['phone'])) {
                $phone =$_POST['phone'];
                $bio = $_POST['bio'];

                echo "<h3>Results:</h3>";

                if(preg_match("/^\d{10}$/", $phone)){
                    echo "Phone number is valid";
                } else {
                    echo "Phone number is invalid";
                }

                preg_match_all("/#\w+/", $bio, $matches);
                echo "<br><br><h3>Hashtags found:</h3>";
                echo "<pre>";
                    print_r($matches[0]);
                echo "</pre>";
            }
        ?>
    </body>
</html>