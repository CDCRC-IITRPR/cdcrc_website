<?php  
 $connect = mysqli_connect("localhost", "root", "", "test_db");  
 $number = count($_POST["name"]);
 if($number > 0)  
 {  
 	// $myfile = fopen("latex/new.txt", "w") or die("Unable to open file!");
      for($i=0; $i<$number; $i++)  
      {  
           if(trim($_POST["name"][$i] != ''))  
           {  
                // $sql = "INSERT INTO tbl_name(name) VALUES('".mysqli_real_escape_string($connect, $_POST["name"][$i])."')";  
                // mysqli_query($connect, $sql);  
           		// fwrite($myfile, $_POST["name"][$i]);
           		echo $i." ".$_POST["name"][$i]."
           		";
           }  
      }
	  // fclose($myfile);
      echo "Data Inserted";  
 }  
 else  
 {  
      echo "Please Enter Details";
 }  
 ?>