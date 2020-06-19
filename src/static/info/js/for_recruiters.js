// console.log('Welcome');

window.onload = function () {
  document.querySelector('.sidebarMenu').addEventListener('click', el => {
    // console.log(el.target.textContent);

    if (el.target.textContent.toString().includes("Why")) {
      let html = `
      <h2 style="color: #126aee;">Why Recruit?</h2>



                <div id="aboutiitrpr">
                    <div>
                        <p xss="removed">
                            IIT Ropar is the first, the largest and the most diversified among the IITs, and has
                            always been an innovator either in the industry or academia; the alumni of this
                            institute have always made their alma mater proud, with their innovative thoughts and
                            perseverance for the growth of corporations all over the globe. The institute offers a
                            robust academic curriculum, along with a culture of excellence in extra­curricular
                            activities. A typical rprian has always played a pivotal role in the growth of
                            organizations, a habit which is cultivated right here on campus. Our alumni reinforce
                            our belief that whichever be the industry, at IIT Ropar, you will always find
                            candidates meeting, and even exceeding your expectations from a prospective employee.
                        </p>
                        <p xss="removed">
                            &nbsp;</p>
                        <h5 style="color: #126aee;">
                            Academic Offerings</h5>
                        <p xss="removed">
                            <img alt="" class="pull-left insideimgSpace"
                                src="/allbuni/ckfinder/userfiles/images/whyacads.jpg" xss="removed"></p>
                        <p xss="removed">
                            IIT Ropar has 19 academic departments, 15 multi-disciplinary research centers and 12
                            schools and more than 25 Industries and Reserach Lab, Reserach Centres and Centre of
                            Excellence offering world class education in engineering, science, humanities,
                            management, law and design. It has laboratories and central research facilities equipped
                            with the most modern equipment to aide practical understanding of concepts and
                            facilitate research and industrial exposure. Courses available in the Vinod Gupta School
                            of Management and Rajiv Gandhi School of Intellectual Property Law ensures that students
                            who have a bend towards management and consulting sectors have their needs met. With
                            such massive diversity in our offerings the only thing you’ll find uniformly throughout
                            is our relentless pursuit of excellence in doing what we do.</p>
                        <div>
                            <div>
                                <p xss="removed">
                                    IIT Ropar keeps continually re-inventing itself in terms of the academic
                                    curriculum so that it can stay ahead of its times and provide its students with
                                    the best set of skills to excel. Our students today have the flexibility to take
                                    cross-departmental courses as additional or even complete a minor degree in
                                    another department, in addition to learning the ins and outs of their major
                                    degree. We also provide them with the opportunity to complete a
                                    Micro-specialization in extremely important aspects of engineering like systems
                                    reliability, embedded wireless systems or even biomedical devices. This enables
                                    them to undertake interdisciplinary research and be more holistic in their
                                    approach towards the industry.</p>
                            </div>
                        </div>
                    </div>
                </div> 

      `;
      document.querySelector('.txt-box').innerHTML = html;
    }

    else if (el.target.textContent.toString().includes("Placement")) {
      html = `
      <h2  style="color: #126aee;">Placement</h2>



      <p  style="color: #126aee;">
          <strong>Dear Sir / Ma'am,</strong></p>
      <p  style="color: #126aee;">
          <strong>Greetings from IIT Ropar. It is indeed with great pleasure, we cordially invite your
              esteemed organization to participate in our campus placement programme to consider students
              graduating in June 2020.</strong></p>
      <p xss="\">
          IIT Ropar, the first, the largest and the most diversified among the IITs, has always been the
          leader. The alumni of this Institute occupy top positions in business, industry, R&amp;D and
          academia in India and abroad. In addition to a rigorous academic schedule, we emphasize on all-round
          development of our students. The beautiful campus, far away from the city, provides an excellent
          environment for learning. Quick on the uptake, with good communication and interpersonal skills and
          aware of modern developments, the typical IIT rprian is expected to play a pivotal role in leading
          organizations that are competitive in terms of products, services, and technology. At IIT Ropar we
          have students meeting various requirements in diversified fields of interest and expertise of the
          industry. It would be our pleasure to welcome you to participate in the recruitment session
          2019-2020.</p>
      <p>
          We have planned the following schedule at IIT Ropar for campus interviews of students graduating in
          2020 :</p>
      <div>
          <h5  style="color: #126aee;">
              1. &nbsp;Pre Placement Talks [ PPT ] for Final Placements - From&nbsp; August 2019 onwards.</h5>
          <p>
              a)&nbsp;&nbsp;If you are interested in making an early PPT – you are most welcome to book a slot
              as early as you can. This early PPT with the interactive session will give a scope for our
              students to understand the profile of your esteemed organization, their job profile including
              job prospects etc.</p>
          <p>
              b)&nbsp;&nbsp; In case your company feels it inconvenient to make visit twice – you are most
              welcome to carry out the entire selection process, including PPT, during final placement season
              on a mutually agreed date.</p>
          <h5  style="color: #126aee;">
              2. &nbsp; Final Placements -</h5>
          <p>
              First Phase :&nbsp;1st&nbsp;to 15th&nbsp;December, 2019.</p>
          <p>
              Second Phase :&nbsp;5th&nbsp;January&nbsp;2020 till end of March 2020</p>
          <h5  style="color: #126aee;">
              3. &nbsp; Job Notification Form</h5>
          <p>
              The company will have to fill in the required details in the JNF (Job Notification Form)
              available on their login.</p>
          <p>
              Link of JNF:&nbsp;<a href="https://erp.iitrpr.ac.in/TrainingPlacement/index"
                  target="_blank">https://erp.iitrpr.ac.in/TrainingPlacement/index</a></p>
          <p>
              Please feel to contact the undersigned anytime as per your convenience.</p>
          <p>
              Looking forward to hear from you soon.</p>
          <p>
              With the warmest regards,&nbsp;</p>
          <p>
              Prof. G P Raja Sekhar&nbsp;<br>
              Chairperson, Career Development Centre (CDC)</p>
      </div>
      <p>
          &nbsp;</p>
      <p>
          UG Curricula:&nbsp;<a target="_blank" href="http://www.iitrpr.ac.in/ug-courses">Link</a>
      </p>
      <p>
          PG Curricula:&nbsp;<a target="_blank" href="http://www.iitrpr.ac.in/pg-courses">Link</a>
      </p>
      `;
      document.querySelector('.txt-box').innerHTML = html;
    }

    else if (el.target.textContent.toString().includes("Internship")) {
      html = `

      <h2  style="color: #126aee;">Internship</h2>



      <p  style="color: #126aee;">
          <strong>Dear Sir / Ma'am,</strong></p>
      <p  style="color: #126aee;">
          <strong>Greetings from IIT Ropar. It is indeed with great pleasure, we cordially invite your
              esteemed organization to participate in our Campus Recruitment Programme to consider the
              students having their compulsory Internship in summers 2020</strong></p>
      <p xss="\">
          IIT Ropar, the first, the largest and the most diversified among the IITs, has always been the
          pacesetter. The alumni of this Institute occupy top positions in business, industry, R&amp;D and
          academia in India and abroad. Over and above a rigorous academic schedule, we place a great emphasis
          on all-round development of our students. The beautiful campus, far away from the city, provides an
          excellent environment for learning. Each and every student is provided with an Internet connection
          in his / her hostel room. Quick on the up-take, with good communication and human relations skills
          and aware of modern developments, the typical IIT rprian is expected to play a pivotal role in
          organizations like yours willing to be internationally competitive in terms of products, services
          and technology. At IIT Ropar you would find candidates meeting your requirements in practically
          every field of interest to your organization. It will be my pleasure to assist in your recruitment
          efforts to meet the challenges ahead.</p>
      <p>
          We have planned the following schedule at IIT Ropar for campus interviews of students eligible for 8
          weeks Compulsory Internship in Summers 2019 (during 1st week of May, 2020&nbsp; to middle of July,
          2020).</p>
      <h5 style="color: #126aee;">
          1. &nbsp;Pre Placement Talks [ PPT ] for Internships : 31st July, 2019 onwards</h5>
      <p>
          The PPTs will be held in two slots each day after the class hours from:&nbsp;<br>
          Monday through Friday - 5.30 PM to 6.30 PM and 6.30 PM to 7.30 PM&nbsp;<br>
          On Saturdays/Sundays/Holidays, we may have around five slots -- 9.30 AM/11.00 AM/2.30 PM/4.30
          PM/6.30 PM</p>
      <h5 style="color: #126aee;">
          2. &nbsp;Selection Process for Internship&nbsp;–&nbsp; August 2019&nbsp; onwards</h5>
      <p>
          If you are interested in hiring both Interns and Full Time, you can give a combined PPT followed by
          Interns Selection the same day.</p>
      <p>
          If you are interested in making an early PPT - you are most welcome to block a slot + date as early
          as you can. This early PPT with interactive session will allow our students to understand the
          profile of your esteemed organization, their job profile including job prospects etc. We would
          request you to kindly ensure your presence in the campus on the allocated slot and date for the PPT
          as otherwise we will be loosing the slot if you make any last moment change in the agreed schedule.
      </p>
      <p>
          In case your company feels it is inconvenient to visit twice - you are most welcome to carry out the
          entire selection process, including PPT, during final placement season on a mutually agreed date.
      </p>
      <h5 style="color: #126aee;">
          3. &nbsp; How to participate :</h5>
      <p>
          If you wish to participate in the Campus Placement and Intern selection process of 2019-20, you need
          to register yourself at&nbsp;<a href="https://erp.iitrpr.ac.in/TrainingPlacement/index"
              target="_blank">this link</a>.</p>
      <p>
          Looking forward to your response and thanking you in anticipation.</p>
      <p>
          With the warmest regards,&nbsp;</p>
      <p>
          Prof. G P Raja Sekhar&nbsp;<br>
          Chairman, Career Development Centre (CDC)</p>

      

    `;
      document.querySelector('.txt-box').innerHTML = html;
    }
    else if (el.target.textContent.toString().includes("FAQ")) {
      html = `
      <h2  style="color: #126aee;">FAQs</h2>



      <p style="color: #126aee;">
          <strong>In what ways can a company recruit from campus ?</strong></p>
      <p>
          The different ways of recruiting are as follows :</p>
      <ul>
          <li>
              <p>
                  The Campus Recruitment Program for which the final year students are eligible.</p>
          </li>
          <li>
              <p>
                  Summer Internship Programs which can be converted to a Pre Placement Offer.</p>
          </li>
      </ul>
      <p style="color: #126aee;">
          <strong>What procedure should a company to register itself for the Campus Recruitment Process
              ?</strong></p>
      <p>
          To register, the company should either contact the CDC office or should register itself on the
          website following which they will be issued login details. These details would enable them to login
          to the Company Portal, using which they can post job openings and see the profiles of students
          eligible and suitable to their job specifications. You can refer to the placement procedure&nbsp;<a
              href="http://cdc.iitrpr.ac.in/p/placement-1" target="_blank">here</a>.</p>
      <p style="color: #126aee;">
          <strong>Is there any fee associated with the process ?</strong></p>
      <p>
          No. There is no fee of any kind associated with the program.</p>
      <p style="color: #126aee;">
          <strong>When does the recruitment process start ?</strong></p>
      <p>
          The Campus Placement Process for the final year student starts on&nbsp;December 1&nbsp;every year.
          The internship process starts in August.</p>
      <p style="color: #126aee;">
          <strong>How well is Ropar connected to the country ?</strong></p>
      <p>
          Ropar is well connected to all major Indian cities by rail. Alternatively, you can reach the Howrah
          railway station and then commute by train or taxi to the institute, taking an additional 2 to 3
          hours. If you wish to travel by air, the nearest airport is NetajiSubhash Chandra Bose International
          Airport, Chandigarh. From there you can take a taxi and reach the campus in 2 ½ hours. For further
          details click&nbsp;<a href="http://cdc.iitrpr.ac.in/p/reach-iit-rpr-1">here</a>.</p>
      <p style="color: #126aee;">
          <strong>What is the process for scheduling Pre Placement Talks on campus ?</strong></p>
      <p>
          A company can only hold its PPT once it has filled in the Job Notification Form. A Pre Placement
          Session is typically scheduled for 1 hour. A student coordinator will be in touch with you regarding
          the formalities once other requirements have been met.</p>
      <p style="color: #126aee;">
          <strong>What facilities are available for accommodation on campus ?</strong></p>
      <p>
          We offer rooms on campus at the Technology Guest House on a twin sharing basis. A Student
          Coordinator will be in touch with you after prior formalities related to the program have been
          completed.</p>
      <p style="color: #126aee;">
          <strong>Are there multiple companies recruiting in a single slot ? How is the problem of multiple
              offers resolved ?</strong></p>
      <p>
          Yes, there are multiple companies recruiting in each slot. The job offers of each particular slot
          are announced at the end of the slot and each candidate is required to confirm his choice by 10 AM
          the next day.</p>
      <p style="color: #126aee;">
          <strong>Can a candidate who has already been placed sit the interviews of another company ?</strong>
      </p>
      <p>
          IIT Ropar strictly follows a&nbsp;One Student, One Job&nbsp;policy wherein, once a job has been
          accepted by the student he will not be eligible for any other company thereafter.</p>
      <p style="color: #126aee;">
          <strong>What sort of infrastructure is available on the campus for the placement process ?</strong>
      </p>
      <p>
          IIT Ropar is equipped with state-of-the-art communication, technological and presentation facilities
          to facilitate the process. These include :</p>
      <ul>
          <li>
              <p>
                  Teleconferencing and Video-Conferencing.</p>
          </li>
          <li>
              <p>
                  Linux and Windows Labs for online tests.</p>
          </li>
          <li>
              <p>
                  Centrally air conditioned auditorium, lecture halls, seminar and conference rooms for
                  presentations, group discussions and interviews.</p>
          </li>
      </ul>
      
    `;
      document.querySelector('.txt-box').innerHTML = html;
    }


    // if clicks on some other tab other than our curriculam or its children
    if (!el.target.textContent.toString().includes("Graduate") && !el.target.textContent.toString().includes("Our")) {
      document.querySelector('.cur-btn').nextSibling.nextSibling.childNodes[1].style.display = 'none';
    }
    // if clicks on our curriculum, it should open or close 
    if (el.target.textContent.toString().includes("Our")) {
      if (document.querySelector('.cur-btn').nextSibling.nextSibling.childNodes[1].style.display == 'block')
        document.querySelector('.cur-btn').nextSibling.nextSibling.childNodes[1].style.display = 'none';
      else {
        document.querySelector('.cur-btn').nextSibling.nextSibling.childNodes[1].style.display = 'block';
      }
    }
    // to make every children of curriclum inactive before  start
    const curbtn = document.querySelector('.cur-btn').nextSibling.nextSibling.childNodes[1].childNodes;
    for (let j = 1; j < curbtn.length; j = j + 2) {
      curbtn[j].classList.remove('active');
    }
    // to make every child inactive other than the selected one
    const table_list = el.target.parentNode.parentNode.childNodes;
    for (let i = 1; i < table_list.length; i = i + 2) {

      table_list[i].classList.remove('active');
    }
    el.target.parentNode.classList.add('active');
  });
}

