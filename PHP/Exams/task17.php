<!-- Form: Input "Account Number" and "Initial Balance".

Logic: Create class BankAccount.


Constructor: Use __construct($accNum, $balance) to set values immediately.


Destructor: Use __destruct() to echo "Account [Num] Closed" at the bottom of the page.

Display: Show the account details. -->

<!DOCTYPE html>
<html>
    <head>
        <title>Bank OOP</title>
        <style>
            body {
                padding-top: 50px;
                text-align: center;
                font-family: 'Segoe UI', sans-serif;
                font-size: 14px;
            }
            .card {
                border: 2px solid #2ecc71;
                background-color: #eafaf1;
                padding: 20px;
                width: 300px;
                margin: 20px auto;
                border-radius: 10px; 
            }
            .closed {
                color: white;
                background-color: #ff4f4fff;
                padding: 10px;
                margin-top: 20px;
                border-radius: 5px;
                display: inline-block;
            }
        </style>
    </head>
    <body>
        <h2>Bak Account Manager</h2>
        <form method="post" action="">
            Account number: <input type="text" name="acc_num" placeholder="ACC_101" required><br><br>
            Initial Balance: <input type="number" name="balance" placeholder="50000" required><br><br>
            <button type="submit">Open Account</button><br><br>
        </form>
        <hr>
        <br>

        <?php
            class BankAccount {
                public $acc_num;
                public $balance;
                
                public function __construct($n, $b) {
                    $this->acc_num = $n;
                    $this->balance = $b;
                }

                public function display() {
                    return "<strong>Account: </strong>$this->acc_num <br><strong>Balance: </strong>$this->balance";
                }

                public function __destruct() {
                    echo "<br><div class='closed'>Session ended. Account [$this->acc_num] Connection Closed.</div>";
                }
            }

            if(isset($_POST['acc_num'])) {
                $myBank = new BankAccount( $_POST['acc_num'], $_POST['balance']);

                echo "<div class='card'>";
                    echo "<h3>Account Active</h3>";
                    echo $myBank->display();
                echo "</div>";
            }
        ?>
    </body>
</html>
