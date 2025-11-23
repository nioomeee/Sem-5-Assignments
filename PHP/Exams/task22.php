<?php
    if(isset($_POST['login-btn'])) {
        $uname = $_POST['uname'];
        $pass = $_POST['password'];

        if(isset($_POST['remember'])) {
            setcookie("user", $uname, time()+86400);
            $msg = "Cookie Set! Close the browser and come back to see the magic.";
        } else {
            setcookie("user", "", time()-3600);
            $msg = "Logged in (Cookie not set)";
        }

    }
?>

<!DOCTYPE html>
<html>
    <head>
        <title>Cookie Login</title>
        <style></style>
    </head>
    <body>
        <h2>Form Login</h2>
        <?php
            if(isset($msg)) {
                echo "<p style='color:green'>$msg</p>";
            }
        ?>
        <form method="post" action="">
            <label>User Name: </label>
            <input type="text" name="uname" 
            value="<?php if(isset($_COOKIE['user'])) echo $_COOKIE['user']; ?>" required>
            <br><br>

            <label>Password: </label>
            <input type="password" name="password" required>
            <br><br>

            <label>
                <input type="checkbox" name="remember">Remember Me
            </label>
            <br><br>

            <button type="submit" name="login-btn">Login</button>
        </form>
    </body>
</html>