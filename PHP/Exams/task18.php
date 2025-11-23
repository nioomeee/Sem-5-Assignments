<!-- Create shapes.php.

Logic:

Interface Drawable with method draw().

Class Circle implements Drawable. draw() prints "Drawing a Circle".

Class Square implements Drawable. draw() prints "Drawing a Square".

Execution: Put both objects in an array and loop through them calling $obj->draw() (Polymorphism). -->

<!DOCTYPE html>
<html>
    <head>
        <title>Polymorphism</title>
        <style>
            body{
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                padding-top: 50px;
                text-align: center;
            }
            .shape {
                border: 2px solid #333;
                padding: 15px;
                margin: 20px auto;
                width: 200px;
                border-radius: 5px;
                background-color: #f0f0f0;
                font-size: 18px;
                font-weight: bold;
                color: #6f00a2ff;
            }
        </style>
    </head>
    <body>
        <h2>Shapes Drawing</h2>
        <?php
            interface Drawable {
                public function draw();
            }

            class Circle implements Drawable {
                public function draw(){
                    return "Drawing a Circle.";
                }
            }

            class Square implements Drawable {
                public function draw(){
                    return "Drawing a Square.";
                }
            }

            $shapes = [
                new Circle(),
                new Square(),
                new Circle()
            ];

            echo "<h3>Processing shapes:</h3>";

            foreach ($shapes as $shape){
                echo "<div class='shape'>";
                    echo $shape->draw();
                echo "</div>";
            }
        ?>
    </body>
</html>