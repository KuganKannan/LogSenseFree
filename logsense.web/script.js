/* ===============================
   SCROLL REVEAL ANIMATION
================================= */

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add("show");
        }
    });
}, {
    threshold: 0.15
});

document.querySelectorAll(".hidden").forEach((el) => {
    observer.observe(el);
});


/* ===============================
   TERMINAL TYPING EFFECT
================================= */

const typingElement = document.getElementById("typing");

if (typingElement) {

    const text = "$ logsense app.log";
    let index = 0;

    function typeWriter() {

        if (index < text.length) {
            typingElement.innerHTML += text.charAt(index);
            index++;
            setTimeout(typeWriter, 45);
        }

    }

    window.addEventListener("load", typeWriter);
}


/* ===============================
   SMOOTH NAVIGATION SCROLL
================================= */

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function(e) {

        e.preventDefault();

        const target = document.querySelector(this.getAttribute("href"));

        if(target){

            target.scrollIntoView({
                behavior: "smooth"
            });

        }

    });

});


/* ===============================
   NAVBAR BLUR ON SCROLL
================================= */

const header = document.querySelector("header");

window.addEventListener("scroll", () => {

    if (window.scrollY > 40) {

        header.style.backdropFilter = "blur(10px)";
        header.style.background = "rgba(15,23,42,0.8)";

    } else {

        header.style.backdropFilter = "none";
        header.style.background = "transparent";

    }

});


/* ===============================
   PARALLAX HERO EFFECT
================================= */

const hero = document.querySelector(".hero");

window.addEventListener("scroll", () => {

    if(hero){

        let offset = window.pageYOffset;
        hero.style.backgroundPositionY = offset * 0.4 + "px";

    }

});


/* ===============================
   CARD TILT HOVER EFFECT
================================= */

const cards = document.querySelectorAll(".card, .usage-card");

cards.forEach(card => {

    card.addEventListener("mousemove", (e) => {

        const rect = card.getBoundingClientRect();

        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        const centerX = rect.width / 2;
        const centerY = rect.height / 2;

        const rotateX = -(y - centerY) / 15;
        const rotateY = (x - centerX) / 15;

        card.style.transform =
            `perspective(600px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;

    });

    card.addEventListener("mouseleave", () => {

        card.style.transform =
            "perspective(600px) rotateX(0deg) rotateY(0deg)";

    });

});


/* ===============================
   IMAGE REVEAL ANIMATION
================================= */

const images = document.querySelectorAll("img");

const imageObserver = new IntersectionObserver((entries) => {

    entries.forEach(entry => {

        if(entry.isIntersecting){

            entry.target.style.opacity = 1;
            entry.target.style.transform = "scale(1)";

        }

    });

}, {
    threshold: 0.2
});

images.forEach(img => {

    img.style.opacity = 0;
    img.style.transform = "scale(0.95)";
    img.style.transition = "all 0.8s ease";

    imageObserver.observe(img);

});


/* ===============================
   BUTTON RIPPLE EFFECT
================================= */

const buttons = document.querySelectorAll(".btn");

buttons.forEach(button => {

    button.addEventListener("click", function(e){

        const circle = document.createElement("span");

        const diameter = Math.max(this.clientWidth, this.clientHeight);
        const radius = diameter / 2;

        circle.style.width = circle.style.height = `${diameter}px`;
        circle.style.left = `${e.clientX - this.offsetLeft - radius}px`;
        circle.style.top = `${e.clientY - this.offsetTop - radius}px`;

        circle.classList.add("ripple");

        const ripple = this.getElementsByClassName("ripple")[0];

        if(ripple){
            ripple.remove();
        }

        this.appendChild(circle);

    });

});


/* ===============================
   FLOATING ELEMENTS
================================= */

const floating = document.querySelectorAll(".floating");

floating.forEach(el => {

    let position = 0;

    setInterval(() => {

        position += 0.5;

        el.style.transform =
            `translateY(${Math.sin(position) * 5}px)`;

    }, 30);

});


/* ===============================
   COUNTER ANIMATION (OPTIONAL)
================================= */

const counters = document.querySelectorAll(".counter");

const speed = 200;

counters.forEach(counter => {

    const updateCount = () => {

        const target = +counter.getAttribute("data-target");
        const count = +counter.innerText;

        const increment = target / speed;

        if(count < target){

            counter.innerText = Math.ceil(count + increment);
            setTimeout(updateCount, 10);

        } else {

            counter.innerText = target;

        }

    };

    updateCount();

});