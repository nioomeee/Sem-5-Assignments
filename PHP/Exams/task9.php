<!-- The "Bad Word" Filter Create censor.php.

Form: A <textarea> for a user comment.

Logic:

Define an array of "banned" words in your PHP (e.g., $banned = ["lazy", "boring", "bad"];).

Check if the user's comment contains any of these words.

Replace them with **** using str_replace.

Display: The "Clean Version" of their comment. -->

<!DOCTYPE html>
<html>
    <head>
        <title>Censoring</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                padding-top: 50px;
                text-align: center;
            }
            td {
                padding: 10px;
            }
            textarea {
                width: 300px;
                height: 100px;
                padding: 10px;
            }
            .result-box {
                background-color: #ffd26aff;
                color: #00856cff;
                border: 1px solid #ccc;
                padding: 20px;
                width: 300px;
                margin: 20px auto;
                border-radius: 8px;
                text-align: left;
            }
            .banned-msg {
                color: red;
                font-size: 12px;
            }
        </style>
    </head>
    <body>
        <h2>Leave comments</h2>
        <form method="post" action="">
            <table>
                <tr>
                    <td><label><strong>Leave your comments:</strong></label></td>
                    <td><textarea name="cmt" placeholder="The class was very boring and lazy" required></textarea></td>
                </tr>
                <tr>
                    <td colspan="2"><button type="submit">Post Comment</button></td>
                </tr>
            </table>
        </form>

        <?php 
            if (isset($_POST['cmt'])) {
                $raw_cmnt = $_POST['cmt'];
                $banned = ["lazy", "boring", "bad"];

                $clean = str_ireplace($banned, "***", $raw_cmnt);

                echo "<div class='result-box'>";
                    echo "<strong>Your posted comment:</strong><br><br>";
                    echo $clean;

                    echo "<br><br><hr><span class='banned-msg'>Filters applied for: " . implode(", ", $banned) . "</span>";
                echo "</div>";
            }
        ?>
    </body>
</html>