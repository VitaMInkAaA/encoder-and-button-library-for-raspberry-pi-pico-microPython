from encoder import Encoder, Encoder_with_out_button


#declaration encoder with button 
enkoder = Encoder(16,17,18)

#I used tick to update encoder or button when while start again, better way its use .tick() at the beginning while before your code 

while True:
#     ussing encoder with buttno
    enkoder.tick()
    if enkoder.is_right():
        print('right')
    if enkoder.is_left():
        print('left')
    
    if enkoder.one_click():
        print('1111')
    if enkoder.double_click():
        print('2')
    if enkoder.triple_click():
        print('3')
    if enkoder.is_n_clicks(5):
        print('5')
        
    if enkoder.ne_click_and_hold():
        print('1111p')
    if enkoder.double_click_and_hold():
        print('2p')
    if enkoder.triple_click_and_hold():
        print('3p')
    if enkoder.n_clicks_and_hold(5):
        print('5p')





    


