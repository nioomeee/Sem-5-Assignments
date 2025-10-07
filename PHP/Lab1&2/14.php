<!-- Create a php program to perform the following:
    • Create a registration form that collects name and email.
    • On submit, pass the data to another page using POST.
    • On the second page, show a message: “Thank you, [Name], for registering with the 
    email: [Email]”. -->

<!DOCTYPE html>
    <head>
        <title>Registration Form</title>
    </head>
    <body>
        <form method="POST" action="display.php">
            <table>
                <tr>
                    <td>
                        <label for="name">Name: </label>
                    </td>
                    <td>
                        <input type="text" name="name" required>
                    </td>
                </tr>

                <tr>
                    <td>
                        <label for="mail">Email: </label>
                    </td>
                    <td>
                        <input type="email" name="mail" required>
                    </td>
                </tr>

                <tr>
                    <td colspan='2'>
                        <input type="submit" value="Submit">
                    </td>
                </tr>
            <table>
        </form>
    </body>
</html>