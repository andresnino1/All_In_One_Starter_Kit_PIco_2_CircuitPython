import terminalio
from adafruit_display_text import label
from fourwire import FourWire
import board, busio, os, displayio
from adafruit_st7789 import ST7789
import adafruit_focaltouch
import time

# Declaracion de Pines - Pantalla LCD - Starter Kit for Pico 2
mosi_pin = board.GP7 # MOSI
clk_pin = board.GP6 # Clock
reset_pin = board.GP24 # Reset
cs_pin = board.GP17 # Chip Select
dc_pin = board.GP16 # RS (register select) o DC (data command)
disp_blk = board.GP0 # Pin Led Back Light

# Declaracion de pines para Touch
i2c_scl = board.GP5
i2c_sda = board.GP4

# Inicializacion del bus de datos SPI
displayio.release_displays()
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)

# Inicializacion del Display ST7789
display = ST7789(display_bus, width=320 , height=240, backlight_pin=disp_blk, rotation=270)

# Iniciacion del bus de datos I2C - para Touch Screen
i2c = busio.I2C(i2c_scl, i2c_sda)

# Iniciacion Touch Screen
touch = adafruit_focaltouch.Adafruit_FocalTouch(i2c)


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
text_group = displayio.Group(scale=3, x=11, y=110) # Grupo de Texto recibe parametros Scale, x, y (zoom y posicion)
text= "curso de robotica"

# Se inicializa el area de texto
text_area= label.Label(terminalio.FONT, text=text, color=0x000000) # Recibe parametros Fuente, Texto y Color de texto

# Se agrega el area de texto al grupo de texto
text_group.append(text_area)

# Se agrega el grupo de texto al Contenedor General de la Pantalla
pantalla.append(text_group)



while True:
    
    my_touch = touch.touches
    
    if len(my_touch) > 0:
        print(f" X: {my_touch[0]['x']} , Y: {my_touch[0]['y']} ")  # Muestra valores de Coordenadas X , Y
        
    else:
        print('No Data')
    
    time.sleep(0.2)
        