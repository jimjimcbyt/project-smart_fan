def on_button_pressed_ab():
    global 段
    段 = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

轉速 = 0
段 = 0
pins.analog_write_pin(AnalogPin.P0, 0)
pins.analog_write_pin(AnalogPin.P1, 0)

def on_forever():
    global 段
    if input.temperature() >= 27:
        段 = 5
    elif input.temperature() >= 26 and input.temperature() < 27:
        段 = 4
    elif input.temperature() >= 25 and input.temperature() < 26:
        段 = 3
    elif input.temperature() >= 24 and input.temperature() < 25:
        段 = 2
basic.forever(on_forever)

def on_forever2():
    pins.analog_write_pin(AnalogPin.P1, 轉速)
basic.forever(on_forever2)

def on_forever3():
    global 轉速
    轉速 = 段 * 200
basic.forever(on_forever3)
