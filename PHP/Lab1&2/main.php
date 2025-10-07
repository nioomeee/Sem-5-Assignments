<!DOCTYPE html>
    <head>
        <title>Link second page</title>
    </head>
    <body>
        <?php 
            // using include
            include "header.php"; //if file is missing, PHP gives warning but script continues

            // using require
            require "header.php"; //if file is missing, PHP gives fatal error and stops execution

            echo "<p>This is the main content of the page.</p>"
        ?>
    </body>
</html>