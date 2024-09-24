<?php
    require_once("includes1/db_connect1.php");
    include_once("templates1/header1.php");
    include_once("templates1/nav1.php");

    if(isset($_POST["send_message"])){
        $Model= mysqli_real_escape_string($conn, $_POST["Model"]);
        $Year = mysqli_real_escape_string($conn, $_POST["Year"]);
        $HorsePower = mysqli_real_escape_string($conn, $_POST["Horse Power"]);
        $Price= mysqli_real_escape_string($conn, $_POST["Price"]);

        $insert_message = "INSERT INTO messages (Model, Year, Horse Power, price) VALUES ('$Model', '', '$year', '$HorsePower','$Price')";
        
        if ($conn->query($insert_message) === TRUE) {
            header("Location: products1.php");
            exit();
        } else {
            echo "Error: " . $insert_message . "<br>" . $conn->error;
        }
    }
?>

<div class="header">
    <h1>Tesla</h1>
</div>

        
<div class="row">
    <div class="content">
    <h1>Talk To Us</h1>
    <form action="<?php print htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="POST" class="contact_form">
        <label for="Fn">Fullname:</label><br>
        <input type="text" name="fullname" id="Fn" placeholder="Fullname" required><br><br>

        <label for="email">Email Address:</label><br>
        <input type="email" id="email" name="email_address" placeholder="Email address" required><br><br>
        
        
        </select>
        <br><br>
    <label for="ms">Comment:</label><br>
    <textarea cols="30" rows="7" name="message" id="ms" required></textarea><br><br>
    <input type="submit" name="send_message" value="Send Message" >
</form>
</div>
<img class="index2_img" src="image/Tesla1.jpg" style="float: right;">
        </div>      
<?php include_once("templates1/footer1.php");?>