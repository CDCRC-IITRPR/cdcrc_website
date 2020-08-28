<?php
include "common.php";
session_start();
if(isset($_SESSION['userid'])){
	$sql = "DELETE FROM cdcrc_events WHERE event_id=".$_POST["event_id"];
	$con->query($sql);
	header("Location: admin.php");
}
else{
	header("Location: login.php");
}
?>