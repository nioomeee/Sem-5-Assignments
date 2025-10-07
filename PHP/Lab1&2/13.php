<!-- Create a PHP program that acts as a basic calculator. 
Use a form to input two numbers anda dropdown for operation (Add, Subtract, Multiply, Divide). 
Show the result on the samepage using POST. -->

<!DOCTYPE html>
    <head>
        <title>Basic calculator</title>
    </head>
    <body>
        <form method="POST">
            <table>
                <tr>
                    <td>
                        <label>1st number: </label>
                    </td>
                    <td>
                        <input type="number" name="num1" step="any" required>
                    </td>

                <tr>
                    <td>
                        <label>2nd number: </label>
                    </td>
                    <td>
                        <input type="number" name="num2" step="any" required>
                    </td>
                </tr>

                <tr>
                    <td>
                        <label>Operation </label>
                    </td>
                    <td>
                        <select name="operation">
                            <option value="sum">+</option>
                            <option value="sub">-</option>
                            <option value="mul">*</option>
                            <option value="div">/</option>
                        </select>
                    </td>
                </tr>

                <tr>
                    <td colspan='2'>
                        <input type="submit" value="Submit">
                    </td>
                </tr>
            </table>
        </form>

        <?php 
            if($_SERVER["REQUEST_METHOD"] == "POST") {
                $num1 = (float) $_POST["num1"];
                $num2 = (float) $_POST["num2"];
                $operation = $_POST["operation"];
                $result = "";

                switch ($operation) {
                    case "sum":
                        $result = $num1 + $num2;
                        break;

                    case "sub":
                        $result = $num1 - $num2;
                        break;

                    case "mul":
                        $result = $num1 * $num2;
                        break;
                    
                    case "div":
                        $result = $num1 / $num2;
                        break;

                    default:
                        $result = "Invalid operator!";
                }

                echo "<h3>Result = $result</h3>";
            }
        ?>
    </body>
</html>