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
			</div>
	</div>


	<div class="popular page_section">
		<div class="container">
			<div class="row" style="color: #535b60;">
				  <div class="col-md-8 col-sm-12">
				  	<div>
                         <p><h1><i class="fas fa-angle-right"></i> &nbsp;HOD Bios</h1></p>
                                        &nbsp;
                         	<h2><i class="fas fa-angle-right"></i>&nbsp;Asad H. Sahir</h2>
                         	&nbsp;
                         	<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/asad-sahir.jpg" alt="" width="100%" height="100%" />
                         	&nbsp;
							<p id="main_text" align="justify" style="color: #535b60;font-size:130%;line-height:160%;">
							
							Asad H. Sahir, PhD is currently responsible for professional development at IIT Ropar. A chemical engineering academician in his current avatar, he is utilizing the training acquired as a Higher Education Teaching Specialist and a Teaching Assistant Scholar at the University of Utah to help students achieve their professional aspirations with the support of Career Development and Corporate Relations Centre team members at IIT Ropar.<br>On the field of professional development, he was an active member of the National Renewable Energy Laboratory’s Postdoctoral Committee which organized numerous training events ranging from talks from distinguished scientists to US Department of Energy administrators. On similar lines, he is working to develop a vibrant community of students who will be the next generation science and technology leaders, and sharing his privileged experiences.<br>When Dr. Sahir is not involved with academic, research and administrative matters, he always welcomes the opportunity to learn from students on creating an academic environment which fuels inspiration, achievement and creates opportunities for transformative learning. A favorite pastime of his nowadays is to draw cartoons for his daughter and rediscover corporate, administrative and academic life from his IIT Ropar and CDCRC team members over a cup of coffee and a nice hot brownie.<br>He feels inspired by reading Creativity, Inc.: Overcoming the Unseen Forces That Stand in the Way of True Inspiration (Ed Catmull), Extreme Ownership: How U.S. Navy SEALs Lead and Win (Jocko Willink) , Lean In: Women, Work, and the Will to Lead (Sheryl Sandberg) and The Art of Possibility: Transforming Professional and Personal Life (Benjamin Zander). Though not a musician, his interests range from Bach to Rachel Platten; and has recently discovered Desert Island Discs BBC podcasts which is furthering his knowledge.
							
							</p>
&nbsp;

              	<h2><i class="fas fa-angle-right"></i>&nbsp;Subodh Sharma</h2>
              	
              	&nbsp;
             	<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/SubodhSir.png" alt="" width="100%" height="100%" />
             	&nbsp;
             	
             	
							<p id="main_text" align="justify" style="color: #535b60;font-size:130%;line-height:160%;">
							
							Mr Subodh Sharma is currently working as Placement &amp; Corporate Relations Manager at IIT Ropar. A
post graduate in management from Panjab University, Chandigarh, he has over 7 years of
experience in managing corporate affairs in different organizations with clients varying from various
industries (Core Engineering , Software Development, Healthcare, Pharmaceutical, Consultancy)
Industry. His scope of work varies from managing corporate relations of IIT Ropar to the professional
development of its students, and enable students seek the best placement &amp; internship
opportunities.<br>
Mr Sharma works closely with the faculty members and industry professionals in exploring various
channels to create and enhance partnership between institute and industry. Another major task
which he performs is in advising and counselling the students towards their career goals and helping
them achieve to the best of their potential. This includes various professional development activities
like incorporating networking skills, Interview preparation, resume building, professional etiquette
and guiding them for other alternative career options.<br>
At IIT Ropar he has been instrumental in developing the concept of learning communities which
provide an alternative option to usual placement operations. Currently Learning Communities have
been formed for Civil Services aspirants and plans are to extend them for GRE and GMAT students.
He is also committed to helping employers identify the best and most innovative ways to recruit on
campus for their goals and bandwidth. He has extensive experience in program management and
event planning, and loves using this experience to create meaningful opportunities for
employer/student connection, education and exploration and strengthening Industry-Academia
Collaboration.<br>
Apart from his professional life he is always looking for the opportunity to brainstorm new ideas
which could help society &amp; people to improve the quality of life. He is also keen to interact with
entrepreneurs and help them in all the possible ways to succeed.
							
							</p>
&nbsp;

              	<!--<h2><i class="fas fa-angle-right"></i>&nbsp;Dhiraj K. Mahajan</h2>
							
							
              	&nbsp;
             	<img src="http://www.iitrpr.ac.in/TP/wp-content/uploads/2018/11/DhirajSir.jpeg" alt="" width="100%" height="100%" />
             	&nbsp;
							<p id="main_text" align="justify" style="color: #535b60;font-size:130%;line-height:170%;">
							
							Asad H. Sahir, PhD is currently responsible for professional development at IIT Ropar. A chemical engineering academician in his current avatar, he is utilizing the training acquired as a Higher Education Teaching Specialist and a Teaching Assistant Scholar at the University of Utah to help students achieve their professional aspirations with the support of Career Development and Corporate Relations Centre team members at IIT Ropar.<br>On the field of professional development, he was an active member of the National Renewable Energy Laboratory’s Postdoctoral Committee which organized numerous training events ranging from talks from distinguished scientists to US Department of Energy administrators. On similar lines, he is working to develop a vibrant community of students who will be the next generation science and technology leaders, and sharing his privileged experiences.<br>When Dr. Sahir is not involved with academic, research and administrative matters, he always welcomes the opportunity to learn from students on creating an academic environment which fuels inspiration, achievement and creates opportunities for transformative learning. A favorite pastime of his nowadays is to draw cartoons for his daughter and rediscover corporate, administrative and academic life from his IIT Ropar and CDCRC team members over a cup of coffee and a nice hot brownie.<br>He feels inspired by reading Creativity, Inc.: Overcoming the Unseen Forces That Stand in the Way of True Inspiration (Ed Catmull), Extreme Ownership: How U.S. Navy SEALs Lead and Win (Jocko Willink) , Lean In: Women, Work, and the Will to Lead (Sheryl Sandberg) and The Art of Possibility: Transforming Professional and Personal Life (Benjamin Zander). Though not a musician, his interests range from Bach to Rachel Platten; and has recently discovered Desert Island Discs BBC podcasts which is furthering his knowledge.
							
							</p>
&nbsp;


							</p>
-->
								</div>
                            </div>
                                 <div class="col-md-4 col-sm-12">
                                 	<div class="col-md-12">
                                 		<!-- News -->
                            			<div style="max-height:300px;overflow-y:scroll;padding-right:16px;padding-bottom:30px;">
                            				<h2 style="padding-bottom:10px;"><i class="fa fa-list-alt"></i> &nbsp;Recent News</h2>
                            				<ul>
                            					<?php
                            						$sql = "SELECT * FROM cdcrc_news WHERE type=\"tnp\" ORDER BY news_id DESC";
													$result = $con->query($sql);
													if ($result->num_rows > 0){
														while($row = $result->fetch_assoc()){
															echo "<li><a href=\"".$row["link"]."\" style=\"color: #000000;\" onmouseover=\"this.style.color='#21618C'\" onmouseout=\"this.style.color='#000000'\"><h3><i class=\"fas fa-angle-right\"></i> &nbsp;".$row["display_text"]."</h3></a></li>";
														}
													}
                            					?>
                            				</ul>
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
