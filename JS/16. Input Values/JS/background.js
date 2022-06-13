const images = [ "0.jpeg", "1.jpeg", "2.jpeg" ]

const changeImage = images[Math.floor(Math.random() * images.length)]
const bgImages = document.createElement("img");


bgImages.src = `img/${changeImage}`;
bgImages.classList = "bgpaint";


document.body.appendChild(bgImages);