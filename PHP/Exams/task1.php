<?php
    $grade = "";
    $total = 0;
    $avg = 0;
    $weekday = 0;
    $showResult = false;
    
    if(isset($_POST['submit_btn'])) {

        $math = $_POST['math'];
        $sci  = $_POST['sci'];
        $eng = $_POST['eng'];

        $day = $_POST['day'];
        
        $total = $math + $sci + $eng;
        $avg = $total / 3;
        
        if ($avg >= 80) {
            $grade = "A";
        } elseif ($avg >= 60) {
            $grade = "B";
        } elseif ($avg >= 40) {
            $grade = "C";
        } elseif ($avg >= 33) {
            $grade = "D";
        } else {
            $grade = "Fail";
        }

        switch($day) {
            case 1: 
                $weekday = "Sunday";
                break;
            case 2:
                $weekday = "Monday";
                break;
            case 3:
                $weekday = "Tuesday";
                break;
            case 4:
                $weekday = "Wednesday";
                break;
            case 5:
                $weekday = "Thursday";
                break;
            case 6:
                $weekday = "Friday";
                break;
            case 7:
                $weekday = "Saturday";
                break;
            default:
                $weekday = "Invalid day Number!";
        }

        $showResult = true;

    }
?>

<!DOCTYPE html>
<head>
    <title>Nested if-else and switch case</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: "#f4f4f9";
            display: flex;
            justify-content: center;
            padding-top: 50px;
        } 
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            width: 500px;
        }
        h2{
            text-align: center;
            color: #333;
            border-bottom: 2px solid;
            padding-bottom: 10px;
        }

        table{
            width: 100%;
            border-collapse: collapse;
        }
        td{
            padding: 10px;
            vertical-align: middle;
        }
        input[type="number"]{
            width: 90%;
            padding:8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .btn{
            color: white:
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            width: 100%;
            cursor: pointer;
            font-size: 16px;
            background-color: #6c5ce7;
        }
        .btn:hover{
            background-color: #5a4ad1;
        }
    </style>
</head>

<body>
    <div class="container">
        <h3>Marks form</form>
        <form method = "post">
            <table>
                <tr>
                    <td><strong>Math marks: </strong></td>
                    <td><input type = "number" name="math" min = "0" max = "100" placeholder="0-100" required ></td>
                </tr>
                <tr>
                    <td><strong>Science marks: </strong></td>
                    <td><input type = "number" name="sci" min = "0" max = "100" placeholder="0-100" required ></td>
                </tr>
                <tr>
                    <td><strong>English marks: </strong></td>
                    <td><input type = "number" name="eng" min = "0" max = "100" placeholder="0-100" required ></td>
                </tr>
                <tr>
                    <td colspan="2"><hr></td>
                </tr>
                <tr>
                    <td><strong>Day Number (1-7):</strong></td>
                    <td><input type="number" name="day" min="0" max="7" placeholder="1-7" required></td>
                </tr>
                <tr>
                    <td colspan="2"><input type="submit" name="submit_btn" value="Generate Report" class = "btn"></td>
                </tr>
            </table>
        </form>

        <?php if($showResult) { ?>

            <div class = "result">
                <h3>Analysis Report:</h3>

                <table style="width: 100%">
                    <tr>
                        <td>Total marks:</td>
                        <td><strong><?php echo $total; ?> / 300</strong></td>
                    </tr>
                    <tr>
                        <td>Percentage</td>
                        <td><strong><?php echo number_format($avg, 2); ?>%</strong></td>
                    </tr>
                    <tr>
                        <td>Grade:</td>
                        <td><?php echo $grade; ?></td>
                    </tr>
                    <tr>
                        <td>Today is: </td>
                        <td><strong><?php echo $weekday; ?></strong></td>
                    </tr>
                </table>
            </div>

        <?php } ?>
    </div>
</body>

</html>