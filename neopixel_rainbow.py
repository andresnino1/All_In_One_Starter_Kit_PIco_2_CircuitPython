import time
import board, digitalio
import neopixel
import rainbowio

# Inicializacion de pines de control NeoPixels
pixel_pin = board.GP22
pixel_enable = board.GP23 # Pin de habilitacion
num_pixels = 20 # Cantidad de Pixeles del Kit

pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)
enable = digitalio.DigitalInOut(pixel_enable)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True # Poner pin de habilitacion en ALTO

i=0

while True:

    color = rainbowio.colorwheel(i % 256)
    pixel.fill(color)
    pixel.show()
    i += 1
    time.sleep(0.05)
    

