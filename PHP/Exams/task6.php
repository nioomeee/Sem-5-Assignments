<!DOCTYPE html>
<head>
    <title>String operations</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            padding: 20px;
        }
        table {
            border-collapse: collapse;

        }
        td {
            padding: 8px;
            border: 1px solid #ddd;
        }
    </style>
</head>
    <form method="post">
        <table>
            <tr>
                <td><label>1. Enter a sentence:</label></td>
                <td><textarea name="main_text" rows="3" placeholder="Type a long sentence here"></textarea></td>
            </tr>
            <tr>
                <td><label>2. Search for a word:</label></td>
                <td><input type="text" name="search" required></td>
            </tr>
            <tr>
                <td><label>3. Replace it with:</label></td>
                <td><input type="text" name="replace" required></td>
            </tr>
            <tr>
                <td colspan=2>
                    <button type="submit" name="analyze">Run operations</button>
                </td>
            </tr>
        </table>
    </form>

    <br><hr><br>

    <?php
        if(isset($_POST['analyze'])) {
            $raw = $_POST['main_text'];
            $search = $_POST['search'];
            $replace = $_POST['replace'];

            $clean = trim($raw);
            $len = strlen($clean);
            $words = str_word_count($clean);

            $position = strpos($clean, $search);
            $pos_msg = ($position === false)? "Not Found" : "Found at index: $position";

            $modified = str_replace($search, $replace, $clean);

            $sub_str = substr($clean, 0, 10) . "...";

            $upper = strtoupper($clean);
            $lower = strtolower($clean);
            $title = ucwords($clean);
            $first = ucfirst($clean);
            $rev = strrev($clean);
            $shuff = str_shuffle($clean);
            $md = md5($clean);

            $array_list = explode(" ", $clean);
        }
    ?>
    <h3>Analysis Report</h3>

    <table>
        <tr>
            <td>Original sentence</td>
            <td><?php echo $raw ?></td>
        </tr>
        <tr>
            <td>Cleaned sentence</td>
            <td><?php echo $clean ?></td>
        </tr>
        <tr>
            <td>Length of sentence</td>
            <td><?php echo $len ?></td>
        </tr>
        <tr>
            <td>Position of the searched word: </td>
            <td><?php echo $pos_msg ?></td>
        </tr>
        <tr>
            <td>Modified sentence</td>
            <td><?php echo $modified ?></td>
        </tr>
        <tr>
            <td>Substring</td>
            <td><?php echo $sub_str ?></td>
        </tr>
        <tr>
            <td>Upper Case</td>
            <td><?php echo $upper ?></td>
        </tr>
        <tr>
            <td>Lower Case</td>
            <td><?php echo $lower ?></td>
        </tr>
        <tr>
            <td>Title sentence</td>
            <td><?php echo $title ?></td>
        </tr>
        <tr>
            <td>First upper case</td>
            <td><?php echo $first ?></td>
        </tr>
        <tr>
            <td>Reversed sentence</td>
            <td><?php echo $rev ?></td>
        </tr>
        <tr>
            <td>Shuffled sentence</td>
            <td><?php echo $shuff ?></td>
        </tr>
        <tr>
            <td>Encrypted sentence</td>
            <td><?php echo $md ?></td>
        </tr>
        <tr>
            <td>Array list:</td>
            <td><?php print_r($array_list) ?></td>
        </tr>
    </table>
</html>