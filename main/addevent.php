<?php
include "common.php";
session_start();
if(isset($_SESSION['userid'])){
	if($_SESSION['userid']=="tnp") $sql = "INSERT INTO cdcrc_events(display_text,link,type) VALUES(\"".$_POST["display_text"]."\",\"".$_POST["link"]."\",\"tnp\")";
	if($_SESSION['userid']=="pd") $sql = "INSERT INTO cdcrc_events(display_text,link,type) VALUES(\"".$_POST["display_text"]."\",\"".$_POST["link"]."\",\"pd\")";
	if($_SESSION['userid']=="cr") $sql = "INSERT INTO cdcrc_events(display_text,link,type) VALUES(\"".$_POST["display_text"]."\",\"".$_POST["link"]."\",\"cr\")";
	if($_SESSION['userid']=="admin") $sql = "INSERT INTO cdcrc_events(display_text,link,type) VALUES(\"".$_POST["display_text"]."\",\"".$_POST["link"]."\",\"cdcrc\")";
	$con->query($sql);
	header("Location: admin.php");
}
else{
	header("Location: login.php");
}
?>