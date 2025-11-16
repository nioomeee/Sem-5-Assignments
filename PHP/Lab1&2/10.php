<!-- Create a php program and perform the followings:
• Create a link that sends your name and age to another page using the GET method.
• On the second page, display a greeting using the values passed in the URL. -->
<!DOCTYPE html>
    <head>
        <title>Link second page</title>
    </head>
    <body>
        <?php
            echo '<a href="page2.php?name=Niomi&age=19">Click here to send data</a>'
        ?>
    </body>
</html>