<?php
include "common.php";
session_start(); 

if(isset($_SESSION['userid'])){
	echo "<a href=\"logout.php\">Log out</a>";
	echo "<h1>Events</h1>";
	if($_SESSION['userid']=="admin") $sql = "SELECT * FROM cdcrc_events ORDER BY event_id DESC";
	else $sql = "SELECT * FROM cdcrc_events WHERE type=\"".$_SESSION['userid']."\" ORDER BY event_id DESC";
	$result = $con->query($sql);
	echo "<table style=\"border: 1px solid black;\">";
	echo "<tr>
    <th style=\"border: 1px solid black;\">Event Id</th>
    <th style=\"border: 1px solid black;\">Display Text</th> 
    <th style=\"border: 1px solid black;\">Link</th>
    <th style=\"border: 1px solid black;\">Type</th>
  </tr>";
	if ($result->num_rows > 0) {
	    while($row = $result->fetch_assoc()) {
	    	echo "<tr>
	    	<td style=\"border: 1px solid black;\">".$row["event_id"]."</td>
	    	<td style=\"border: 1px solid black;\">".$row["display_text"]."</td>
	    	<td style=\"border: 1px solid black;\">".$row["link"]."</td>
	    	<td style=\"border: 1px solid black;\">".$row["type"]."</td>
	    	</tr>";
	    }
	} else {
	    echo "<tr><td>No Events Found</td></tr>";
	}
	echo "</table><br>";
	echo "<form action=\"addevent.php\" method=\"POST\">
  Display Text:
  <input type=\"text\" name=\"display_text\">
  Link:
  <input type=\"text\" name=\"link\">
  <input type=\"submit\" value=\"Add event\">
</form>";
	echo "<form action=\"deleteevent.php\" method=\"POST\">
  Event Id:
  <input type=\"text\" name=\"event_id\">
  <input type=\"submit\" value=\"Delete event\">
</form><br>";
	
	echo "<h1>News</h1>";
	if($_SESSION['userid']=="admin") $sql = "SELECT * FROM cdcrc_news ORDER BY news_id DESC";
	else $sql = "SELECT * FROM cdcrc_news WHERE type=\"".$_SESSION['userid']."\" ORDER BY news_id DESC";
	$result = $con->query($sql);
	echo "<table style=\"border: 1px solid black;\">";
	echo "<tr>
    <th style=\"border: 1px solid black;\">News Id</th>
    <th style=\"border: 1px solid black;\">Display Text</th> 
    <th style=\"border: 1px solid black;\">Link</th>
    <th style=\"border: 1px solid black;\">Type</th>
  </tr>";
	if ($result->num_rows > 0) {
	    while($row = $result->fetch_assoc()) {
	    	echo "<tr>
	    	<td style=\"border: 1px solid black;\">".$row["news_id"]."</td>
	    	<td style=\"border: 1px solid black;\">".$row["display_text"]."</td>
	    	<td style=\"border: 1px solid black;\">".$row["link"]."</td>
	    	<td style=\"border: 1px solid black;\">".$row["type"]."</td>
	    	</tr>";
	    }
	} else {
	    echo "<tr><td>No News Found</td></tr>";
	}
	echo "</table><br>";
	echo "<form action=\"addnews.php\" method=\"POST\">
  Display Text:
  <input type=\"text\" name=\"display_text\">
  Link:
  <input type=\"text\" name=\"link\">
  <input type=\"submit\" value=\"Add News\">
</form>";
	echo "<form action=\"deletenews.php\" method=\"POST\">
  News Id:
  <input type=\"text\" name=\"news_id\">
  <input type=\"submit\" value=\"Delete News\">
</form>";
}
else{
	header("Location: login.php");
}
?>