段 = 0
轉速 = 0
pins.analog_write_pin(AnalogPin.P0, 1023)
pins.analog_write_pin(AnalogPin.P1, 1023)
pins.analog_write_pin(AnalogPin.P2, 1023)
pins.analog_write_pin(AnalogPin.P3, 1023)

def on_forever():
    global 轉速
    轉速 = 段 * 200
basic.forever(on_forever)

def on_forever2():
    global 段
    if input.temperature() >= 27:
        段 = 5
    elif input.temperature() >= 26 and input.temperature() < 27:
        段 = 4
    elif input.temperature() >= 25 and input.temperature() < 26:
        段 = 3
    elif input.temperature() >= 24 and input.temperature() < 25:
        段 = 2
basic.forever(on_forever2)
