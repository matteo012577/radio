def on_pin_pressed_p0():
    basic.show_string(":)")
    radio.send_string(":)")
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        basic.show_string("A")
    elif receivedNumber == 2:
        basic.show_string("B")
    elif receivedNumber == 3:
        basic.show_string("C")
    elif receivedNumber == 4:
        basic.show_string("D")
    elif receivedNumber == 5:
        basic.show_string("E")
    elif receivedNumber == 6:
        basic.show_string("F")
    elif receivedNumber == 7:
        basic.show_string("G")
    elif receivedNumber == 8:
        basic.show_string("H")
    elif receivedNumber == 9:
        basic.show_string("I")
    elif receivedNumber == 10:
        basic.show_string("J")
    elif receivedNumber == 11:
        basic.show_string("K")
    elif receivedNumber == 12:
        basic.show_string("L")
    elif receivedNumber == 13:
        basic.show_string("M")
    elif receivedNumber == 14:
        basic.show_string("N")
    elif receivedNumber == 15:
        basic.show_string("O")
    elif receivedNumber == 16:
        basic.show_string("P")
    elif receivedNumber == 17:
        basic.show_string("Q")
    elif receivedNumber == 18:
        basic.show_string("R")
    elif receivedNumber == 19:
        basic.show_string("S")
    elif receivedNumber == 20:
        basic.show_string("T")
    elif receivedNumber == 21:
        basic.show_string("U")
    elif receivedNumber == 22:
        basic.show_string("V")
    elif receivedNumber == 23:
        basic.show_string("W")
    elif receivedNumber == 24:
        basic.show_string("X")
    elif receivedNumber == 25:
        basic.show_string("Y")
    elif receivedNumber == 26:
        basic.show_string("Z")
    elif receivedNumber > 0:
        basic.show_string("ERROR")
    else:
        pass
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global leters
    leters += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_logo_pressed():
    radio.send_string("")
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_pin_pressed_p2():
    basic.show_string(":(")
    radio.send_string(":(")
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_ab():
    radio.send_number(leters)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global leters
    leters += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.show_string(";)")
    radio.send_string(";)")
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

leters = 0
radio.set_group(1)

def on_forever():
    if leters == 1:
        basic.show_string("A")
    elif leters == 2:
        basic.show_string("B")
    elif leters == 3:
        basic.show_string("C")
    elif leters == 4:
        basic.show_string("D")
    elif leters == 5:
        basic.show_string("E")
    elif leters == 6:
        basic.show_string("F")
    elif leters == 7:
        basic.show_string("G")
    elif leters == 8:
        basic.show_string("H")
    elif leters == 9:
        basic.show_string("I")
    elif leters == 10:
        basic.show_string("J")
    elif leters == 11:
        basic.show_string("K")
    elif leters == 12:
        basic.show_string("L")
    elif leters == 13:
        basic.show_string("M")
    elif leters == 14:
        basic.show_string("N")
    elif leters == 15:
        basic.show_string("O")
    elif leters == 16:
        basic.show_string("P")
    elif leters == 17:
        basic.show_string("Q")
    elif leters == 18:
        basic.show_string("R")
    elif leters == 19:
        basic.show_string("S")
    elif leters == 20:
        basic.show_string("T")
    elif leters == 21:
        basic.show_string("U")
    elif leters == 22:
        basic.show_string("V")
    elif leters == 23:
        basic.show_string("W")
    elif leters == 24:
        basic.show_string("X")
    elif leters == 25:
        basic.show_string("Y")
    elif leters == 26:
        basic.show_string("Z")
    elif leters > 0:
        basic.show_string("ERROR")
    elif leters < 0:
        basic.show_string("ERROR")
    else:
        pass
basic.forever(on_forever)
