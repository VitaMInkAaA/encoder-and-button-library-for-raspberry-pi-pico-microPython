from machine import Pin
from button import Button

class Encoder(Button):
    # pins(A pin encoder, direction pin encoder, buttun pin , (optional time to click default 400ms), (optional to to press default 1000ms)
    def __init__(self, clk_pin , dt_pin , sw_pin, time_to_click = 400, time_to_press = 1000):
        super().__init__(sw_pin, time_to_click, time_to_press)
        self.clk_pin = Pin(clk_pin, Pin.IN, Pin.PULL_UP)
        self.dt_pin = Pin(dt_pin, Pin.IN, Pin.PULL_UP)
        self.previous_value = True
        self.button_down = False
        self.dir = None
        

    def tick(self):
        super().tick()
        self.dir = None
        if self.previous_value != self.clk_pin.value():
            if self.clk_pin.value() == False:
                if self.dt_pin.value() == False:
                    self.dir = 'left'
                else:
                    self.dir = 'right'
            self.previous_value = self.clk_pin.value()
        

    def is_left(self):
        if self.dir == 'left':
            return True
        return False
    
    def is_right(self):
        if self.dir == 'right':
            return True
        return False
    
    
    
class Encoder_with_out_button():
    # pins(A pin encoder, direction pin encoder)
    def __init__(self, clk_pin , dt_pin):
        self.clk_pin = Pin(clk_pin, Pin.IN, Pin.PULL_UP)
        self.dt_pin = Pin(dt_pin, Pin.IN, Pin.PULL_UP)
        self.previous_value = True
        self.button_down = False
        self.dir = None
        

    def tick(self):
        self.dir = None
        if self.previous_value != self.clk_pin.value():
            if self.clk_pin.value() == False:
                if self.dt_pin.value() == False:
                    self.dir = 'left'
                else:
                    self.dir = 'right'
            self.previous_value = self.clk_pin.value()
        

    def is_left(self):
        if self.dir == 'left':
            return True
        return False
    
    def is_right(self):
        if self.dir == 'right':
            return True
        return False
    
