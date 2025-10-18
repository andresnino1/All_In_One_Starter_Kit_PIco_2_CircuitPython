import time
import board, digitalio
import neopixel


# Inicializacion de pines de control NeoPixels
pixel_pin = board.GP22
pixel_enable = board.GP23 # Pin de habilitacion
num_pixels = 20 # Cantidad de Pixeles del Kit

pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)
enable = digitalio.DigitalInOut(pixel_enable)
enable.direction = digitalio.Direction.OUTPUT
enable.value = True # Poner pin de habilitacion en ALTO

# Paleta de Colores
RED = (255,0,0)
YELLOW = (255,150,0)
GREEN = (0,255,0)


while True:
    
    pixel[5]= RED
    pixel.show()

    

