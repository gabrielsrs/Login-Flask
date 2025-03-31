let slider = document.querySelector('.social-login');
let contentItems = document.querySelector('.social-content');
let items = document.querySelectorAll('.item');

const heightItemsContent = slider.offsetHeight;
let scrollPos;
let interval;

items.forEach(item => {
 let clone = item.cloneNode(true)
 clone.classList.add('clone')
 contentItems.appendChild(clone)
})

function scrollUpdate() {
 scrollPos = slider.scrollTop
 if(scrollPos >= heightItemsContent) {
  slider.scrollTo({top: 1})
 }else if(scrollPos <= 0) {
  slider.scrollTo({top: heightItemsContent - 1})
 }

 requestAnimationFrame(scrollUpdate)
}

function animation(clear) {
    if(clear) {
        clearInterval(interval)
    } else {
        interval = setInterval(function() {slider.scrollBy(0,1)}, 40)
    }
}

slider.addEventListener("mouseenter", disable);
slider.addEventListener("mouseleave", enable);

function disable(){
    animation(true)
}

function enable(){
    animation()
}

(function onLoad() {
 slider.scrollTo({top: 1})
 scrollUpdate();
 enable()
}())
