<!DOCTYPE html>
    <head>
        <title>Calculator</title>
        <style>
            body {
                font-family: "Times New Roman", serif;
                background-color: "#f0f0f0";
            }
            h2 {
                color: #0000ff;
            }
            table {
                background-color: #8a858577;
                padding: 15px;
            }
        </style>
    </head>

    <body>
        <?php 
            $result = "";
            if($_SERVER["REQUEST_METHOD"] == "POST") {
                $a = $_POST['num1'];
                $b = $_POST['num2'];

                if(isset($_POST['add'])) {
                    $result = $a + $b;
                } elseif (isset($_POST['sub'])) {
                    $result = $a - $b;
                } elseif (isset($_POST['mul'])) {
                    $result = $a * $b;
                } elseif (isset($_POST['div'])) {
                    if ($b == 0) {
                        $result = "Cannot divide by 0";
                    } else {
                        $result = $a / $b;
                    }
                }
            }
        ?>
        <form method="POST">
            <table>
                <h2> Form with multiple submit buttons</h2>
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
                        <label> Result: </label>
                    </td>
                    <td>
                        <input type="text" readonly value = "<?php 
                            echo $result;
                        ?>">
                    </td>
                </tr>

                <tr>
                    <td>
                        <input type="submit" value="Add" name="add">
                    </td>
                    <td>
                        <input type="submit" value="Subtract" name="sub">
                    </td>
                </tr>

                <tr>
                    <td>
                        <input type="submit" value="Multiply" name="mul">
                    </td>
                    <td>
                        <input type="submit" value="Divide" name="div">
                    </td>
                </tr>
            </table>
        </form>
    </body>
</html>