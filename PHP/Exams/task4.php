<!-- The "Stat Calculator" (Return Values)  Create a webpage stats.php with a form taking two numbers.

Define a function calculateStats($n1, $n2) in a separate PHP block.

The function should return an Array containing: The Sum, The Difference, and The Product.

Display these 3 values in a formatted Result Box on the page. -->

<!DOCTYPE html>
<head>
    <title>Stat Calculator</title>
</head>

<body style = 'font-family: "sans-serif";'>
    <h2> Enter details: </h2>
    <form method = "post" action="stats.php">
        <label>Enter number 1: </label>
        <input type="number" required name="num1"> <br><br>
        <label>Enter number 2: </label>
        <input type="number" required name="num2"> <br><br>

        <button type="submit">Calculate</button>
    </form>
</body>
</html>