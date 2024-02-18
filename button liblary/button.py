from machine import Pin
from time import ticks_ms, sleep

class Button():
    def __init__(self, pin,time_to_click= 500, time_to_press=1000):
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        self.clicks_counter_return = 0
        self.clicks_counter = 0
        self.time_for_last_click = ticks_ms()
        self.time_to_click = time_to_click
        self.time_to_press = time_to_press
        self.button_down = False
        self.pressed_and_hold_times = 0
        self.still_pressed = False
        self.time_start_press = ticks_ms()
        self.flag = False
        
        
    
    def tick(self):
        if self.pin.value():
            self.button_down = False
            self.time_press_start = ticks_ms()
            self.still_pressed = False
            
        if not self.pin.value():
            if not self.flag:
                self.time_start_press = ticks_ms()
                self.flag = True
            self.still_pressed = True
            self.time_for_last_click = ticks_ms()
            if self.button_down == False:
                self.clicks_counter +=1
                self.button_down = True
                self.still_pressed = True
            sleep(0.03)
#         preesed check
        if ticks_ms() - self.time_start_press >=  self.time_to_press:
            if self.button_down:
                self.pressed_and_hold_times = self.clicks_counter
                self.clicks_counter = 0
            self.time_start_press = ticks_ms()
#             chcech click times
        if ticks_ms() - self.time_for_last_click > self.time_to_click:
            self.clicks_counter_return = self.clicks_counter
            self.clicks_counter = 0
#             self.time_for_last_click = ticks_ms()
            self.flag = False
            
            
#     click get
    def one_click(self):
        if  self.clicks_counter_return == 1:
            self.clicks_counter_return = 0
            self.clicks_counter = 0
            return True
        return False
    def double_click(self):
        if self.clicks_counter_return == 2:
            self.clicks_counter_return = 0
            self.clicks_counter = 0
            return True
        return False
    def triple_click(self):
        if self.clicks_counter_return == 3 :
            self.clicks_counter_return = 0
            self.clicks_counter = 0
            return True
        return False

    def is_n_clicks(self, n):
        if self.clicks_counter_return == n:
            self.clicks_counter_return = 0
            self.clicks_counter = 0
            return True
        return False
#     hold get
    def ne_click_and_hold(self):
        if  self.pressed_and_hold_times == 1:
            self.pressed_and_hold_times = 0
            self.clicks_counter = 0
            return True
        return False
    def double_click_and_hold(self):
        if self.pressed_and_hold_times == 2:
            self.pressed_and_hold_times = 0
            self.clicks_counter = 0
            return True
        return False
    def triple_click_and_hold(self):
        if self.pressed_and_hold_times == 3 :
            self.pressed_and_hold_times = 0
            self.clicks_counter = 0
            return True
        return False

    def n_clicks_and_hold(self, n):
        if self.pressed_and_hold_times == n:
            self.pressed_and_hold_times = 0
            self.clicks_counter = 0
            return True
        return False
            
