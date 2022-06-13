
const API_KEY = "c818c9ad59997d8c3df5e458ec8de8fa"


// lat = 위도
// lon = 경도
// 위치를 불러오는 함수
function onGeoOk(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
    fetch(url).then(response => response.json()).then(data => {
        const city = document.querySelector("#weather span:first-child")
        const weather = document.querySelector("#weather span:last-child")
        city.innerText = `현재 위치 ${data.name}`;
        weather.innerText = `날씨 :${data.weather[0].main} 온도 :${data.main.temp}°C`;
    })

}

function onGeoError() {
    console.log("Lost your location, No weather Data ");
}



// 유저의 좌표를 가져온다.
navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);

