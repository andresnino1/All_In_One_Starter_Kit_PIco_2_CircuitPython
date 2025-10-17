import terminalio
from adafruit_display_text import label
from fourwire import FourWire
import board, busio, os, displayio
from adafruit_st7789 import ST7789
import time
from adafruit_motor import servo
import pwmio

# Declaracion de Pines - Pantalla LCD - Starter Kit for Pico 2
mosi_pin = board.GP7 # MOSI
clk_pin = board.GP6 # Clock
reset_pin = board.GP24 # Reset
cs_pin = board.GP17 # Chip Select
dc_pin = board.GP16 # RS (register select) o DC (data command)
disp_blk = board.GP0 # Pin Led Back Light

# Declaracion Pines Servo 
servo_pin = board.GP13

# Iniciacion PWM para controlar Servomotor
pwm = pwmio.PWMOut(servo_pin, duty_cycle= 2**15, frequency=50)
my_servo = servo.Servo(pwm)

# Inicializacion del bus de datos SPI
displayio.release_displays()
spi = busio.SPI(clock=clk_pin, MOSI=mosi_pin)
display_bus = FourWire(spi, command=dc_pin, chip_select=cs_pin, reset=reset_pin)


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

print('fin de programa') # imprimir en consola



while True:
    for angle in range(0, 180, 5):  # 0 - 180 grados, 5 grados cada paso.
        my_servo.angle = angle
        text_area.text= (f"Agulo: {angle}")
        time.sleep(0.3)
    for angle in range(180, 0, -5): # 180 - 0 grados, 5 grados cada paso.
        my_servo.angle = angle
        text_area.text= (f"Angulo: {angle}")
        time.sleep(0.3)
   
    
