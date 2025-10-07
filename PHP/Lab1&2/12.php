<!-- Create an HTML form that collects:
• Name
• Age
• Gender (radio buttons)
• Hobbies (checkboxes)
Use the POST method to display the submitted data in a formatted table using PHP. -->

<!DOCTYPE html>
    <head>
        <title>Form</title>
    </head>
    <body>
        <form method="POST">
            <table>
                <tr>
                    <td>
                        <label>Name: </label>
                    </td>
                    <td>
                        <input type="text" name="name">
                    </td>
                </tr>

                <tr>
                    <td>
                        <label>Age: </label>
                    </td>
                    <td>
                        <input type="number" name="age">
                    </td>
                </tr>

                <tr>
                    <td>
                        <label>Gender: </label>
                    </td>
                    <td>
                        <input type="radio" name="gender" value="Male"> Male
                        <input type="radio" name="gender" value="Female"> Female
                        <input type="radio" name="gender" value="Others"> Others
                    </td>
                </tr>

                <tr>
                    <td>
                        <label>Hobbies: </label>
                    </td>
                    <td>
                        <input type="checkbox" name="hobbies[]" value="Reading">Reading
                        <input type="checkbox" name="hobbies[]" value="Music">Music
                        <input type="checkbox" name="hobbies[]" value="Dancing">Dancing
                        <input type="checkbox" name="hobbies[]" value="Travelling">Travelling
                    </td>
                </tr>

                <tr>
                    <td colSpan="2">
                        <input type="submit" value="submit">
                    </td>
                </tr>
            </table>
        </form>

        <?php
            if($_SERVER["REQUEST_METHOD"] == "POST") {
                $name = $_POST['name'];
                $age = $_POST['age'];
                $gender = $_POST['gender'];
                $hobbies = isset($_POST['hobbies']) ? implode(", ", $_POST['hobbies']): "None";

                echo "<h3> Submitted details: </h3>";
                echo "<table border='1' cellpadding='5'>";
                echo "<tr> <th> Name: </th> <td> $name </td> </tr>";
                echo "<tr> <th> Age: </th> <td> $age </td> </tr>";
                echo "<tr> <th> Gender: </th> <td> $gender </td> </tr>";
                echo "<tr> <th> Hobbies: </th> <td> $hobbies </td> </tr>";
                echo "</table>";

            }
        ?>
    </body>
</html>