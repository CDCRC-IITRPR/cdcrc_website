<html>  
      <head>  
           <title>CV_maker</title>  
           <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />  
           <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>  
           <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>  
      </head>  
      <body>  
           <div class="container">  
                <br />  
                <br />  
                <h2 align="center">Enter your Details</h2>  
                <div class="form-group">  
                     <form name="add_name" id="add_name">
                     	<center>
                     	<input type="text" name="pname" placeholder="Enter your name" class="form-control name_list">
                     	</center>
                          <div class="table-responsive">  
                               <table class="table table-bordered" id="dynamic_field">
                               		<tr><td><h2>Section: Personal Data</h2></td>
                               		<td><button type="button" name="add" id="addsection" class="btn btn-success">Add More Section</button></td><td><button type="button" name="add" id="add" class="btn btn-success">Add More Fields</button></td>
                               		</tr>
                                    <tr>  
                                         <td><input type="text" name="name[]" placeholder="Enter detail" class="form-control name_list" /></td><td><input type="text" name="name[]" placeholder="Enter detail" class="form-control name_list" /></td>  
                                    </tr>  
                               </table>  
                               <input type="button" name="submit" id="submit" class="btn btn-info" value="Submit" />  
                          </div>  
                     </form>  
                </div>  
           </div>  
      </body>  
 </html>  
 <script>  
 $(document).ready(function(){  
      var i=2,j=500;
      var temp = [0];
      $('#add').click(function(){  
           i+=2;  
           $('#dynamic_field').append('<tr id="row'+i+'"><td><input type="text" name="name[]" placeholder="Enter detail" class="form-control name_list" /></td><td><input type="text" name="name[]" placeholder="Enter detail" class="form-control name_list" /></td></tr>');  
      });
      $('#addsection').click(function(){  
           j++; 
           temp.push(i+1); 
           i+=3;
           $('#dynamic_field').append('<tr id="row'+j+'"><td><h2>Section:</h2></td><td> <input type="text" name="name[]" placeholder="Enter Section Name" class="form-control name_list" /></tr>');  
           $('#dynamic_field').append('<tr id="row'+i+'"><td><input type="text" name="name[]" placeholder="Enter detail" class="form-control name_list" /></td><td><input type="text" name="name[]" placeholder="Enter detail" class="form-control name_list" /></td></tr>');
      });  
      $(document).on('click', '.btn_remove', function(){  
           var button_id = $(this).attr("id");   
           $('#row'+button_id+'').remove();  
      });  
      $('#submit').click(function(){
      		temp.push(i);
      		var data1 = $('#add_name').serializeArray();
            data1.push({name:'count',value:temp.length-1});
            data1.push({name:'temp',value: temp});
           $.ajax({  
                url:"latex.php",
                method:"POST",
                data:data1,
                success:function(data)
                {  
                     location.href = "view.php";
                }  
           });  
      });  
 });  
 </script>
