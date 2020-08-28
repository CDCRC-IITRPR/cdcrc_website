<?php 
include "common.php";
?>
<!DOCTYPE html>
<html lang="en">
<head>
<title>Gallery | IIT Ropar</title>
<link rel="shortcut icon" href="images/iitlogo.png" />
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="description" content="Course Project">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="styles/bootstrap4/bootstrap.min.css">
<link href="plugins/fontawesome-free-5.0.1/css/fontawesome-all.css" rel="stylesheet" type="text/css">
<link rel="stylesheet" type="text/css" href="styles/courses_styles.css">
<link rel="stylesheet" type="text/css" href="styles/courses_responsive.css">
</head>
<body>

<div class="super_container">

	<!-- Header -->

	<header class="header d-flex flex-row">
		<div class="header_content d-flex flex-row align-items-center">
			<!-- Logo -->
			<div class="logo_container">
				<div class="logo">
					<img src="images/iitlogo.png" alt="" height="50" width="50">
					<span>IIT Ropar</span>
					<div class="cdcrc"><h3 style="color: #FFFFFF;"></h3></div>
				</div>
			</div>

			<!-- Main Navigation -->

<nav class="main_nav_container">
				<div class="main_nav">
					<ul class="main_nav_list">
						<li class="main_nav_item dropdown">
							<a href="index.php" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">home</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="corporate.php">Home</a>
                                <a class="dropdown-item" href="index.php">CDCRC Home</a>
                            </div>
						</li>
						<li class="main_nav_item dropdown">
							<a href="index.php" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">Industrial</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="#">Consultancy</a>
                                <a class="dropdown-item" href="#">Membership</a>
                            </div>
						</li>
						<li class="main_nav_item"><a href="#">Sponsored Research</a></li>
						<li class="main_nav_item"><a href="#">Central Lab Facility</a></li>
						<!--<li class="main_nav_item"><a class="nav-link" href="#">Departments</a></li>-->
						<li class="main_nav_item"><a href="#">Research Domains</a></li>
					</ul>
				</div>
			</nav>
		</div>
		<div class="header_side d-flex flex-row justify-content-center align-items-center">
			<img src="images/phone-call.svg" alt="">
			<span>+91 78142 52244</span>
		</div>

		<!-- Hamburger -->
		<div class="hamburger_container">
			<i class="fas fa-bars trans_200"></i>
		</div>

	</header>
	
	<!-- Menu -->
	<div class="menu_container menu_mm">

		<!-- Menu Close Button -->
		<div class="menu_close_container">
			<div class="menu_close"></div>
		</div>

		<!-- Menu Items -->
		<div class="menu_inner menu_mm">
			<div class="menu menu_mm">
				<ul class="menu_list menu_mm">
                                        <li class="menu_item menu_mm dropdown">
							<a href="index.php" class="dropdown-toggle" id="navbardrop" data-toggle="dropdown">Home</a>
							<div class="dropdown-menu">
								<a class="dropdown-item" href="corporate.php">Home</a>
                                <a class="dropdown-item" href="index.php">CDCRC Home</a>
                            </div>
						</li>
						<li class="menu_item menu_mm dropdown">
							<a href="#" class=" dropdown-toggle" id="navbardrop" data-toggle="dropdown">Industrial</a>
                            <div class="dropdown-menu">
							<a class="dropdown-item" href="#">Consultancy</a>
                                <a class="dropdown-item" href="#">Membership</a>
                            </div>
						</li>
						<li class="menu_item menu_mm"><a href="recruiters.php">Sponsored Research</a></li>
						<li class="menu_item menu_mm"><a href="placementsummary.php">Central Lab Facility</a></li>
						<li class="menu_item menu_mm"><a href="contacts.php">Research Domain</a></li>
                                        
						</ul>

				<!-- Menu Social -->
				
				<div class="menu_social_container menu_mm">
					<ul class="menu_social menu_mm">
						<!--<li class="menu_social_item menu_mm"><a href="#"><i class="fab fa-pinterest"></i></a></li>-->
						<li class="menu_social_item menu_mm"><a target="_blank" href="https://in.linkedin.com/company/placementcelliitropar"><i class="fab fa-linkedin-in"></i></a></li>
						<li class="menu_social_item menu_mm"><a target="_blank" href="https://www.youtube.com/channel/UCvAgHSpVV8yfmu75OFBbomA"><i class="fab fa-youtube"></i></a></li>
						<li class="menu_social_item menu_mm"><a target="_blank" href="https://www.facebook.com/Career-Development-Corporate-Relations-Center-IIT-Ropar-169217773601805/"><i class="fab fa-facebook-f"></i></a></li>
						<li class="menu_social_item menu_mm"><a target="_blank" href=""><i class="fab fa-twitter"></i></a></li>
					</ul>
				</div>

			</div>

		</div>
		<div class="menu_copyright menu_mm">Colorlib All rights reserved</div>
	</div>
	
	<!-- Home -->

	<div class="home">
		<div class="home_background_container prlx_parent">
			<div class="home_background prlx" style="background-image:url(images/professional.jpeg)"></div>
		</div>
		<div class="home_content">
			<h1>Gallery</h1>
		</div>

	</div>
			<?php
				echo "<marquee style=\"color: #FFFFFF; background: #21618C;\" onMouseOver=\"this.stop()\" onMouseOut=\"this.start()\"><h3>";
				$sql = "SELECT * FROM cdcrc_events WHERE type=\"pd\" ORDER BY event_id DESC";
				$result = $con->query($sql);

				if ($result->num_rows > 0) {
				    while($row = $result->fetch_assoc()) {
				    	echo "|&nbsp; <a href=\"".$row["link"]."\" style=\"color: #FFFFFF\">".$row["display_text"]."</a>&nbsp;";    
				    }
				    echo "&nbsp;|";
				} else {
				    echo "<a href=\"#\" style=\"color: #FFFFFF\">No Events</a>";
				}
				echo "</h3></marquee>";
			?>
	<!-- Popular -->

	<div class="popular page_section">
		<div class="container">
			<div class="row" style="color: #000000;">
				  <div class="card col-md-8 col-sm-12">
				  
					<div>
                        <h1><i class="fas fa-angle-right"></i> &nbsp;Corporate Relations Gallery</h1>
                        &nbsp;
						
						
					<div id="imgGallary1" style="position:relative;width:300px;height:300px;border-radius:5px;border:1px solid black;overflow:hidden;display: block;margin-left: auto;margin-right: auto;width: 50%;">
						<img src="images/galleryimages/2.jpg" alt="" width="100%" height="100%" />
						<img src="images/galleryimages/3.jpg" alt="" width="100%" height="100%" />
						<img src="images/galleryimages/7.jpg" alt="" width="100%" height="100%" />
					</div>
					<script>
					(function(){
							var imgLen = document.getElementById('imgGallary1');
							var images = imgLen.getElementsByTagName('img');
							var counter = 1;

							if(counter <= images.length){
								setInterval(function(){
									images[0].src = images[counter].src;
									console.log(images[counter].src);
									counter++;

									if(counter === images.length){
										counter = 1;
									}
								},2000);
							}
					})();
					</script>
					</div>
                        <br><br>

                    <div id="imgGallary2" style="position:relative;width:300px;height:300px;border-radius:5px;border:1px solid black;overflow:hidden;display: block;margin-left: auto;margin-right: auto;width: 50%;">
						<img src="images/galleryimages/4.jpg" alt="" width="100%" height="100%" />
						<img src="images/galleryimages/5.jpg" alt="" width="100%" height="100%" />
						<img src="images/galleryimages/6.jpg" alt="" width="100%" height="100%" />
					</div>
					<script>
					(function(){
							var imgLen = document.getElementById('imgGallary2');
							var images = imgLen.getElementsByTagName('img');
							var counter = 1;

							if(counter <= images.length){
								setInterval(function(){
									images[0].src = images[counter].src;
									console.log(images[counter].src);
									counter++;

									if(counter === images.length){
										counter = 1;
									}
								},2000);
							}
					})();
					</script>
                    <br><br>
                    <div id="imgGallary3" style="position:relative;width:300px;height:300px;border-radius:5px;border:1px solid black;overflow:hidden;display: block;margin-left: auto;margin-right: auto;width: 50%;">
						<img src="images/galleryimages/10.jpg" alt="" width="100%" height="100%" />
						<img src="images/galleryimages/11.jpg" alt="" width="100%" height="100%" />
						<img src="images/galleryimages/12.jpg" alt="" width="100%" height="100%" />
					</div>
					<script>
					(function(){
							var imgLen = document.getElementById('imgGallary3');
							var images = imgLen.getElementsByTagName('img');
							var counter = 1;

							if(counter <= images.length){
								setInterval(function(){
									images[0].src = images[counter].src;
									console.log(images[counter].src);
									counter++;

									if(counter === images.length){
										counter = 1;
									}
								},2000);
							}
					})();
					</script>
			
					
					
                            </div>
                                 <div class="col-md-4 col-sm-12">
                                 	<div class="col-md-12">
                                 		<!-- News -->
                            			<div style="max-height:300px;overflow-y:scroll;padding-right:16px;padding-bottom:30px;">
                            				<h2 style="padding-bottom:10px;"><i class="fa fa-list-alt"></i> &nbsp;Recent News</h2>
                            				<ul>
                            					<?php
                            						$sql = "SELECT * FROM cdcrc_news WHERE type=\"pd\" ORDER BY news_id DESC";
													$result = $con->query($sql);
													if ($result->num_rows > 0){
														while($row = $result->fetch_assoc()){
															echo "<li><a href=\"".$row["link"]."\" style=\"color: #000000;\" onmouseover=\"this.style.color='#21618C'\" onmouseout=\"this.style.color='#000000'\"><h3><i class=\"fas fa-angle-right\"></i> &nbsp;".$row["display_text"]."</h3></a></li>";
														}
													}
                            					?>
                            				</ul>
                            			</div>
                            			<!-- Quick Links -->
                            			<div class="row">
                            			     <div class="col-sm-6 col-md-12">
                            				<br>
                                			<h2 style="font-style:italic;"><i class="fas fa-external-link-alt"></i> &nbsp;Quick Links</h2>
                            			     </div>
                            			<!-- Reach Us -->
                                		     <div class="col-sm-6 col-md-12">
                                		     <br>
                                    	                  <h2 style="font-style:italic;"><i class="fas fa-envelope"></i> &nbsp;Quick Contacts</h2>
                                                                <br>
								<h3>HOD Placement and Internships:</h3>
								<h4 style="font-style:italic;">hod.placement@iitrpr.ac.in , 7814252244</h4>
                                                		<h3>HOD Corporate Relations: </h3>
								<h4 style="font-style:italic;">hod.cr@iitrpr.ac.in, 8427587779</h4>
                                                                <h3>HOD Professional Development:</h3>
								<h4 style="font-style:italic;"> hod.pd@iitrpr.ac.in</h4>
                                                                <h3>Placement and Corporate Relations Manager</h3>
								<h4 style="font-style:italic;"> subodh.sharma@iitrpr.ac.in,  8699020183</h4>
                                                                <h3>CDCRC Office: </h3>
								<h4 style="font-style:italic;">cdcrc.office@iitrpr.ac.in</h4>
                                                                <h3>IIT Ropar Corporate Relations Office: </h3>
								<h4 style="font-style:italic;">cr.office@iitrpr.ac.in</h4>





                                    	             </div>
                                                </div>
                                       </div>
                                      

                                                   
                              </div>
                        
                                 	</div>
                                 </div>
                        </div>
           
                       

                </div>
         </div>
   </div>
 </div>
 </div>
		
	
	<!-- Footer -->

	<?php include 'footer.php';?>

</div>

<script src="js/jquery-3.2.1.min.js"></script>
<script src="styles/bootstrap4/popper.js"></script>
<script src="styles/bootstrap4/bootstrap.min.js"></script>
<script src="plugins/greensock/TweenMax.min.js"></script>
<script src="plugins/greensock/TimelineMax.min.js"></script>
<script src="plugins/scrollmagic/ScrollMagic.min.js"></script>
<script src="plugins/greensock/animation.gsap.min.js"></script>
<script src="plugins/greensock/ScrollToPlugin.min.js"></script>
<script src="plugins/OwlCarousel2-2.2.1/owl.carousel.js"></script>
<script src="plugins/scrollTo/jquery.scrollTo.min.js"></script>
<script src="plugins/easing/easing.js"></script>
<script src="js/custom.js"></script>

</body>
</html>
