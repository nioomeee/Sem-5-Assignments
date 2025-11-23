<!-- The Email Extractor Create email_tool.php.

Form: Enter a full Email Address (e.g., student@glsuniversity.com).

Logic:

Use string functions (like strpos and substr OR explode) to separate the Username (student) from the Domain (glsuniversity.com).

Check: If the domain is not "gmail.com", display a warning: "Please use a Gmail address."

Display: "Hello [Username], your provider is [Domain]." -->

<!DOCTYPE html>
<html>
    <head>
        <title>Email Extractor</title>
        <style>
            body {
                font-family: sans-serif;
                text-align: center;
                padding-top: 50px;
            }
            .warning {
                color: red;
                font-weight: bold;
            }
            .success {
                color: green;
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <form method="post" action="">
            <label>Enter your email: </label>
            <input type="email" placeholder="name@example.com" required name="mail">
            <br><br>
            <button type="submit">Extract Data</button>
        </form>
        <br><hr style="width=50%">

        <?php
            if(isset($_POST['mail'])) {
                $email = $_POST['mail'];
                $parts = explode("@", $email);
                $uname = $parts[0];
                $domain = $parts[1];

                if($domain != "gmail.com") {
                    echo "<p class='warning'>Warning: Please use a Gmail address!</p>";
                }

                echo "<p class='success'>Hello <strong>$uname</strong>,</p>";
                echo"<p>Your provider is <u>$domain</u>.</p>";
            }
        ?>
    </body>
</html>