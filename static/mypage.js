const button = document.querySelector("#plus");
const button1 = document.querySelector("#plus1");
const button2 = document.querySelector("#plus2");
const accordion = document.querySelector("#accord");
const accordion1 = document.querySelector("#accord1");
const accordion2 = document.querySelector("#accord2");

button.addEventListener('click',()=>{
    
    if(accordion.classList.contains('accordion-content')==true){
        accordion.classList.toggle('active');
        accordion.classList.contains('active') ? button.innerHTML = '-' : button.innerHTML='+';
    }
})

button1.addEventListener('click',()=>{
    if(accordion.classList.contains('accordion-content')==true){
        accordion1.classList.toggle('active');
        accordion1.classList.contains('active') ? button1.innerHTML = '-' : button1.innerHTML = '+';
    }
    
})

button2.addEventListener('click',()=>{
    if(accordion.classList.contains('accordion-content')==true){
        accordion2.classList.toggle('active');
        accordion2.classList.contains('active') ? button2.innerHTML = '-' : button2.innerHTML = '+';
    }
})

//myprofile dom
const prof = document.querySelector(".spp");
const cross = document.getElementById("cros");
const display = document.querySelector(".display");
const content = document.querySelector(".content");
const profile = document.querySelector(".profile");
const dat = document.querySelector(".dat");
const dat1 = document.querySelector(".dat1");
const dat2 = document.querySelector(".dat2");
const bookingbutton = document.getElementById("booking");
const bookingbutton1 = document.getElementById("booking1");
const bookingbutton2 = document.getElementById("booking2");

prof.addEventListener('click',()=>{
    
    display.classList.add("active")?.classList.add("active");
    display.classList.remove("nonactive");
    content.classList.add("filter");
    profile.classList.add("filter");
    

});

cross.addEventListener('click',()=>{
    display.classList.add("nonactive")?.classList.add("nonactive");
    display.classList.remove("active");
    content.classList.remove("filter");
    profile.classList.remove("filter");
})

bookingbutton.addEventListener("click",()=>{
   dat.classList.add("active")?.classList.add("active");
   dat.classList.remove("nonactive");  
})

bookingbutton1.addEventListener("click",()=>{
    dat1.classList.add("active")?.classList.add("active");
    dat1.classList.remove("nonactive");  
 })

 bookingbutton2.addEventListener("click",()=>{
    dat2.classList.add("active")?.classList.add("active");
    dat2.classList.remove("nonactive");  
 })



