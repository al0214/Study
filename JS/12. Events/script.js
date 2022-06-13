const h1 = document.querySelector("div.hello:first-child h1");


function handleTitleCluck() {
    h1.style.color = "blue";
}

function handleMouseEnter() {
    h1.innerText = "Mouse is here!"
}

function handleMouseLeave() {
    h1.innerText = "Mouse is gone!"
}

function handleWindowResize() {
    document.body.style.backgroundColor = "tomato"
}

function handleWindowCopy() {
    alert("copier!")
}

function handleWindowOffline() {
    alert("SOS no WIFI")
}

function handleWindowOnline() {
    alert("So good")
}

h1.onclick = handleTitleCluck;
h1.onmouseenter = handleMouseEnter;
h1.onmouseleave = handleMouseLeave;
window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
window.addEventListener("offline", handleWindowOffline);
window.addEventListener("online", handleWindowOnline);

//title.style.color = "color" 색갈 변경