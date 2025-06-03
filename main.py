input.onButtonPressed(Button.AB, function () {
    段 = 0
})
let 轉速 = 0
let 段 = 0
pins.analogWritePin(AnalogPin.P0, 0)
pins.analogWritePin(AnalogPin.P1, 0)
basic.forever(function () {
    if (input.temperature() >= 27) {
        段 = 5
    } else if (input.temperature() >= 26 && input.temperature() < 27) {
        段 = 4
    } else if (input.temperature() >= 25 && input.temperature() < 26) {
        段 = 3
    } else if (input.temperature() >= 24 && input.temperature() < 25) {
        段 = 2
    }
})
basic.forever(function () {
    pins.analogWritePin(AnalogPin.P1, 轉速)
})
basic.forever(function () {
    轉速 = 段 * 200
})
