<?php 
include "common.php";
?>
<!DOCTYPE html>
<html lang="en">
<head>
<title>Training and Placement | IIT Ropar</title>
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
					<h3 style="color: #FFFFFF;">Career Development and<br>Corporate Relations Centre</h3>
				</div>
			</div>

			<!-- Main Navigation -->
			<nav class="main_nav_container">
				<div class="main_nav">
					<ul class="main_nav_list">
						<li class="main_nav_item dropdown">
							<a href="index.php" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">home</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="tnp.php">T&P Home</a>
                                <a class="dropdown-item" href="index.php">CDCRC Home</a>
                                <a class="dropdown-item" href="http://www.iitrpr.ac.in/TP/index.php/msg-from-fic/">From The T&P Head</a>
                            </div>
						</li>
						<li class="main_nav_item"><a href="students.php">Students</a></li>
						<li class="main_nav_item dropdown">
							<a href="#" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">Academics</a>
                            <div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="http://www.iitrpr.ac.in/academic">Academics</a>
                                <a class="dropdown-item" href="http://www.iitrpr.ac.in/departments-schools">Department</a>
                                <a class="dropdown-item" href="http://www.iitrpr.ac.in/handbook-information">Course Description</a>
                                 <a class="dropdown-item" href="http://www.iitrpr.ac.in/research-iit-ropar">Research & Development</a>
                            </div>
						</li>
						<li class="main_nav_item dropdown">
							<a href="index.php" class="nav-link dropdown-toggle" id="navbardrop" data-toggle="dropdown">For Recruiters</a>
							<div class="dropdown-menu" style="background: #21618C; color: #FFFFFF">
                                <a class="dropdown-item" href="recruiters.php">Placement Procedure</a>
                                <a class="dropdown-item" target="_blank" href="https://drive.google.com/file/d/1eZza_gCHrIis2TsSWn8gwOYv7cuWtFiD/view?usp=sharing">Download JAF</a>
                                <a class="dropdown-item" target="_blank" href="https://drive.google.com/open?id=1idFnfF8ZxCAPkY-R8aXAPnA0RyO-Wcm2">Download INF</a>
                            </div>
						</li>
						<li class="main_nav_item"><a href="placementsummary.php">Statistics</a></li>
						<li class="main_nav_item"><a href="contacts.php">contact</a></li>
					</ul>
				</div>
			</nav>
		</div>
		<div class="header_side d-flex flex-row justify-content-center align-items-center">
			<span><img src="images/phone-call.svg" alt="">&nbsp;+91 86990 20183<br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#" style="color: #FFFFFF; margin-right: 20px;" onmouseover="this.style.color='#FFD800'" onmouseout="this.style.color='#FFFFFF'"><i class="fab fa-linkedin-in"></i></a>
				<a href="#" style="color: #FFFFFF; margin-right: 20px;" onmouseover="this.style.color='#FFD800'" onmouseout="this.style.color='#FFFFFF'"><i class="fab fa-facebook-f"></i></a>
				<a href="#" style="color: #FFFFFF; margin-right: 20px;" onmouseover="this.style.color='#FFD800'" onmouseout="this.style.color='#FFFFFF'"><i class="fab fa-twitter"></i></a>
				<a href="#" style="color: #FFFFFF;" onmouseover="this.style.color='#FFD800'" onmouseout="this.style.color='#FFFFFF'"><i class="fab fa-youtube"></i></a>
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
							<a href="index.php" class="dropdown-toggle" id="navbardrop" data-toggle="dropdown">Home</a>
							<div class="dropdown-menu">
                                <a class="dropdown-item" href="tnp.php">T&P Home</a>
                                <a class="dropdown-item" href="index.php">CDCRC Home</a>
                                <a class="dropdown-item" href="http://www.iitrpr.ac.in/TP/index.php/msg-from-fic/">From The T&P Head</a>

                            </div>
						</li>
						<li class="menu_item menu_mm"><a href="students.php">Students</a></li>
						<li class="menu_item menu_mm dropdown">
							<a href="#" class=" dropdown-toggle" id="navbardrop" data-toggle="dropdown">Academics</a>
                            <div class="dropdown-menu">
                                <a class="dropdown-item" href="http://www.iitrpr.ac.in/academic">Academics</a>
                                <a class="dropdown-item" href="http://www.iitrpr.ac.in/departments-schools">Department</a>
                                <a class="dropdown-item" href="http://www.iitrpr.ac.in/handbook-information">Course Description</a>
                                 <a class="dropdown-item" href="http://www.iitrpr.ac.in/research-iit-ropar">Research & Development</a>
                            </div>
						</li>
						<li class="menu_item menu_mm"><a href="recruiters.php">For Recruiters</a></li>
						<li class="menu_item menu_mm"><a href="placementsummary.php">Placement Staticstics</a></li>
						<li class="menu_item menu_mm"><a href="contacts.php">Contacts</a></li>
                                        
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
			<div class="home_background prlx" style="background-image:url(images/tnp.jpg)"></div>
		</div>
		<div class="home_content">
			<h1>Training and Placement</h1>
		</div>

	</div>
			<?php
				echo "<marquee style=\"color: #FFFFFF; background: #21618C;\" onMouseOver=\"this.stop()\" onMouseOut=\"this.start()\"><h3>";
				$sql = "SELECT * FROM cdcrc_events WHERE type=\"tnp\" ORDER BY event_id DESC";
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
			<div class="row" style="color: #535b60;">
				  <div class="col-md-8 col-sm-12">
				  	<div>
                                        <p><h1><i class="fas fa-angle-right"></i> &nbsp;Why IIT Ropar?</h1></p>
                                        &nbsp;
                                       <h2><i class="fas fa-angle-right"></i>&nbsp;Students-IIT Ropar</h2>
