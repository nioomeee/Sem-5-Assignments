<!-- Form: Input a "New Fruit".

Logic: Start with an array ["Apple", "Banana"].


Push: Add the new fruit to the end using array_push().


Pop: Remove the last element using array_pop() and display which one was removed.


Merge: Create a second array ["Mango", "Grapes"] and merge it with the first using array_merge().

Display: print_r() the final array. -->

<!DOCTYPE html>
<html>
    <head>
        <title>Stack ops</title>
        <style>
            body {
                font-family: 'Courier New', monospace;
                font-size: 14px;
                padding-top: 50px;
                text-align: center;
            }
            .box {
                border: 1px solid #333;
                padding: 10px;
                margin-bottom: 10px;
                background: #f9f9f9;
            }
            h3 {
                margin-top: 0;
                color: #555;
            }

        </style>
    </head>
    <body>
        <h2>Fruit Stack Manager</h2>
        <form method="post" action="">
            <label>Add a new fruit: </label>
            <input type="text" name="new_fruit" placeholder="e.g., Orange" required><br><br>
            <button type="submit">Run Stack Operations</button>
        </form>
        <br><br><hr>
        <?php
            if(isset($_POST['new_fruit'])) {
                $input = $_POST['new_fruit'];
                $stack = ["Apple", "Banana"];
                // 1. initial array
                echo "<div class='box'><h3>1. Initial Array: </h3>". implode(", ", $stack) ."</div>";

                array_push($stack, $input);
                // 2. Push
                echo "<div class='box'><h3>2. Push(Add '$input')</h3>Result: ". implode(", ", $stack) ."</div>";

                // 3. Pop
                $popped = array_pop($stack);
                echo "<div class = 'box'><h3>3. Pop(Remove Last)</h3>";
                    echo "Removed item: $popped<br>";
                    echo "Result: " . implode(", ", $stack);
                echo "</div>";

                // 4. Unshift - add to start
                array_unshift($stack, $input);
                echo "<div class = 'box'><h3>4. Unshift(Add First)</h3>";
                    echo "Result: " . implode(", ", $stack);
                echo "</div>";

                // 5. SHIFT - Remove from start
                $shifted = array_shift($stack);
                echo "<div class = 'box'><h3>5. Shift(Remove First)</h3>";
                    echo "Removed item: $shifted<br>";
                    echo "Result: " . implode(", ", $stack);
                echo "</div>";

                // 6. MERGE - combine with other arrays
                $others = ["Mango", "Grapes"];
                $final = array_merge($stack, $others);
                echo "<div class = 'box'><h3>6. Merge(with Mango, Grapes)</h3>";
                    echo "Result: " . implode(", ", $final);
                echo "</div>";
            }
        ?>
    </body>
</html>

