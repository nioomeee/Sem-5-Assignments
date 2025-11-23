 <!-- connect, insert, display -->

<!DOCTYPE html>
<html>
    <head>
        <title>Adding students</title>
    </head>
    <body>
        <h2>Add new Students</h2>

        <form method="post">
            Name: <input type="text" name="s_name" required><br><br>
            Email: <input type="email" name="s_email" required><br><br>
            <button type="submit" name="save_btn">Save Data</button>
        </form>

        <hr>

        <?php
            if(isset($_POST['save_btn'])) {
                $name = $_POST['s_name'];
                $email = $_POST['s_email'];

                // mysqli_connect(servername, username, password, dbname)
                $conn = mysqli_connect("localhost", "root", "", "test_db");

                if(!$conn) {
                    die("Connection Failed!");
                } 

                $sql = "INSERT INTO students (name, email) VALUES ('$name', '$email')";

                if (mysqli_query($conn, $sql)) {
                    echo "Student saved successfully.";
                } else {
                    echo "Error: " . mysqli_error($conn);
                }
                mysqli_close($conn);
            }
        ?>
    </body>
</html>