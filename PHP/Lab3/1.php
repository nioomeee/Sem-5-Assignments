<!-- 1 Create form for following using form and table tag. (call on same page) -->
<!DOCTYPE html>
    <head>
        <title>Addition Form</title>
    </head>
    <body>
        <form method="POST">
            <table>
                <tr>
                    <td>
                        <label for="num1">Enter the 1st number: </label>
                    </td>
                    <td>
                        <input type="number" name="num1" required>
                    </td>
                </tr>

                <tr>
                    <td>
                        <label for="num2">Enter the 2nd number: </label>
                    </td>
                    <td>
                        <input type="number" name="num2" required>
                    </td>
                </tr>

                <tr>
                    <td colspan='2'>
                        <input type="submit" value="ADD" name="submit">
                    </td>
                </tr>

                <tr>
                    <td>
                        <label for="result">Sum= </label>
                    </td>
                    <td>
                        <input type="text" readonly value = "<?php 
                                if(isset($_POST['submit'])) {
                                    $a = $_POST['num1'];
                                    $b = $_POST['num2'];

                                    echo $a + $b;
                                }
                            ?>"
                        >
                    </td>
                </tr>
            </table>
        </form>
    </body>
</html>