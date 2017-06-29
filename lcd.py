import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("hello", 1)
mylcd.lcd_display_string("PM1: ", 2)
mylcd.lcd_display_string("PM2.5: ", 3)
mylcd.lcd_display_string("PM10", 4)
            

