<!-- Form: Input Brand, Model, and Year.

Logic: Create a class Car with attributes $brand, $model, $year.


Method: Add a method displayInfo() that returns a formatted string.

Execution: Create an object from the form data and call displayInfo(). -->

<!DOCTYPE html>
<html>
    <head>
        <title>Car</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                padding-top: 50px;
                text-align: center;
            }
            .car-card {
                border: 2px solid #333;
                border-radius: 10px;
                padding: 20px;
                width: 300px;
                margin: 20px auto;
                background-color: #f9f9f9;
                box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.1);
            } 
            h3 {
                margin-top: 0;
                color: #2c3e50;
            }
        </style>
    </head>
    <body>
        <form method="post" action="">
            <label>Car brand: </label>
            <input type="text" name="brand" required>
            <br><br>
            <label>Car model: </label>
            <input type="text" name="model" required>
            <br><br>
            <label>Car year: </label>
            <input type="text" name="year" required>
            <br><br>
            <button type="submit">Build Car</button>
        </form>
        <br><br><hr><br>

        <?php
            class Car {
                public $brand;
                public $model;
                public $year;

                public function displayInfo() {
                    echo "This is a <strong>$this->year $this->brand $this->model</strong>.";
                }
            }

            if(isset($_POST['brand'])) {

                $myCar = new Car();

                $myCar->brand = $_POST['brand'];
                $myCar->model = $_POST['model'];
                $myCar->year = $_POST['year'];

                echo "<div class = 'car-card'>";
                    echo "<h3>Car Created!</h3>";
                    echo $myCar->displayInfo();
                echo "</div>";
            }
        ?>
    </body>
</html>