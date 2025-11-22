<!-- The Dynamic Table Generator  Create a webpage table.php that accepts a number.

Generate the Multiplication Table for that number (1 to 10) inside an HTML <table>.

Styling: If the result is Even, color the row background Light Blue. If Odd, color it Light Gray. -->
<!DOCTYPE html>

<head>
    <title>Table Generator</title>
    <style>
        body { font-family: sans-serif; }
        table {
            border-collapse: collapse;
            width: 50%;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #333;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #333;
            color: white;
        }
    </style>
</head>

<body>
        <h2> Dynamic Table Generator </h2>
        <form method = "post"> 
            <label>Enter a number:<label>
            <input type="number" name="num" required placeholder="e.g., 8">
            <button type="submit"> Generate Table</button>
        </form>

        <?php
            if (isset($_POST['num'])){
                $num = $_POST['num'];
                echo "<h3> Multiplication table for $num </h3>";

                echo "<table>";
                    echo "<tr>";
                        echo "<th>Equation</th>";
                        echo "<th>Result</th>";
                    echo "</tr>";
                    
                    for ($i = 1; $i <= 10; $i++) {
                        $result = $i * $num;

                        if($result % 2 == 0) {
                            $bg_color = "#4bc3e4ff";
                        } else {
                            $bg_color = "#f0f0f0";
                        }

                        echo "<tr style = 'background-color: $bg_color;'>";
                            echo "<td>$num x $i</td>";
                            echo "<td>$result</td>";
                        echo "</tr>";
                    }
                
                echo "</table>";
            }
        ?>
</body>

</html>