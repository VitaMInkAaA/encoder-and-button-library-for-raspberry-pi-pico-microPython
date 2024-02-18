from button import Button

#declaration button
but = Button(18)


while True:
    #I used tick to update encoder or button when while start again, better way its use .tick() at the beginning while before your code
    
    but.tick()
    
    
    # ussung button
    if but.one_click():
        print('1111')
    if but.double_click():
        print('2')
    if but.triple_click():
        print('3')
    if but.is_n_clicks(5):
        print('5')
        
    if but.ne_click_and_hold():
        print('1111p')
    if but.double_click_and_hold():
        print('2p')
    if but.triple_click_and_hold():
        print('3p')
    if but.n_clicks_and_hold(5):
        print('5p')
    