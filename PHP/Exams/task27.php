<!-- CRUD ops on database connection -->

<?php
    $conn = mysqli_connect("localhost", "root", "password", "test_db");

    if(!$conn) {
        die("Connection failed!");
    }

    $id = "";
    $name = "";
    $email = "";
    $btn_text = "Save";

    // 1. DELETE
    if(isset($_GET['delete'])) {
        $id_to_delete = $_GET['delete'];

        mysqli_query($conn, "DELETE FROM students WHERE id=$id_to_delete");
    }

    // 2. EDIT
    if(isset($_GET['edit'])) {
        $id = $_GET['edit'];

        $result = mysqli_query($conn, "SELECT * FROM students WHERE id=$id");
        $row = mysqli_fetch_assoc($result);

        $name = $row['name'];
        $email = $row['email'];

        $btn_text = "Update";
    }

    // 3. Save/Update button
    if(isset($_POST['save_btn'])) {
        $n = $_POST['name'];
        $e = $_POST['email'];

        $hidden_id = $_POST['hidden_id'];

        if($hidden_id > 0) {
            $sql =("UPDATE students SET name='$n', email='$e' WHERE id='$hidden_id'");
        } else {
            $sql = ("INSERT INTO students (name, email) VALUES ('$n', '$e')");
        }

        mysqli_query($conn, $sql);

        header("Location: task27.php");
    }
?>

<!DOCTYPE html>
<html>
    <head>
        <title>CRUD Ops</title>
    </head>
    <body>
        <h2>Student Manager</h2>
        <form method="post">
            <input type="hidden" name="hidden_id" value="<?php echo $id; ?>">

            Name: <input type="text" name="name" value="<?php echo $name; ?>"> <br><br>
            Email: <input type="email" name="email" value="<?php echo $email; ?>"> <br><br>

            <button type="submit" name="save_btn"><?php echo $btn_text; ?></button>
        </form>

        <table border="1">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Action</th>
            </tr>

            <?php
                $result = mysqli_query($conn, "SELECT * FROM students");

                while($row = mysqli_fetch_assoc($result)) {
                    echo "<tr>";
                        echo "<td>". $row['id'] ."</td>";
                        echo "<td>". $row['name'] ."</td>";
                        echo "<td>";
                            echo "<a href='task27.php?edit=" . $row['id']. "'>Edit</a> | ";
                            echo "<a href='task27.php?delete=".$row['id']. "'>Delete</a>";
                        echo "</td>";
                    echo "</tr>";
                }
            ?>
        </table>
    </body>
</html>