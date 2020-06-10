console.log('sdfaa');
document.querySelector('#leftSidecssmenu').addEventListener('click', el => {
    console.log(el.target.textContent);
    // if clicks on some other tab other than our curriculam or its children
    if (!el.target.textContent.toString().includes("Graduate")&&!el.target.textContent.toString().includes("Our")) {
      document.querySelector('.cur-btn').nextSibling.nextSibling.childNodes[1].style.display = 'none';
    }
    // if clicks on our curriculum, it should open or close 
    if (el.target.textContent.toString().includes("Our")) {
      if(document.querySelector('.cur-btn').nextSibling.nextSibling.childNodes[1].style.display == 'block')
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
