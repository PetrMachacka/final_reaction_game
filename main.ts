pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let P1 = 0
let P2 = 0
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    P1 = 1
    console.log("P1 1")
})
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    
    P2 = 1
    console.log("P2 1")
})
basic.forever(function forever() {
    
    P1 = 0
    P2 = 0
    basic.clearScreen()
    let random = randint(3000, 6000)
    basic.pause(random)
    if (2 < 1) {
        console.log("")
    } else if (P1 && P2 == 1) {
        basic.showString("C")
    } else if (P1 == 1) {
        basic.showNumber(2)
    } else if (P2 == 1) {
        basic.showNumber(1)
    } else {
        basic.showLeds(`
        # . # . #
        . # # # .
        . . # . .
        . # . # .
        # . . . #
        `, 0)
        music.playTone(Note.C, 1500)
        if (P1 && P2 == 1) {
            basic.showString("C")
        } else if (P1 == 1) {
            basic.showNumber(1)
        } else if (P2 == 1) {
            basic.showNumber(2)
        } else {
            basic.showIcon(IconNames.Sad)
        }
        
        basic.pause(3000)
    }
    
})
