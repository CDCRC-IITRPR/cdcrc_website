<?php 
include "common.php";
?>
<!DOCTYPE html>
<html lang="en">
<head>
<title>Professional Development | IIT Ropar</title>
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
					<div class="cdcrc"><h3 style="color: #FFFFFF;">Career Development and<br>Corporate Relations Centre</h3></div>
				</div>
			</div>

			<!-- Main Navigation -->
			<nav class="main_nav_container">
				<div class="main_nav">
					<ul class="main_nav_list">
						<li class="main_nav_item dropdown">
							<a href="index.php" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">home</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="professional.php">Home</a>
                                <a class="dropdown-item" href="index.php">CDCRC Home</a>
                            </div>
						</li>
						<li class="main_nav_item"><a href="lectseries.php" class="nav-link">Lecture Series</a></li>
						<li class="main_nav_item dropdown">
							<!-- <a href="#" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">opportunities</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="tnp.php">Job/Placement</a>
                                <a class="dropdown-item" href="#">UPSC</a>
                                <a class="dropdown-item" href="#">GATE</a>
                                <a class="dropdown-item" href="#">GRE/GMAT/CAT</a>
                            </div> -->
                            <a href="#" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">Resources</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="library.php">Library</a>
                                <a class="dropdown-item" href="ugresourses.php">For UG Students</a>
                                <a class="dropdown-item" href="gradresourses.php">For Graduate Students</a>
                            </div>
						</li>
						<li class="main_nav_item dropdown">
							<a href="index.php" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">Initiatives</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="internship.php">CDCRC Innovation Internship</a>
                                <a class="dropdown-item" href="rspr.php">Research Scholar Peer Learning</a>
                            </div>
						</li>
						<li class="main_nav_item"><a href="webpages.php" class="nav-link">Webpages</a></li>
					</ul>
				</div>
			</nav>
		</div>
		<div class="header_side d-flex flex-row justify-content-center align-items-center">
			<img src="images/envelope.svg">
			<span>hod.pd@iitrpr.ac.in</span>
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
							<a href="index.php" class=" dropdown-toggle" id="navbardrop" data-toggle="dropdown">Home</a>
							<div class="dropdown-menu">
                                <a class="dropdown-item" href="professional.php">Home</a>
                                <a class="dropdown-item" href="index.php">CDCRC Home</a>
                            </div>
						</li>
						<li class="menu_item menu_mm"><a href="lectseries.php">Lecture Series</a></li>
						<li class="menu_item menu_mm dropdown">
							<!-- <a href="#" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">opportunities</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="tnp.php">Job/Placement</a>
                                <a class="dropdown-item" href="#">UPSC</a>
                                <a class="dropdown-item" href="#">GATE</a>
                                <a class="dropdown-item" href="#">GRE/GMAT/CAT</a>
                            </div> -->
                            <a href="#" class=" dropdown-toggle" id="navbardrop" data-toggle="dropdown">Resources</a>
							<div class="dropdown-menu">
                                <a class="dropdown-item" href="library.php">Library</a>
                                <a class="dropdown-item" href="ugresourses.php">For UG Students</a>
                                <a class="dropdown-item" href="gradresourses.php">For Graduate Students</a>
                            </div>
						</li>
						<li class="menu_item menu_mm dropdown">
							<a href="index.php" class=" dropdown-toggle" id="navbardrop" data-toggle="dropdown">Initiatives</a>
							<div class="dropdown-menu">
                                <a class="dropdown-item" href="internship.php">CDCRC Innovation Internship</a>
                                <a class="dropdown-item" href="rspr.php">Research Scholar Peer Learning</a>
                            </div>
						</li>
						<li class="menu_item menu_mm"><a href="webpages.php">Webpages</a></li>

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
			<h1>Professional Development</h1>
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
				  <div class="col-md-8 col-sm-12">
				  	<div>
                        <h1><i class="fas fa-angle-right"></i> &nbsp;Professional Development at IIT Ropar</h1>
                        &nbsp;<h2 style="padding-left: 1em;">Professional Development in IIT Ropar caters to the following needs for the IIT Ropar student community:</h2>
                        <ul style="list-style-type:disc;">
                        	<li><p style="font-size:170%; color:black;padding-left: 1em;">Facilitating discovery of potential, interests and aptitudes (self-discovery).</p></li>
                        	<li><p style="font-size:170%; color:black;padding-left: 1em;">Organizing opportunities for students on developing effective communication skills (e.g. resumes, group discussions and interviews) and gearing them up for lifelong learning.</p></li>
                        	<li><p style="font-size:170%; color:black;padding-left: 1em;">Organizing speaking opportunities and workshops by professionals (e.g. IIT alumni, faculty, Human Resource Professionals, Entrepreneurs, Industries, Research Organizations-Domestic and International) who are interested in inspiring and enabling achievement-oriented and talented IIT Ropar students.</p></li>
                        	<li><p style="font-size:170%; color:black;padding-left: 1em;">Recommending and developing resources for professional development (e.g. library development, peer-learning initiatives, adult learning)  for the future scientific and technical workforce.</p></li>
                        </ul>
                        
                                 
					</div>
					&nbsp;
					<div>
                        <h1><i class="fas fa-angle-right"></i> &nbsp;Learning Community</h1>
                        &nbsp;
                        
						
						
					<div id="imgGallary1" style="position:relative;width:600px;height:600px;border-radius:5px;border:1px solid black;overflow:hidden;display: block;margin-left: auto;margin-right: auto;width: 100%;">
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/cdcrc1.png" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/Learning-Community-IAS.jpg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/cdcrc1.png" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/Learning-Community-IAS.jpg" alt="" width="100%" height="100%" />
					</div>
					<p align="justify" style="font-size:170%; color:black;">At the suggestion of Mr. Subodh Sharma, Placement and Corporate Relations Centre students were encouraged to begin a “Learning Community”. A Learning Community is a student-led study group where initial encouragement is provided by Professional Development @IIT Ropar through a small development grant in the form of support for books periodicals.<br>
