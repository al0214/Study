const calculator = {
    plus: function(a, b) {
        return a + b;
    },

    minus: function(a, b) {
        return a - b;
    },

    times: function(a, b) {
        return a * b;
    },

    divide: function(a, b) {
        return a / b;
    },

    power: function(a, b) {
        return a ** b;
    },

}

const plusResult = calculator.plus(10, 20)
const minusResult = calculator.minus(10, 20)
const timeResult = calculator.times(10, 20)
const divideResult = calculator.divide(10, 20)
const powerResult = calculator.power(10, 20)