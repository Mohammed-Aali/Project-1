flash = document.getElementById('flash');
if (flash) {
    flash.addEventListener('click', (event) => {
        flash.style.display = "none";
    })
}

// page identity
let currentPage = window.location.href
if(currentPage.match(/(^|\W)login($|\W)/)) {

    window.onload = () =>
    {
        if (passCheck.innerHTML === "Email or Password don't match") {
            passCheck.classList.add("d-block")
        }
    }
    // define a an object array of regEx with the message associated with them
    let regexArray = [
        {regex: /^[^]{8,32}$/, msg: "Password must be exactly between 8 and 32 characters long."},
        {regex: /[a-z]/, msg: 'Password must contain at least one lowercase letter.'},
        {regex: /[A-Z]/, msg: 'Password must contain at least one uppercase letter.'},
        {regex: /\d/, msg: "Password must contain at least one number."},
    ]

    // setup variables
    let checkResult, checkEmail, checkPass;
    let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    const email = document.getElementById('emailInput');
    const form = document.getElementsByTagName('form')[0];
    const password = document.getElementById("current-password");
    const passCheck = document.getElementById("passCheck");
    const emailCheck = document.getElementById("emailCheck");
    const signIn = document.getElementById("signIn");
    const togglePasswordBlock = document.getElementsByClassName('input-group-text')[0];
    const togglePasswordButton = document.getElementById('togglePasswordButton');
    // disable the button after it has been clicked
    function disableBtn() {
        var btn = document.getElementById("loginBtn");
        btn.disabled = true;
        btn.innerHTML = 'Posting...';
    }

    togglePasswordBlock.addEventListener('click', togglePassword)
    function togglePassword(){
        if (password.type === 'password') {
            password.type = 'text';
            togglePasswordButton.setAttribute('aria-label', 'Hide password.');
            togglePasswordButton.classList.replace("bi-eye-slash", "bi-eye");
        } else {
            password.type = 'password';
            togglePasswordButton.setAttribute('aria-label', 'Show password as plain text. ' + 'Warning: this will display your password on the screen.');
            togglePasswordButton.classList.replace("bi-eye", "bi-eye-slash");
        }
    }
    // check for email
    email.addEventListener('input', event => {
        checkResult = true
        emailIn = event.target.value
        if(emailRegex.test(emailIn)) {
            emailCheck.innerHTML = '<span style="color: green;">Nice 😊</span>'
        } else {
            checkResult = false
            emailCheck.classList.add('d-block');
            emailCheck.innerHTML = 'Please enter a valid email Adress';
        }
    })
    // check password for validity using the regexp Array
    password.addEventListener('input', event => {
        passwordIn = event.target.value
        checkResult = true
        regexArray.forEach(item => {
            if(!item.regex.test(passwordIn)) {
            checkResult = false
            passCheck.classList.add('d-block')
            passCheck.innerHTML = `<p>${item.msg}</p>`
            }
            });
            if (checkResult) {
                passCheck.innerHTML = '<span style="color: green;">Nice 😊</span>'
            }
    });


    // form check
    form.addEventListener('submit', event => {
        if (!checkResult)
        {
            form.classList.add("was-validated");
            event.preventDefault();
            event.stopPropagation();
        }
    })
} else if (currentPage.match(/(^|\W)register($|\W)/)) {
    // on load window
    window.onload = function()
    {
        if (emailCheck.innerHTML === 'Email is already in use') {
            emailCheck.classList.add("d-block")
        }
    }

    // define a an object array of regEx with the message associated with them
    let regexArray = [
    {regex: /^[^]{8,32}$/, msg: "Password must be exactly between 8 and 32 characters long."},
        {regex: /[a-z]/, msg: 'Password must contain at least one lowercase letter.'},
        {regex: /[A-Z]/, msg: 'Password must contain at least one uppercase letter.'},
        {regex: /\d/, msg: "Password must contain at least one number."},
    ]

    // define variable
    let checkResult, checkConfirm;
    let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/
    const email = document.getElementById('emailInput')
    const form = document.getElementsByTagName('form')[0]
    const password = document.getElementById("password")
    const confirmPassword = document.getElementById("confirmPassword")
    const passTest = document.getElementById("passTest")
    const passCheck = document.getElementById("passCheck")
    const emailCheck = document.getElementById("emailCheck")
    const togglePasswordBlock0 = document.getElementsByClassName('input-group-text')[0];
    const togglePasswordBlock1 = document.getElementsByClassName('input-group-text')[1];
    const togglePasswordButton1 = document.getElementById('togglePasswordButton1');
    const togglePasswordButton2 = document.getElementById('togglePasswordButton2');
    const singUp = document.getElementById("signUp")

    function disableButton() {
        signUp.disabled = true;
        signUp.innerHTML = 'Posting..';
    }
    // handels the toggle functionallity
    function togglePassword(element, button){
        if (element.type === 'password') {
            element.type = 'text';
            button.setAttribute('aria-label', 'Hide password.');
            button.classList.replace("bi-eye-slash", "bi-eye");
        } else {
            element.type = 'password';
            button.setAttribute('aria-label', 'Show password as plain text. ' + 'Warning: this will display your password on the screen.');
            button.classList.replace("bi-eye", "bi-eye-slash");
        }
    }

    // add event listeners for each button
    togglePasswordBlock0.addEventListener('click', function() {
        console.log("button1 is clicked")
        togglePassword(password, togglePasswordButton1);
    });

    togglePasswordBlock1.addEventListener('click', function() {
        togglePassword(confirmPassword, togglePasswordButton2);
    });

    email.addEventListener('input', event => {
        checkResult = true
        emailIn = event.target.value
        if(emailRegex.test(emailIn)) {
            emailCheck.innerHTML = '<span style="color: green;">Nice 😊</span>'
        } else {
            checkResult = false
            emailCheck.classList.add('d-block');
            emailCheck.innerHTML = 'Please enter a valid email Adress';
        }
    })
    let passwordIn=''
    // check password for validity using the regexp Array
    password.addEventListener('input', event => {
    passwordIn = event.target.value
    checkResult = true
    regexArray.forEach(item => {
        if(!item.regex.test(passwordIn)) {
        checkResult = false
        passCheck.classList.add('d-block')
        passCheck.innerHTML = `<p>${item.msg}</p>`
        }
        });
        if (checkResult) {
            passCheck.innerHTML = '<span style="color: green;">Nice 😊</span>'
        }
    });
    // check for confimarion
    confirmPassword.addEventListener('input', event => {
        if (passwordIn != event.target.value)
        {
            checkConfirm = false;
            passTest.classList.add('d-block')
        }
        else
        {
            checkConfirm = true;
            passTest.className = passTest.className.replace('d-block', 'gone')
        }
    })

    // prevent form default
    form.addEventListener('submit', event => {
        if (!checkResult || !checkConfirm)
        {
            form.classList.add("was-validated");
            event.preventDefault();
            event.stopPropagation();
        }
    })
} else if (currentPage.match(/(^|\W)confirm($|\W)/)) {
    // on load window
    window.onload = () =>
    {
        if (confirmCheck.innerHTML === 'Please enter a valid confirmation code.') {
            confirmCheck.classList.add("d-block")
        }
    }

    // set up the variables
    const confirmCheck = document.getElementById('confirmCheck');
    const confirmationCode = document.getElementById('confirmationCode');
    const confirmButton = document.querySelector("button[value='confirm']");
    const resendButton = document.querySelector("button[value='resend']");
    const resendCodeCheck = document.querySelector("#resendCodeCheck");

    let regExp = /^[0-9a-zA-Z]{6}$/
    const form = document.getElementsByTagName('form')[0]
    let passCheck = false;

    // add event listener to check for characters
    confirmationCode.addEventListener('input', function(e) {
        codeIn = event.target.value
        if(!regExp.test(codeIn)) {
            confirmCheck.innerHTML = 'Code Must be 6 characters';
            confirmCheck.classList.add("d-block")
        } else {
            passCheck = true;
            confirmCheck.className = confirmCheck.className.replace('d-block', 'gone')
        }
    })

    // add event listener to stop the form in case it did not meat conditions
    form.addEventListener('submit', function(event) {
        // grab the value of the button that was pressed
        let buttonValue = event.submitter.value;
        if (buttonValue !== 'resend' && !passCheck)
        {
            form.classList.add("was-validated");
            event.preventDefault();
            event.stopPropagation();
        }
    })
} else {

    const cat = document.getElementById("cat")
    const sliders = document.querySelectorAll('.swiper-slide')
    const firstCol = document.querySelector('#firstCol')
    const secondCol = document.querySelector('#secondCol')
    let previousSlideId = null;
    let toggleState = false;
    slidersInfo = [{id: 'slide1',title1: 'Front End', title2: 'Back End', paragraph1: "I used <i class='bi bi-filetype-html'></i> for structure, <i class='bi bi-filetype-css'></i> for layout and appearance, <i class='bi bi-bootstrap'></i> for responsiveness, and <i class='bi bi-filetype-js'></i> for interactivity. I used Swiper JavaScript, for the sliders, to showcase my portfolio and projects.", paragraph2: "I used <i class='bi bi-filetype-py'></i> Flask, to make the web app dynamic. I also used SQLite3 for storing the data securely. I used the CS50 library to connect to the SQLite3 database and interact with it effectively."}, {id: 'slide2',title1: 'Undecided', title2: 'Undecided', paragraph1: 'Coming soon. This tap should also be a website, If it is not then I will change the front end title for it to make sence, but till then 👻.', paragraph2: 'This section should describe the details of the back end of the "coming soon" website, right now its lonely since I have not created another website :"(.'}, {id: "slide3", title1: 'To be determined', title2: 'To be determined',paragraph1: "This should be filled out soon enough, tbh I had this amount of slides so that the site does not look off. Hope you enjoyed given me a free therapy session, lol.", paragraph2: 'If you have any ideas for stuff you would like to build or need some help building hmu.'}, {id: "slide4", title1: 'Pending approval', title2: 'Quote',paragraph1: "The good thing about what I am doing currently is that the only approval I need is from myself, thankfully I am very easy to convince.", paragraph2: 'I have this quote by Al mutanabbi that I really like:<p p dir="rtl" lang="ar">إِذا غامَرتَ في شَرَفٍ مَرومٍ فَلا تَقنَع بِما دونَ النُجومِ </p>' }]
    sliders.forEach(slide => {
    slide.addEventListener('click', event => {
        let slideId = slide.getAttribute('id')
        document.getElementsByClassName('main2')[0].scrollIntoView()
        for (let i = 0; i < slidersInfo.length; i++)
        {
            if (slidersInfo[i].id == slideId) {
                if (!toggleState) {
                    firstCol.innerHTML = `<h1 class='text-start'>${slidersInfo[i].title1}</h1>
                    <p class='text-start'>${slidersInfo[i].paragraph1}</p>`
                    firstCol.style.borderRight='2px solid var(--orange)'
                    secondCol.innerHTML = `<h1 class='text-start'>${slidersInfo[i].title2}</h1>
                    <p class='text-start'>${slidersInfo[i].paragraph2}</p>`
                    toggleState = true;
                    previousSlideId = slideId
                } else if (toggleState && previousSlideId === slideId){
                    firstCol.innerHTML = `<div class="alert alert-light meow" role="alert">
                    Hey again, click the slides so I can disappear.
                    </div>
                    <img id="cat" src="/static/images/cat.png" alt="cat" title="Cat image">`
                    firstCol.style.borderRight = ''
                    secondCol.innerHTML = ''
                    previousSlideId = slidersInfo[i].id
                    toggleState = false;
                } else {
                    firstCol.innerHTML = `<h1 class='text-start'>${slidersInfo[i].title1}</h1>
                    <p class='text-start'>${slidersInfo[i].paragraph1}</p>`
                    firstCol.style.borderRight='2px solid var(--orange)'
                    secondCol.innerHTML = `<h1 class='text-start'>${slidersInfo[i].title2}</h1>
                    <p class='text-start'>${slidersInfo[i].paragraph2}</p>`
                    toggleState = false;
                }
        }
      }
    })
  })
  // swiper related code
  var swiper = new Swiper(".mySwiper", {
  effect: "coverflow",
  //   grabCursor: true,
    loop: true,
    centeredSlides: true,
    slidesPerView: 2,
    coverflowEffect: {
      rotate: 30,
      stretch: 0,
      depth: 100,
      modifier: 2,
      slideShadows: true,
    },
    breakpointsInverse: true,
    breakpoints: {
      // when window width is >= 320px
          00: {
            slidesPerView: 1,
          },
          // when window width is >= 640px
          640: {
          slidesPerView: 2,
      }
    },
    keyboard: {
      enabled: true,
    },

    pagination: {
      el: ".swiper-pagination",
      // dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
}