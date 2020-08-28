<?php
	if (isset($_POST["userid"]) && isset($_POST["password"])) {
		if(($_POST["userid"]=="admin" && $_POST["password"]=="12qwaszx")||($_POST["userid"]=="tnp" && $_POST["password"]=="12qwaszx")||($_POST["userid"]=="pd" && $_POST["password"]=="12qwaszx")||($_POST["userid"]=="cr" && $_POST["password"]=="12qwaszx")){
			session_start();
            $_SESSION['userid'] = $_POST["userid"];
            header("Location: admin.php");
		}
	}
?>
<form action="login.php" method="POST">
  Username:<br>
  <input type="text" name="userid"><br>
  Password:<br>
  <input type="password" name="password"><br>
  <input type="submit" value="Submit">
</form>