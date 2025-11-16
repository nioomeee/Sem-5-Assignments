<!-- Defintion: Checks if "php" exists in the text (i makes it case-insensitive). -->
<?php
    $pattern = "/php/i";
    
    $text1 = "Php is a programming language";
    echo "<br> Searching in string : {$text1}";

    if (preg_match($pattern, $text1)) {
        echo "<br>String contains PHP!";
    } else {
        echo "<br> String doesn't contain php!";
    }

    echo "<br>";
    $text2 = "I like Java more";

    echo "<br> Searching in string {$text2}:<br>";
    if (preg_match($pattern, $text2)) {
        echo "String conatins PHP!";
    } else {
        echo "String doesn't contain PHP!";
    }
?>