<p id="main_text" align="justify" style="color: #535b60;font-size:130%;">The undergraduates at IIT Ropar are scrutinized through IIT-JEE, which is considered one of the toughest examination across the globe. Only top 2% of the students make it to the IIT&#8217;s.</p>

<p id="main_text" align="justify" style="color: #535b60;font-size:130%;">Students are exposed to the most modern and up-to-date curriculum and contemporary developments in various disciplines of engineering. In addition to scientific and engineering skills, our graduates have been moulded into well-rounded personalities, given their exposure to team work on projects, presentation and communication skills and active participation in extracurricular activities.</p>

<p id="main_text" align="justify" style="color: #535b60;font-size:130%;">The students at IIT Ropar have been instrumental in shaping the institute by forming co-curricular societies and student bodies and organising institute-level events.</p>

<p id="main_text" align="justify" style="color: #535b60;font-size:130%;">The students have to complete a 10-week mandatory internship program. Organizations continually appreciate the hard work of IIT Ropar students and recognize them for their talent, innovation and industry readiness.</p>

<p id="main_text" align="justify" style="color: #535b60;font-size:130%;">The students also work on their major B.Tech projects in the final year of their study, which involves solving current industrial and other research oriented problems that involve potential products which may be commercialized in future.</p>
&nbsp;
<h2 class="page-title"><i class="fas fa-angle-right"></i>&nbsp;Selection Process</h2>
<!--<p> &nbsp;&nbsp;<br />-->

