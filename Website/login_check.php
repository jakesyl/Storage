<?php
//TODO switch to postgres
$host="localhost"; // Host name 
$username="jakesyl"; // username 
$password="jake1998"; // password 
$db_name="test"; // DB name 
$tbl_name="members"; // Table name 

$conn_string = "host= " + localhost + "dbname= " + db_name + " user= " + username + " password = " + password;

// Connect to server and select databse.
pg_connect($conn_string) or die "can't connect";
// username and password sent from form 
$myusername=$_POST['myusername']; 
$mypassword=$_POST['mypassword']; 

// To protect MySQL injection (more detail about MySQL injection)
$myusername = stripslashes($myusername);
$mypassword = stripslashes($mypassword);
$myusername = mysql_real_escape_string($myusername);
$mypassword = mysql_real_escape_string($mypassword);
$sql="SELECT * FROM $tbl_name WHERE username='$myusername' and password='$mypassword'";
$result=mysql_query($sql);

// Mysql_num_row is counting table row
$count=mysql_num_rows($result);

// If result matched $myusername and $mypassword, table row must be 1 row
if($count==1){

// Register $myusername, $mypassword and redirect to file "login_success.php"
session_register("myusername");
session_register("mypassword"); 
header("location:success.php");
}
else {
echo "Wrong Username or Password";
}
?>