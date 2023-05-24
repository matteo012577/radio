input.onPinPressed(TouchPin.P0, function () {
    basic.showString(":)")
    radio.sendString(":)")
})
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        basic.showString("A")
    } else if (receivedNumber == 2) {
        basic.showString("B")
    } else if (receivedNumber == 3) {
        basic.showString("C")
    } else if (receivedNumber == 4) {
        basic.showString("D")
    } else if (receivedNumber == 5) {
        basic.showString("E")
    } else if (receivedNumber == 6) {
        basic.showString("F")
    } else if (receivedNumber == 7) {
        basic.showString("G")
    } else if (receivedNumber == 8) {
        basic.showString("H")
    } else if (receivedNumber == 9) {
        basic.showString("I")
    } else if (receivedNumber == 10) {
        basic.showString("J")
    } else if (receivedNumber == 11) {
        basic.showString("K")
    } else if (receivedNumber == 12) {
        basic.showString("L")
    } else if (receivedNumber == 13) {
        basic.showString("M")
    } else if (receivedNumber == 14) {
        basic.showString("N")
    } else if (receivedNumber == 15) {
        basic.showString("O")
    } else if (receivedNumber == 16) {
        basic.showString("P")
    } else if (receivedNumber == 17) {
        basic.showString("Q")
    } else if (receivedNumber == 18) {
        basic.showString("R")
    } else if (receivedNumber == 19) {
        basic.showString("S")
    } else if (receivedNumber == 20) {
        basic.showString("T")
    } else if (receivedNumber == 21) {
        basic.showString("U")
    } else if (receivedNumber == 22) {
        basic.showString("V")
    } else if (receivedNumber == 23) {
        basic.showString("W")
    } else if (receivedNumber == 24) {
        basic.showString("X")
    } else if (receivedNumber == 25) {
        basic.showString("Y")
    } else if (receivedNumber == 26) {
        basic.showString("Z")
    } else if (receivedNumber > 0) {
        basic.showString("ERROR")
    } else {
    	
    }
})
input.onButtonPressed(Button.A, function () {
    leters += -1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    radio.sendString("")
    basic.clearScreen()
})
input.onPinPressed(TouchPin.P2, function () {
    basic.showString(":(")
    radio.sendString(":(")
})
input.onButtonPressed(Button.AB, function () {
    radio.sendNumber(leters)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function () {
    leters += 1
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showString(";)")
    radio.sendString(";)")
})
let leters = 0
radio.setGroup(1)
basic.forever(function () {
    if (leters == 1) {
        basic.showString("A")
    } else if (leters == 2) {
        basic.showString("B")
    } else if (leters == 3) {
        basic.showString("C")
    } else if (leters == 4) {
        basic.showString("D")
    } else if (leters == 5) {
        basic.showString("E")
    } else if (leters == 6) {
        basic.showString("F")
    } else if (leters == 7) {
        basic.showString("G")
    } else if (leters == 8) {
        basic.showString("H")
    } else if (leters == 9) {
        basic.showString("I")
    } else if (leters == 10) {
        basic.showString("J")
    } else if (leters == 11) {
        basic.showString("K")
    } else if (leters == 12) {
        basic.showString("L")
    } else if (leters == 13) {
        basic.showString("M")
    } else if (leters == 14) {
        basic.showString("N")
    } else if (leters == 15) {
        basic.showString("O")
    } else if (leters == 16) {
        basic.showString("P")
    } else if (leters == 17) {
        basic.showString("Q")
    } else if (leters == 18) {
        basic.showString("R")
    } else if (leters == 19) {
        basic.showString("S")
    } else if (leters == 20) {
        basic.showString("T")
    } else if (leters == 21) {
        basic.showString("U")
    } else if (leters == 22) {
        basic.showString("V")
    } else if (leters == 23) {
        basic.showString("W")
    } else if (leters == 24) {
        basic.showString("X")
    } else if (leters == 25) {
        basic.showString("Y")
    } else if (leters == 26) {
        basic.showString("Z")
    } else if (leters > 0) {
        basic.showString("ERROR")
    } else if (leters < 0) {
        basic.showString("ERROR")
    } else {
    	
    }
})
