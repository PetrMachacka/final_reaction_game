pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)

P1 = 0
P2 = 0

def on_pin_pressed_p1():
    global P1
    P1 = 1
    print("P1 1")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
def on_pin_pressed_p2():
    global P2
    P2 = 1
    print("P2 1")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def forever():
    global P1, P2
    P1 = 0
    P2 = 0
    basic.clear_screen()
    random = randint(3000, 6000)
    basic.pause(random)
    if 2 < 1:
        print("")
    elif P1 and P2 == 1:
            basic.show_string("C")
    elif P1 == 1:
        basic.show_number(2)
    elif P2 == 1:
        basic.show_number(1)
    else:   
        basic.show_leds("""
        # . # . #
        . # # # .
        . . # . .
        . # . # .
        # . . . #
        """, 0)
        music.play_tone(Note.C, 1500)
        if P1 and P2 == 1:
            basic.show_string("C")
        elif P1 == 1:
            basic.show_number(1)
        elif P2 == 1:
            basic.show_number(2)
        else:
            basic.show_icon(IconNames.SAD)
        basic.pause(3000)
basic.forever(forever)