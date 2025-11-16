<!-- Create a form with username and id fields using the POST method.
On submission, show:
• "Welcome [username]" if the id is blank display appropriate message.
• "Invalid login" otherwise. -->

<!DOCTYPE hml>
    <head>
        <title>AForm</title>
    </head>
    <body>
        <form method="post">
            <table>
                <tr>
                    <td><label>Username:</label></td>
                    <td><input type="text" name="uname"> </td>
                </tr>
                <tr>
                    <td><label>ID:</label></td>
                    <td><input type="text" name="id"> </td>
                </tr>
                <tr>
                    <td><input type="submit" value="submit"> </td>
                </tr>
            </table>
        </form>

        <?php
            if($_SERVER["REQUEST_METHOD"] == "POST") {
                $username = $_POST['uname'];
                $ID = $_POST['id'];

                if (!empty($username) && empty($ID)) {
                    echo "Welcome $username, but ID cant be blank";
                } elseif (!empty($username) && !empty($ID)) {
                    echo "Welcome $username, id = $ID";
                } else {
                    echo "Invalid login";
                }
            }
        ?>
    </body>
</html>

