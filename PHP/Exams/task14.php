<!-- Create matrix.php.


Form: No input needed (Hardcode the data for this one, as per Lab 5 Q1 ).

Logic: Create a 2D array: $students = [ ["Name"=>"Amit", "Sub"=>"PHP", "Marks"=>80], ["Name"=>"Sara", "Sub"=>"Java", "Marks"=>90] ];

Search: Add a text input to "Search for a Student Name".

Display: Use a foreach loop. If the search matches a name, show only that row; otherwise show all. -->

<!DOCTYPE html>
<html>
    <head>
        <title>Students</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                padding-top: 50px;
                text-align: center;
            }
            table {
                border-collapse: collapse;
                margin: 20px auto;
                padding-top: 20px;
                width: 60%;
            } 
            th, td {
                border: 1px solid #333;
                padding: 10px;
                text-align: left;
            }
            th {
                text-align:center;
                background-color: #333;
                color: white;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }

        </style>
    </head>
    <body>
        <h2>Student Record Search</h2>
        <form method="post" action="">
            <label>Search student by name: </label>
            <input type="text" placeholder="e.g., Amit" name="search_term">
            <br><br>
            <button type="submit">Search</button>
            <button type="submit" name="clear">Show all</button>
        </form>
        <br><br><hr>

        <?php
            $students = [
                ["Name" => "Anika", "Sub" => "PHP", "Marks" => 80],
                ["Name" => "Tanya", "Sub" => "Python", "Marks" => 98],
                ["Name" => "Gouri", "Sub" => "Java", "Marks" => 89],
                ["Name" => "Preet", "Sub" => "PHP", "Marks" => 78]                
            ];

            $search = $_POST['search_term'] ?? '';

            if(isset($_POST['clear'])) {
                $search = "";
            }

            echo "<h3>Result:</h3>";
            echo "<table>";
                echo "<tr> <th>Name</th> <th>Subject</th> <th>Marks</th> </tr>";

                foreach ($students as $student) {
                    $name = $student['Name'];
                    
                    if(empty($search) || stripos($name, $search) !== false) {
                        echo "<tr>";
                            echo "<td>" . $student['Name'] . "</td>";
                            echo "<td>" . $student['Sub'] . "</td>";
                            echo "<td>" . $student['Marks'] . "</td>";
                        echo "</tr>";
                    }
                }
            echo "</table>";
        ?>
    </body>
</html>