轉速 = 0
if input.temperature() >= 27:
    pass
else:
    pass

def on_forever():
    global 轉速
    段 = 0
    轉速 = 段 * 200
basic.forever(on_forever)