<p id="main_text" align="justify" style="color: #535b60;font-size:130%;">The selection to various programmes at IIT Ropar is extremely stringent to ensure that only the best of the students throughout the country secure admission. The admission to various programmes is carried out through highly competitive entrance examinations and procedures. Admission to B.Tech programmes is based on the JEE (Joint Entrance Examination) and that to the Doctoral Programme (PhD) is based on a centralized examination, GATE (Graduate Aptitude Test in Engineering), along with examinations and interviews conducted by each department within the institute.</p>
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

			<!-- <div class="row course_boxes">
				
				
				<div class="col-lg-4 course_box">
					<div class="card">
						<img class="card-img-top" src="images/course_1.jpg" alt="https://unsplash.com/@kellybrito">
						<div class="card-body text-center">
							<div class="card-title"><a href="courses.html">A complete guide to design</a></div>
							<div class="card-text">Adobe Guide, Layes, Smart Objects etc...</div>
						</div>
						<div class="price_box d-flex flex-row align-items-center">
							<div class="course_author_image">
								<img src="images/author.jpg" alt="https://unsplash.com/@mehdizadeh">
							</div>
							<div class="course_author_name">Michael Smith, <span>Author</span></div>
							<div class="course_price d-flex flex-column align-items-center justify-content-center"><span>$29</span></div>
						</div>
					</div>
				</div>

				
				<div class="col-lg-4 course_box">
					<div class="card">
						<img class="card-img-top" src="images/course_2.jpg" alt="https://unsplash.com/@cikstefan">
						<div class="card-body text-center">
							<div class="card-title"><a href="courses.html">Beginners guide to HTML</a></div>
							<div class="card-text">Adobe Guide, Layes, Smart Objects etc...</div>
						</div>
						<div class="price_box d-flex flex-row align-items-center">
							<div class="course_author_image">
								<img src="images/author.jpg" alt="https://unsplash.com/@mehdizadeh">
							</div>
							<div class="course_author_name">Michael Smith, <span>Author</span></div>
							<div class="course_price d-flex flex-column align-items-center justify-content-center"><span>$29</span></div>
						</div>
					</div>
				</div>

				
				<div class="col-lg-4 course_box">
					<div class="card">
						<img class="card-img-top" src="images/course_3.jpg" alt="https://unsplash.com/@dsmacinnes">
						<div class="card-body text-center">
							<div class="card-title"><a href="courses.html">Advanced Photoshop</a></div>
							<div class="card-text">Adobe Guide, Layes, Smart Objects etc...</div>
						</div>
						<div class="price_box d-flex flex-row align-items-center">
							<div class="course_author_image">
								<img src="images/author.jpg" alt="https://unsplash.com/@mehdizadeh">
							</div>
							<div class="course_author_name">Michael Smith, <span>Author</span></div>
							<div class="course_price d-flex flex-column align-items-center justify-content-center"><span>$29</span></div>
						</div>
					</div>
				</div>
			</div> -->
		</div>		
	</div>

	<!-- Register -->

	<!-- <div class="register">

		<div class="container-fluid">
			
			<div class="row row-eq-height">
				<div class="col-lg-6 nopadding">
					
					

					<div class="register_section d-flex flex-column align-items-center justify-content-center">
						<div class="register_content text-center">
							<h1 class="register_title">Register now and get a discount <span>50%</span> discount until 1 January</h1>
							<p class="register_text">In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum. Aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempo.</p>
							<div class="button button_1 register_button mx-auto trans_200"><a href="#">register now</a></div>
						</div>
					</div>

				</div>

				<div class="col-lg-6 nopadding">
					
					

					<div class="search_section d-flex flex-column align-items-center justify-content-center">
						<div class="search_background" style="background-image:url(images/search_background.jpg);"></div>
						<div class="search_content text-center">
							<h1 class="search_title">Search for your course</h1>
							<form id="search_form" class="search_form" action="post">
								<input id="search_form_name" class="input_field search_form_name" type="text" placeholder="Course Name" required="required" data-error="Course name is required.">
								<input id="search_form_category" class="input_field search_form_category" type="text" placeholder="Category">
								<input id="search_form_degree" class="input_field search_form_degree" type="text" placeholder="Degree">
								<button id="search_submit_button" type="submit" class="search_submit_button trans_200" value="Submit">search course</button>
							</form>
						</div> 
					</div>

				</div>
			</div>
		</div>
	</div> -->

	<!-- Services -->

	<!-- <div class="services page_section">
		
		<div class="container">
			<div class="row">
				<div class="col">
					<div class="section_title text-center">
						<h1>Our Services</h1>
					</div>
				</div>
			</div>

			<div class="row services_row">

				<div class="col-lg-4 service_item text-left d-flex flex-column align-items-start justify-content-start">
					<div class="icon_container d-flex flex-column justify-content-end">
						<img src="images/earth-globe.svg" alt="">
					</div>
					<h3>Online Courses</h3>
					<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
				</div>

				<div class="col-lg-4 service_item text-left d-flex flex-column align-items-start justify-content-start">
					<div class="icon_container d-flex flex-column justify-content-end">
						<img src="images/exam.svg" alt="">
					</div>
					<h3>Indoor Courses</h3>
					<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
				</div>

				<div class="col-lg-4 service_item text-left d-flex flex-column align-items-start justify-content-start">
					<div class="icon_container d-flex flex-column justify-content-end">
						<img src="images/books.svg" alt="">
					</div>
					<h3>Amazing Library</h3>
					<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
				</div>

				<div class="col-lg-4 service_item text-left d-flex flex-column align-items-start justify-content-start">
					<div class="icon_container d-flex flex-column justify-content-end">
						<img src="images/professor.svg" alt="">
					</div>
					<h3>Exceptional Professors</h3>
					<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
				</div>

				<div class="col-lg-4 service_item text-left d-flex flex-column align-items-start justify-content-start">
					<div class="icon_container d-flex flex-column justify-content-end">
						<img src="images/blackboard.svg" alt="">
					</div>
					<h3>Top Programs</h3>
					<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
				</div>

				<div class="col-lg-4 service_item text-left d-flex flex-column align-items-start justify-content-start">
					<div class="icon_container d-flex flex-column justify-content-end">
						<img src="images/mortarboard.svg" alt="">
					</div>
					<h3>Graduate Diploma</h3>
					<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
				</div>

			</div>
		</div>
	</div> -->

	<!-- Testimonials -->

	<!-- <div class="testimonials page_section">
		
		<div class="testimonials_background_container prlx_parent">
			<div class="testimonials_background prlx" style="background-image:url(images/testimonials_background.jpg)"></div>
		</div>
		<div class="container">

			<div class="row">
				<div class="col">
					<div class="section_title text-center">
						<h1>What our students say</h1>
					</div>
				</div>
			</div>

			<div class="row">
				<div class="col-lg-10 offset-lg-1">
					
					<div class="testimonials_slider_container">

						
						<div class="owl-carousel owl-theme testimonials_slider">
							
							
							<div class="owl-item">
								<div class="testimonials_item text-center">
									<div class="quote">“</div>
									<p class="testimonials_text">In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
									<div class="testimonial_user">
										<div class="testimonial_image mx-auto">
											<img src="images/testimonials_user.jpg" alt="">
										</div>
										<div class="testimonial_name">james cooper</div>
										<div class="testimonial_title">Graduate Student</div>
									</div>
								</div>
							</div>

							
							<div class="owl-item">
								<div class="testimonials_item text-center">
									<div class="quote">“</div>
									<p class="testimonials_text">In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
									<div class="testimonial_user">
										<div class="testimonial_image mx-auto">
											<img src="images/testimonials_user.jpg" alt="">
										</div>
										<div class="testimonial_name">james cooper</div>
										<div class="testimonial_title">Graduate Student</div>
									</div>
								</div>
							</div>

							
							<div class="owl-item">
								<div class="testimonials_item text-center">
									<div class="quote">“</div>
									<p class="testimonials_text">In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum.</p>
									<div class="testimonial_user">
										<div class="testimonial_image mx-auto">
											<img src="images/testimonials_user.jpg" alt="">
										</div>
										<div class="testimonial_name">james cooper</div>
										<div class="testimonial_title">Graduate Student</div>
									</div>
								</div>
							</div>

						</div>

					</div>
				</div>
			</div>

		</div>
	</div> -->

	<!-- Events -->

	<!-- <div class="events page_section">
		<div class="container">
			
			<div class="row">
				<div class="col">
					<div class="section_title text-center">
						<h1>Upcoming Events</h1>
					</div>
				</div>
			</div>
			
			<div class="event_items">

				
				<div class="row event_item">
					<div class="col">
						<div class="row d-flex flex-row align-items-end">

							<div class="col-lg-2 order-lg-1 order-2">
								<div class="event_date d-flex flex-column align-items-center justify-content-center">
									<div class="event_day">07</div>
									<div class="event_month">January</div>
								</div>
							</div>

							<div class="col-lg-6 order-lg-2 order-3">
								<div class="event_content">
									<div class="event_name"><a class="trans_200" href="#">Student Festival</a></div>
									<div class="event_location">Grand Central Park</div>
									<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor.</p>
								</div>
							</div>

							<div class="col-lg-4 order-lg-3 order-1">
								<div class="event_image">
									<img src="images/event_1.jpg" alt="https://unsplash.com/@theunsteady5">
								</div>
							</div>

						</div>	
					</div>
				</div>

				
				<div class="row event_item">
					<div class="col">
						<div class="row d-flex flex-row align-items-end">

							<div class="col-lg-2 order-lg-1 order-2">
								<div class="event_date d-flex flex-column align-items-center justify-content-center">
									<div class="event_day">07</div>
									<div class="event_month">January</div>
								</div>
							</div>

							<div class="col-lg-6 order-lg-2 order-3">
								<div class="event_content">
									<div class="event_name"><a class="trans_200" href="#">Open day in the Univesrsity campus</a></div>
									<div class="event_location">Grand Central Park</div>
									<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor.</p>
								</div>
							</div>

							<div class="col-lg-4 order-lg-3 order-1">
								<div class="event_image">
									<img src="images/event_2.jpg" alt="https://unsplash.com/@claybanks1989">
								</div>
							</div>

						</div>	
					</div>
				</div>

				
				<div class="row event_item">
					<div class="col">
						<div class="row d-flex flex-row align-items-end">

							<div class="col-lg-2 order-lg-1 order-2">
								<div class="event_date d-flex flex-column align-items-center justify-content-center">
									<div class="event_day">07</div>
									<div class="event_month">January</div>
								</div>
							</div>

							<div class="col-lg-6 order-lg-2 order-3">
								<div class="event_content">
									<div class="event_name"><a class="trans_200" href="#">Student Graduation Ceremony</a></div>
									<div class="event_location">Grand Central Park</div>
									<p>In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor.</p>
								</div>
							</div>

							<div class="col-lg-4 order-lg-3 order-1">
								<div class="event_image">
									<img src="images/event_3.jpg" alt="https://unsplash.com/@juanmramosjr">
								</div>
							</div>

						</div>	
					</div>
				</div>

			</div>
				
		</div>
	</div> -->
	<!-- Companies -->
	<div class="col-md-12 col-sm-12" style="padding-top:30px; color: #535b60;">
	        		<center><h1>Past Recruiters</h1>
	        		<marquee>
	        		<ul style="list-style-type: none; margin: 0; padding: 0; overflow: hidden;">
					    <li style="float: left; margin-left: 30px"><img src="images/c1.png" style="height:65px;max-width:150px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c2.jpg" style="height:65px;max-width:150px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c9.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c8.jpg" style="height:65px;max-width:150px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c11.jpg" style="height:65px;max-width:150px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c3.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c10.jpg" style="height:65px;max-width:150px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c4.jpg" style="height:65px;max-width:100px;" /></li>
                        <li style="float: left; margin-left: 30px"><img src="images/c6.jpg" style="height:65px;max-width:100px;" ></li>
					</ul>
					</marquee></center>
					<br>
				<div class="col-md-12" style="padding:12px;padding-left:0px;"><a href="companies.php" class="newslinks" target="_blank">See More &nbsp;<i class="fa fa-angle-double-right"></i></a></div>
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
