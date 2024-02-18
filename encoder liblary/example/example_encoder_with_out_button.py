from encoder import Encoder_with_out_button


#I used tick to update encoder or button when while start again, better way its use .tick() at the beginning while before your code 

enkoder_with_out_button = Encoder_with_out_button(16,17)

while True:
#     ussing encoder with out buttno
    enkoder_with_out_button.tick()
    if enkoder_with_out_button.is_right():
        print('right')
    if enkoder_with_out_button.is_left():
        print('left')