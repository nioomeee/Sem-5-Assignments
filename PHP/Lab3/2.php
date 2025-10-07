<!DOCTYPE html>
    <head>
        <title>School ID Registration Form</title>
    </head>
    <body>
        <form method="POST">
            <table cellpadding = "5" cellspacing = "0">
                <tr>
                    <th colspan='2'>
                        Name
                    </th>
                </tr>

                <tr>
                    <td>
                        <input type="text" name="fname" placeholder="First">
                    </td>
                    <td>
                        <input type="text" name="lname" placeholder="Last">
                    </td>                    
                </tr>

                <tr>
                    <th colSpan="2">Expected Year of Graduation</th>
                </tr>
                <tr>
                    <td colSpan="2"><input type="year" name="grad"></td>
                </tr>

                <tr>
                    <th colSpan="2">Address</th>
                </tr>
                <tr>
                    <td colSpan="2"><input type="text" name="addres1" placeholder="Street Address"></td>
                </tr>
                <tr>
                    <td colSpan="2"><input type="text" name="addres2" placeholder="Address Line 2"></td>
                </tr>


            </table>
        </form>
    </body>
</html>