<?php
include "common.php";
session_start();
if(isset($_SESSION['userid'])){
	$sql = "DELETE FROM cdcrc_news WHERE news_id=".$_POST["news_id"];
	$con->query($sql);
	header("Location: admin.php");
}
else{
	header("Location: login.php");
}
?>