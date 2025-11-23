<!-- Logic:

Class MathOps.

Constant PI = 3.14159.

Static Method calculateArea($radius).

Execution: Call MathOps::calculateArea(5) without creating an object (new MathOps). -->

<!DOCTYPE html>
<html>
    <head>
        <title>Static Math Ops</title>
        <style>
            body{
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
                padding-top: 50px;
                text-align: center;
            }
            .result-box {
                padding: 20px;
                margin: 20px auto;
                border: 2px solid #333;
                background-color: #f0f0f0;
                font-weight: 18px;
                font-weight: bold;
                color: #432affff;
                width: 200px;
            }

        </style>
    </head>
    <body>
        <h2>Static calculator</h2>

        <?php
            class MathOps {
                const PI = 3.14159;

                public static function calculateArea($rad) {
                    $area = self::PI * $rad * $rad;
                    return $area;
                }
            }
        

            $radius = 5;
            $result = MathOps::calculateArea($radius);
        ?>

            <div class="result-box">
                Radius: <?php echo $radius; ?><br>
                Area: <?php echo $result; ?>
            </div>
    </body>
</html>