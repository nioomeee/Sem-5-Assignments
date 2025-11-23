<!-- fetch data -->

<!DOCTYPE html>
<html>
    <head>
        <title>Students</title>
    </head>
    <body>
        <h2>Fetching students data:</h2>
        
        <?php 
            // mysqli_connect(servername, username, password, dbname)
            $conn = mysqli_connect("localhost", "root", "", "test_db");

            if(!$conn) {
                die("Connection Failed!");
            }

            $sql = "SELECT * FROM students";

            $result = mysqli_query($conn, $sql);

            if(mysqli_num_rows($result) > 0) {
                echo "<table border='1'>";
                    echo "<tr> <th>ID</th> <th>Name</th> <th>Email</th> </tr>";

                    while($row = mysqli_fetch_assoc($result)) {
                        echo "<tr>";
                            echo "<td>". $row['id'] ."</td>";
                            echo "<td>". $row['name'] ."</td>";
                            echo "<td>". $row['email'] ."</td>";
                        echo "</tr>";
                    }
                echo "</table>";
            } else {
                echo "No students found";
            }

            mysqli_close();
        ?>
    </body>
</html>