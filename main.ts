input.onButtonPressed(Button.AB, function () {
    if (開關 == 1) {
        開關 = 0
    } else {
        開關 = 1
    }
})
let 開關 = 0
pins.analogWritePin(AnalogPin.P0, 0)
pins.analogWritePin(AnalogPin.P1, 0)
開關 = 0
let 段 = 0
let 轉速 = 0
basic.forever(function () {
    if (input.temperature() >= 27) {
        段 = 5
    } else if (input.temperature() >= 26 && input.temperature() < 27) {
        段 = 4
    } else if (input.temperature() >= 25 && input.temperature() < 26) {
        段 = 3
    } else if (input.temperature() >= 24 && input.temperature() < 25) {
        段 = 2
    } else {
        段 = 0
    }
})
basic.forever(function () {
    if (開關 == 1) {
        pins.analogWritePin(AnalogPin.P1, 轉速)
    } else {
        pins.analogWritePin(AnalogPin.P1, 0)
    }
})
basic.forever(function () {
    轉速 = 段 * 200
})
