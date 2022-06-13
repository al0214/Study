// "15" => 15
// parseInt => string을 number로 바꿔준다
// 데이터 타입을 볼려면 typeof
// isNaN = number인지 아닌지 boolean으로 return(True이면 X False이면 O)
// if = 조건문은 값이 boolean으로 나와야 한다.
// prompt = 응답이 올때까지 계속 대기 (매우 오래된 방법)

// 음주 가능 구별 계산기
const age = parseInt(prompt("How old are you?"));

if (isNaN(age) || age < 0) {
    console.log("Please write a real positive number");
} else if (age < 18) {
    console.log("You are too young.");
} else if (age >= 18 && age <= 50) {
    console.log("You can drink");
} else if (age > 50 && age <= 80) {
    console.log("You should exercise")
} else if (age === 100) {
    console.log("Wow you are wise")
} else if (age > 80) {
    console.log("You can do whatever you want.");
}