import terminalio
from adafruit_display_text import label
from fourwire import FourWire
import board, busio, os, displayio, digitalio
from adafruit_st7789 import ST7789
import time
from adafruit_hcsr04 import HCSR04

# Declaracion de Pines - Pantalla LCD - Starter Kit for Pico 2
mosi_pin = board.GP7 # MOSI
clk_pin = board.GP6 # Clock
reset_pin = board.GP24 # Reset
cs_pin = board.GP17 # Chip Select
dc_pin = board.GP16 # RS (register select) o DC (data command)
disp_blk = board.GP0 # Pin Led Back Light

# Declaracion pines Sensor Ultrasonico
echo = board.GP8
trig = board.GP9

# Declaracion pines LED
red_pin = board.GP18
yellow_pin = board.GP20
green_pin = board.GP19

# Iniciacion Salida Digial pin LED Rojo
red = digitalio.DigitalInOut(red_pin)
red.direction = digitalio.Direction.OUTPUT

# Iniciacion Salida Digial pin LED Amarillo
yellow = digitalio.DigitalInOut(yellow_pin)
yellow.direction = digitalio.Direction.OUTPUT

# Iniciacion Salida Digial pin LED Verde
green = digitalio.DigitalInOut(green_pin)
green.direction = digitalio.Direction.OUTPUT

# Inicializacion del bus de datos SPI
displayio.release_displays()
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

# Inicializacion Sensor Ultrasonico HCSR04
sensor_ultrasonico = HCSR04(trigger_pin=trig, echo_pin=echo)

# Inicializacion del Display ST7789
display = ST7789(display_bus, width=320 , height=240, backlight_pin=disp_blk, rotation=270)


# Se Inicializa el Contenedor Principal
pantalla = displayio.Group(scale=1, x=0, y=0) # Grupo recibe parametros Scale, x, y (zoom y posicion en la pantalla)
display.root_group = pantalla # Pantalla se declara como grupo principal

# Inicializacion de los Pixeles y Paleta de Colores
color_bitmap = displayio.Bitmap(320, 240, 1) # Cantidad de Pixeles Ancho y Alto y Cantidad de Colores
color_palette = displayio.Palette(1) # Se inicia la paleta de colores
color_palette[0] = 0x00FF00 # Color Verde

# Inicializacion Fondo de Pantalla
fondo_patalla = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
pantalla.append(fondo_patalla) # Se agrega fondo de pantalla al contenerdo del grupo principal

# Se inicializa el contenedor principal de los Textos
text_group = displayio.Group(scale=2, x=11, y=100) # Grupo de Texto recibe parametros Scale, x, y (zoom y posicion)
text= ""

# Se inicializa el area de texto
text_area= label.Label(terminalio.FONT, text=text, color=0x000000) # Recibe parametros Fuente, Texto y Color de texto

# Se agrega el area de texto al grupo de texto
text_group.append(text_area)

# Se agrega el grupo de texto al Contenedor General de la Pantalla
pantalla.append(text_group)

# iniciar LEDs apagados
red.value=False 
yellow.value=False 
green.value=False


while True:

    distance=sensor_ultrasonico.distance
    text_area.text= (f"Distancia: {distance}")
    print(distance) # Imprime valor de distancia en consola
    # Si el valor de distancia es menor de 10, enciende led ROJO
    if distance < 10:
        red.value=True
        yellow.value=False
        green.value=False
    # Si el valor de distancia es mayor de 30, enciende led VERDE
    elif distance > 30:
        red.value=False
        yellow.value=False
        green.value=True
    # Si la distancia esta entre 10 y 30, enciende del AMARILLO
    else:
        red.value=False
        yellow.value=True 
        green.value=False
        
    time.sleep(0.3)
   
   
    
