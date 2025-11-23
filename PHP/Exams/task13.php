<!-- The "Product Catalog" (Associative Sorting)

Task: Create catalog.php.

Form: Input 3 Products (Name & Price).

Logic: Store them in an associative array ["Name" => Price].


Sort: Use asort() to sort them by Price (Low to High).

Display: A table showing the sorted list. Highlight the most expensive item in Yellow. -->

<!DOCTYPE html>
<html>
    <head>
        <title>Product Catalog</title>
        <style>
            body{
                font-family: 'Segoe UI', sans-serif;
                padding-top: 50px;
                text-align: center;
                font-size: 14px;
            }
            button {
                font-size: 18px;
                font-weight: bold;
                color: #ccc;
                background-color: #463192ff;
                padding: 5px;
                border-radius: 5px;
            }
            table {
                margin: 20px auto;
                border-collapse: collapse;
                width: 50%;
            }
            th, td {
                border: 1px solid #333;
                padding: 10px;
            }
            th {
                background-color: #333;
                color: #ffffff;
            }
            .expensive {
                background-color: #2057b7ff;
                font-weight: bold;
                color: #ffffff;
            }
        </style>
    </head>
    <body>
        <h2>Product Catalog</h2>
        <form method="post" acton="">
            <strong>Product 1:</strong>
            <input type="text" name="n1" placeholder="Name" required>
            <input type="number" name="p1" placeholder="Price" required>
            <br><br>

            <strong>Product 2:</strong>
            <input type="text" name="n2" placeholder="Name" required>
            <input type="number" name="p2" placeholder="Price" required>
            <br><br>

            <strong>Product 3:</strong>
            <input type="text" name="n3" placeholder="Name" required>
            <input type="number" name="p3" placeholder="Price" required>
            <br><br>

            <button type="submit">Sort & Display</button>
        </form>
        <br><br><hr>
        <?php
            if(isset($_POST['n1'])) {
                $n1 = $_POST['n1']; $p1 = $_POST['p1'];
                $n2 = $_POST['n2']; $p2 = $_POST['p2'];
                $n3 = $_POST['n3']; $p3 = $_POST['p3'];

                $catalog = [
                    $n1 => $p1,
                    $n2 => $p2,
                    $n3 => $p3
                ];

                asort($catalog);

                $highest_price = max($catalog);

                echo "<h3>Sorted Inventory:</h3>";
                echo "<table>";
                    echo "<tr>";
                        echo "<th>Product Name</th>";
                        echo "<th>Product Price</th>";
                    echo "</tr>";

                    foreach ($catalog as $name => $price){
                        $class = "";
                        if ($price == $highest_price){
                            $class = "expensive";
                        }
                        echo "<tr class=$class>";
                            echo "<td>$name</td>";
                            echo "<td>$price</td>";
                        echo "</tr>";
                    }
                echo "</table>";
            }
        ?>
    </body>
</html>