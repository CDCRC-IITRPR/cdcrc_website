// console.log('Welcome');

window.onload = function () {
    document.querySelector('.sidebarMenu').addEventListener('click', el => {
      // console.log(el.target.textContent);
  
      if (el.target.textContent.toString().includes("SDE")) {
        let html = `
        <h2 style="color: #126aee;">SDE</h2>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit voluptatum quas vero? Voluptatem molestias rem amet recusandae. Nemo deleniti, sit corrupti exercitationem unde explicabo ullam dignissimos officiis, magnam inventore nihil fugit, omnis nesciunt deserunt aliquid dolorum obcaecati ut repellendus! Voluptatibus sint, molestiae nesciunt unde quidem velit aliquam delectus ratione, a sapiente blanditiis debitis? Rem possimus tempora quidem impedit deleniti et laborum in delectus perspiciatis ipsam, ratione nulla saepe nostrum! Incidunt, accusamus sapiente. Maiores aspernatur amet architecto. Cupiditate quasi fuga officia, repellendus accusamus expedita, repudiandae repellat nesciunt error at, ullam blanditiis velit dicta unde quas perspiciatis nostrum. Odit delectus quam debitis.</p>       
  
        `;
        document.querySelector('.txt-box').innerHTML = html;
      }
  
      else if (el.target.textContent.toString().includes("Non-Core")) {
        html = `
        <h2  style="color: #126aee;">Non-Core</h2>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit voluptatum quas vero? Voluptatem molestias rem amet recusandae. Nemo deleniti, sit corrupti exercitationem unde explicabo ullam dignissimos officiis, magnam inventore nihil fugit, omnis nesciunt deserunt aliquid dolorum obcaecati ut repellendus! Voluptatibus sint, molestiae nesciunt unde quidem velit aliquam delectus ratione, a sapiente blanditiis debitis? Rem possimus tempora quidem impedit deleniti et laborum in delectus perspiciatis ipsam, ratione nulla saepe nostrum! Incidunt, accusamus sapiente. Maiores aspernatur amet architecto. Cupiditate quasi fuga officia, repellendus accusamus expedita, repudiandae repellat nesciunt error at, ullam blanditiis velit dicta unde quas perspiciatis nostrum. Odit delectus quam debitis.</p>
  
        `;
        document.querySelector('.txt-box').innerHTML = html;
      }
  
      else if (el.target.textContent.toString().includes("Core")) {
        html = `
  
        <h2  style="color: #126aee;">Core</h2>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit voluptatum quas vero? Voluptatem molestias rem amet recusandae. Nemo deleniti, sit corrupti exercitationem unde explicabo ullam dignissimos officiis, magnam inventore nihil fugit, omnis nesciunt deserunt aliquid dolorum obcaecati ut repellendus! Voluptatibus sint, molestiae nesciunt unde quidem velit aliquam delectus ratione, a sapiente blanditiis debitis? Rem possimus tempora quidem impedit deleniti et laborum in delectus perspiciatis ipsam, ratione nulla saepe nostrum! Incidunt, accusamus sapiente. Maiores aspernatur amet architecto. Cupiditate quasi fuga officia, repellendus accusamus expedita, repudiandae repellat nesciunt error at, ullam blanditiis velit dicta unde quas perspiciatis nostrum. Odit delectus quam debitis.</p>
  
      `;
        document.querySelector('.txt-box').innerHTML = html;
      }
      else if (el.target.textContent.toString().includes("FAQ")) {
        html = `
        <h2  style="color: #126aee;">FAQs</h2>
        
        
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
  
  