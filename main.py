led_verte = pyb.Pin( 'X1', pyb.Pin.OUT_PP)
led_bleu = pyb.Pin( 'X2', pyb.Pin.OUT_PP)

while True:
    led_verte.high()
    led_bleu.low()
    pyb.delay(150)
    led_verte.low()
    led_bleu.high()
    pyb.delay(150)