The philosophy behind a “Learning Community” is to help students achieve their dreams and aspirations which may not be addressed through a typical placement activity in a technology school. The Learning Communities are useful to address career options like preparation for management and serving the country through Administrative and Defence Services. We encourage students for ideas and interested personnel to get in touch with us for participation in panel discussion or sessions.
						</p>
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
					
					
					&nbsp;
					<div>
                        <h1><i class="fas fa-angle-right"></i> &nbsp;Bridging Connections</h1>
                        &nbsp;
					
					<div id="imgGallary2" style="position:relative;width:600px;height:600px;border-radius:5px;border:1px solid black;overflow:hidden;display: block;margin-left: auto;margin-right: auto;width: 100%;">
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/NID-Ahmedabad.jpg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/American-Center-Interaction-3.jpg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/IIM-Ahmedabad-1.jpg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/Nandu-Nandkishore.jpeg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/LeanIn.png" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/Toastmasters-IIT-Ropar-1.jpg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/Invest-India-1.jpeg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/Ankush-Khera.png" alt="" width="100%" height="100%" />
					</div>
				<p align="justify" style="font-size:170%; color:black;">An important aspect of Professional Development @ IIT Ropar is to bridge connections between IIT Ropar and institutions. In association with the Corporate Relations section we strive to identify learning opportunities between organizations and IIT Ropar. These learning opportunities could be in the form of supporting organizations of professional interest (e.g. Lean-In, Toastmasters and Society for Women Engineers: planned for 2018-19) to visiting academic and research institutions to learn and engage from the best and share with our community.</p>
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
					</div>
					
					&nbsp;
					<div>
                        <h1><i class="fas fa-angle-right"></i> &nbsp;Enhancing Student Mobility</h1>
                        &nbsp;
					
					<div id="imgGallary3" style="position:relative;width:600px;height:600px;border-radius:5px;border:1px solid black;overflow:hidden;display: block;margin-left: auto;margin-right: auto;width: 100%;">
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/FIPI-Women-In-Energy-2018-1.jpg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/Young-Thinkers-Conference-2018.jpg" alt="" width="100%" height="100%" />
						<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/CII-Manufacturing-Excellence.jpg" alt="" width="100%" height="100%" />
					</div>
					<p align="justify" style="font-size:170%; color:black;">The Professional Development section of the Career Development and Corporate Relations Centre is working continually on connecting students to best available opportunities beyond the rich academic environment of IIT Ropar. In 2018, our students have participated in various initiatives ranging from representing their research in industry forums to sharing their opinion on issues of global and national importance. At IIT Ropar we always encourage interested organizations to share opportunities where our talented students could showcase their potential.</p>

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
								<h4 style="font-style:italic;"> placement@iitrpr.ac.in,  8699020183</h4>
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
