<?php require_once("includes1/db_connect1.php");
//SELECT `Model`, `Year`, `Horse Power`, `Price` FROM `carinfo`
$select_car= "SELECT `Model`, `Year`, `Horse Power`, `Price` FROM `carinfo`";
$sel_car= $conn->query($select_car);
$cm=0;
if ($sel_car->num_rows > 0) {
  // output data of each row
  while($select_car= $sel_car->fetch_assoc()) {
    $cm++;
?>
        <tr>
            <td><?php print $cm; ?>.</td>
            <td><?php print $select_car["Model"]; ?></td>
            <td><?php print $select_car["Year"]; ?></td>
            <td><?php print '<strong>' . $select_car["Horse Power"]?></td>
            
           
        </tr>
<?php
  }
} else {
  echo "0 results";
}
?>