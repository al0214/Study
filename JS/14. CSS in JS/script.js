const h1 = document.querySelector("div.hello:first-child h1");

function handleMouseEnter() {
    const currentColor = h1.style.color;
    let newColor;
    if (currentColor === "blue") {
        newColor = "tomato";
    } else {
        newColor = "blue";
    }
    h1.style.color = newColor;
}

h1.addEventListener("click", handleMouseEnter);

//title.style.color = "color" 색갈 변경