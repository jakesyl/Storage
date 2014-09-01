<?php

$host="localhost"; // Host name 
$username="jakesyl"; // username 
$password="jake1998"; // password 
$db_name="site_users"; // DB name 
$tbl_name="members"; // Table name 

$conn_string = "host= " + $localhost + "dbname= " + $db_name + " user= " + $username + " password = " + $password;

// Connect to server and select databse.
$conn =pg_connect($conn_string) or die "can't connect";
// username and password sent from form 
$name=$_POST['Name']; 
$address=$_POST['Address']; 
$pass=$_POST['Password']; 
$pass  = password_hash($pass, PASSWORD_DEFAULT);
$name = stripslashes($name);
$address = stripslashes($address);
$sql="INSERT INTO FROM $tbl_name VALUES '$Name' , '$Address', '$Password',";
$params = array(
    "$Name" => $name,
    "$tbl_name" => $tbl_name,
    "$Address" => $address
    "$Password" => $pass
);
$result = pg_prepare($conn, "insertion", $sql)
$result = pg_execute($conn, "insertion", $params)


?>