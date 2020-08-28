<?php 
include "common.php";
?>
<!DOCTYPE html>
<html lang="en">
<head>
<title>CDCRC | IIT Ropar</title>
<link rel="shortcut icon" href="images/iitlogo.png" />
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="description" content="CDCRC Website">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" type="text/css" href="styles/bootstrap4/bootstrap.min.css">
<link href="plugins/fontawesome-free-5.0.1/css/fontawesome-all.css" rel="stylesheet" type="text/css">
<link rel="stylesheet" type="text/css" href="plugins/OwlCarousel2-2.2.1/owl.carousel.css">
<link rel="stylesheet" type="text/css" href="plugins/OwlCarousel2-2.2.1/owl.theme.default.css">
<link rel="stylesheet" type="text/css" href="plugins/OwlCarousel2-2.2.1/animate.css">
<link rel="stylesheet" type="text/css" href="styles/main_styles.css">
<link rel="stylesheet" type="text/css" href="styles/responsive.css">
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
							<a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown" style="margin-left: 50px;">Home</a>
                            <div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="directordesk.php">From The Director's Desk</a>
                                <a class="dropdown-item" href="role.php">Role of CDCRC</a>
                                <a class="dropdown-item" href="structure.php">Structure of CDCRC</a>
                            </div>
                        </li>
						<li class="main_nav_item dropdown">
							<a href="#" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">For Companies</a>
                            <div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="tnp.php">Training & Placement</a>
                                <a class="dropdown-item" href="corporate.php">Corporate Relations</a>
                            </div>
						</li>
						<li class="main_nav_item dropdown">
							<a href="#" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">For Students</a>
                            <div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="professional.php">Professional Development</a>
                                <a class="dropdown-item" href="tnp.php">Training & Placement</a>
                            </div>
						</li>
						<li class="main_nav_item"><a href="cdcrcteam.php" class="nav-link">CDCRC Team</a></li>
					</ul>
				</div>
			</nav>
		</div>
		<div class="header_side d-flex flex-row justify-content-center align-items-center">
			<span>
				<a target="_blank" href="https://in.linkedin.com/company/placementcelliitropar" style="color: #FFFFFF; margin-right: 20px;" onmouseover="this.style.color='#FFD800'" onmouseout="this.style.color='#FFFFFF'"><i class="fab fa-linkedin-in"></i></a>
				<a target="_blank" href="https://www.facebook.com/Career-Development-Corporate-Relations-Center-IIT-Ropar-169217773601805/" style="color: #FFFFFF; margin-right: 20px;" onmouseover="this.style.color='#FFD800'" onmouseout="this.style.color='#FFFFFF'"><i class="fab fa-facebook-f"></i></a>
				<a href="#" style="color: #FFFFFF; margin-right: 20px;" onmouseover="this.style.color='#FFD800'" onmouseout="this.style.color='#FFFFFF'"><i class="fab fa-twitter"></i></a>
				<a target="_blank" href="https://www.youtube.com/channel/UCvAgHSpVV8yfmu75OFBbomA" style="color: #FFFFFF;" onmouseover="this.style.color='#FFD800'" onmouseout="this.style.color='#FFFFFF'"><i class="fab fa-youtube"></i></a>
			</span>
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
							<a class="dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown" style="margin-left: 50px;">Home</a>
                            <div class="dropdown-menu">
                                <a class="dropdown-item" href="directordesk.php">From The Director's Desk</a>
                                <a class="dropdown-item" href="role.php">Role of CDCRC</a>
                                <a class="dropdown-item" href="structure.php">Structure of CDCRC</a>
                            </div>
                        </li>
						<li class="menu_item menu_mm dropdown">
							<a href="#" class="dropdown-toggle" id="navbardrop" data-toggle="dropdown">For Companies</a>
                            <div class="dropdown-menu">
                                <a class="dropdown-item" href="tnp.php">Training & Placement</a>
                                <a class="dropdown-item" href="corporate.php">Corporate Relations</a>
                            </div>
						</li>
						<li class="menu_item menu_mm dropdown">
							<a href="#" class=" dropdown-toggle" id="navbardrop" data-toggle="dropdown">For Students</a>
                            <div class="dropdown-menu" >
                                <a class="dropdown-item" href="professional.php">Professional Development</a>
                                <a class="dropdown-item" href="tnp.php">Training & Placement</a>
                            </div>
						</li>
						<li class="menu_item menu_mm"><a href="cdcrcteam.php" class="nav-link">CDCRC Team</a></li>




					
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

		<!-- Hero Slider -->
		<div class="hero_slider_container">
			<div class="hero_slider owl-carousel">
				
				<!-- Hero Slide -->
				<div class="hero_slide">
					<div class="hero_slide_background" style="background-image:url(images/background/1.png)"></div>
					<div class="hero_slide_container d-flex flex-column align-items-center justify-content-center">
						<div class="hero_slide_content text-center">
							<h1 data-animation-in="fadeInUp" data-animation-out="animate-out fadeOut">Connecting <span>Talent</span> with <span>Opportunity</span></h1>
						</div>
					</div>
				</div>
				
				<!-- Hero Slide -->
				<div class="hero_slide">
					<div class="hero_slide_background" style="background-image:url(images/background/2.png)"></div>
					<div class="hero_slide_container d-flex flex-column align-items-center justify-content-center">
						<div class="hero_slide_content text-center">
							<h1 data-animation-in="fadeInUp" data-animation-out="animate-out fadeOut">Connecting <span>Talent</span> with <span>Opportunity</span></h1>
						</div>
					</div>
				</div>
				
				<!-- Hero Slide -->
				<div class="hero_slide">
					<div class="hero_slide_background" style="background-image:url(images/background/3.png)"></div>
					<div class="hero_slide_container d-flex flex-column align-items-center justify-content-center">
						<div class="hero_slide_content text-center">
							<h1 data-animation-in="fadeInUp" data-animation-out="animate-out fadeOut">Connecting <span>Talent</span> with <span>Opportunity</span></h1>
						</div>
					</div>
				</div>

				<div class="hero_slide">
					<div class="hero_slide_background" style="background-image:url(images/background/4.png)"></div>
					<div class="hero_slide_container d-flex flex-column align-items-center justify-content-center">
						<div class="hero_slide_content text-center">
							<h1 data-animation-in="fadeInUp" data-animation-out="animate-out fadeOut">Connecting <span>Talent</span> with <span>Opportunity</span></h1> 
						</div>
					</div>
				</div>

			</div>

			<div class="hero_slider_left hero_slider_nav trans_200"><span class="trans_200">prev</span></div>
			<div class="hero_slider_right hero_slider_nav trans_200"><span class="trans_200">next</span></div>
		</div>

	</div>

	<div class="hero_boxes">
		<div class="hero_boxes_inner">
			<div class="container">
				<div class="row">

					<div class="col-lg-4 hero_box_col">
						<div class="hero_box d-flex flex-row align-items-center justify-content-start">
							<img src="images/professional.svg">
							<div class="hero_box_content">
								<a href="professional.php">
								<h2 class="hero_box_title" style="padding-right: 10px;">Professional Development</h2>
								</a>
							</div>
						</div>
					</div>

					<div class="col-lg-4 hero_box_col">
						<div class="hero_box d-flex flex-row align-items-center justify-content-start">
							<img src="images/tnp.svg">
							<div class="hero_box_content">
								<a href="tnp.php">
								<h2 class="hero_box_title">Placement & Internships</h2>
								</a>
							</div>
						</div>
					</div>

					<div class="col-lg-4 hero_box_col">
						<div class="hero_box d-flex flex-row align-items-center justify-content-start">
							<img src="images/corporate.svg">
							<div class="hero_box_content">
								<a href="corporate.php">
								<h2 class="hero_box_title" style="padding-right: 20px;">Corporate Relations</h2>
								</a>
							</div>
						</div>
					</div>

				</div>
			</div>
			<?php
				echo "<marquee style=\"color: #FFFFFF; background: #21618C; margin-top: 25px;\" onMouseOver=\"this.stop()\" onMouseOut=\"this.start()\"><h3>";
				$sql = "SELECT * FROM cdcrc_events ORDER BY event_id DESC";
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
			
		</div>
		<!-- <h3 style="width:10%; display:inline-block; float: left; background: #FFFFFF; color: #21618C; padding-left: 10px;">Events:</h3><marquee style="color: #FFFFFF; background: #21618C; width:90%; display:inline-block; float: right;" onMouseOver="this.stop()" onMouseOut="this.start()"><h3>Events</h3></marquee> -->
	</div>

	<!-- Popular -->

	<div class="popular page_section">
		<div class="container">
			<div class="row" style="color: #000000;">
				  <div class="col-md-8 col-sm-12">
				  	<h1>About Career Development and Corporate Relations Centre</h1>
				  	<h2><i class="fas fa-angle-right"></i> &nbsp;IIT Ropar, through their Career Development and Corporate Relations Centre (CDCRC) aims at</h2>
				  	<ul style="list-style-type: disc;">
				  		<h2 style="padding-left: 1em;"><li>Giving its students a career orientation in terms of options they have, namely careers in the industry, academia, R&D, entrepreneurship, public service etc.</li></h2>
				  		<h2 style="padding-left: 1em;"><li>Organizing professional development activities</li></h2>
				  		<h2 style="padding-left: 1em;"><li>Familiarize students with industry expectations and other career alternatives</li></h2>
				  		<h2 style="padding-left: 1em;"><li>Helping students to discover their interest for leveraging opportunities provided through IIT Ropar which will help them launch themselves in careers that will maximize one's potential to excel.</li></h2>
				  		<h2 style="padding-left: 1em;"><li>Building close contacts with the Industry through their Corporate Relations Unit which will help the Institute become the most preferred campus for a variety of employers for campus recruitment and also in terms of interaction with the Institute faculty and for R&D facilities, Consultancy and Continuing Education and other Industry-Institute Interaction programmes.</li></h2>
				  	</ul>
                  </div>
                                 <div class="col-md-4 col-sm-12">
                                 	<div class="col-md-12">
                                 		<!-- News -->
                            			<div style="max-height:300px;overflow-y:scroll;padding-right:16px;padding-bottom:30px;">
                            				<h2 style="padding-bottom:10px;font-style:italic;"><i class="fa fa-list-alt"></i> &nbsp;Recent News</h2>
                            				<ul>
                            					<!-- <li><a href="#" style="color: #000000;" onmouseover="this.style.color='#21618C'" onmouseout="this.style.color='#000000'"><h3><i class="fas fa-angle-right"></i> &nbsp;News1</h3></a></li> -->
                            					<?php
                            						$sql = "SELECT * FROM cdcrc_news ORDER BY news_id DESC";
													$result = $con->query($sql);
													if ($result->num_rows > 0){
														while($row = $result->fetch_assoc()){
															echo "<li><a href=\"".$row["link"]."\" style=\"color: #000000;\" onmouseover=\"this.style.color='#21618C'\" onmouseout=\"this.style.color='#000000'\"><h3><i class=\"fas fa-angle-right\"></i> &nbsp;".$row["display_text"]."</h3></a></li>";
														}
													}
                            					?>
                            				</ul>
                            			</div>
                            			<br>
                                    	<h2><i class="fab fa-facebook-f" aria-hidden="true"></i>&nbsp;&nbsp;Facebook</h2>
                                    	<div class="fb-page" data-href="https://www.facebook.com/Career-Development-Corporate-Relations-Center-IIT-Ropar-169217773601805/" data-tabs="timeline" data-small-header="false" data-adapt-container-width="true" data-hide-cover="false" data-show-facepile="true"><blockquote cite="https://www.facebook.com/Career-Development-Corporate-Relations-Center-IIT-Ropar-169217773601805/" class="fb-xfbml-parse-ignore"><a href="https://www.facebook.com/Career-Development-Corporate-Relations-Center-IIT-Ropar-169217773601805/">Career Development &amp; Corporate Relations Center, IIT Ropar</a></blockquote></div>
                            			
                            			<br>
                            			<br>
                            			<br>
                                    	<h2 style="font-style:italic;"><i class="fas fa-envelope"></i> &nbsp; &nbsp;Quick Contacts</h2>
                                                 
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

	<!-- Companies -->
	<!-- <div class="col-md-12 col-sm-12" style="padding-top:30px; color: #000000;">
	        		<center><h1>Past Recruiters</h1>
	        		<marquee>
	        		<ul style="list-style-type: none; margin: 0; padding: 0; overflow: hidden;">
					    <li style="float: left; margin-left: 30px"><img src="images/c1.png" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c2.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c9.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c8.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c11.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c3.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c10.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c4.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c6.jpg" style="height:65px;max-width:100px;" ></li>
					</ul>
					</marquee></center>
					<br>
				<div class="col-md-12" style="padding:12px;padding-left:0px;"><a href="companies.php" class="newslinks" target="_blank">See More &nbsp;<i class="fa fa-angle-double-right"></i></a></div>
	        	</div>


	        </div> -->
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
<div id="fb-root"></div>
<script>(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = 'https://connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v3.0';
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
</html>
