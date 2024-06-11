##########Auto-Clicker##########

#####Imports######

import os as o

import sys as s

import tkinter as tk

#import mouse as ms

import pynput.mouse as pnm

import keyboard as ky

import time as tm

#####Window#####

window = tk.Tk()

window.title("auto clicker")

window.geometry("500x250")

window.resizable(False, False)

window.iconphoto(False, tk.PhotoImage(file = o.path.split(o.path.split(__file__)[0])[0] + "/icon/auto-clicker.png")) #Used for the development environment.

#window.iconphoto(False, tk.PhotoImage(file = o.path.split(o.path.split(s.executable)[0])[0] + "/icon/auto-clicker.png")) #Used for the windows executable environment.

#window.iconphoto(False, tk.PhotoImage(file = o.path.split(o.path.split(o.path.split(o.path.split(o.path.split(s.executable)[0])[0])[0])[0])[0] + "/icon/auto-clicker.png")) #Used for the mac application environment.

frame = tk.Canvas(window, width = window.winfo_width(), height = window.winfo_height(), bg = "#FFFFFF")

frame.pack()

def fill(event):
    frame.config(width = window.winfo_width(), height = window.winfo_height())
    
window.bind("<Configure>", fill)

running = True

def closing(): #Terminate the program and tells the loop to end, avoiding updates after window destruction.
    global running
    running = False
    window.destroy()
    
window.protocol("WM_DELETE_WINDOW", closing) #Close the program on window close button pressed / clicked.

window.unbind_all("<<NextWindow>>")
window.unbind_all("<<PrevWindow>>")

window.withdraw()
window.deiconify()

#####Elements#####

black = "#000000"

white = "#FFFFFF"

grey = "#333333"

run_state = False

hotkey_set = True

key_set = True

hotkey_keybind = []

hotkey_text_info = ""

key_keybind = []

key_text_info = ""

right_click = False

left_click = False

mouse = pnm.Controller()

light_mode = True

def run_switch():
    global run_state
    run_state = not run_state

def set_hotkey():
    global running
    global hotkey_set
    global hotkey_keybind
    global hotkey_text_info
    global key_set
    hotkey_set = not hotkey_set
    key_set = True #Prevent setting hotkey and key at the same time.
    if not hotkey_set:
        hotkey_keybind = []
    while running and not hotkey_set:
        if ky.is_pressed("escape"): #if ky.is_pressed("esc"):
            hotkey_set = True
        key = ky.read_key()
        if not key in hotkey_keybind:
            hotkey_keybind.append(key)
        confirm = False
        hotkey_text_info = ""
        for iteration, current in enumerate(hotkey_keybind):
            if iteration == 0:
                hotkey_text_info += current
            else:
                hotkey_text_info += ", " + current
        frame.itemconfig(hotkey_text, text = hotkey_text_info)
        tm.sleep(1)
        while running and not hotkey_set and not confirm:
            if ky.is_pressed("enter") or ky.is_pressed("space"):
                confirm = True
                tm.sleep(1)
            window.update()

def set_key():
    global running
    global key_set
    global key_keybind
    global key_text_info
    global hotkey_set
    key_set = not key_set
    hotkey_set = True #Prevent setting key and hotkey at the same time.
    if not key_set:
        key_keybind = []
    while running and not key_set:
        if ky.is_pressed("escape"): #if ky.is_pressed("esc"):
            key_set = True
        key = ky.read_key()
        if not key in key_keybind:
            key_keybind.append(key)
        confirm = False
        key_text_info = ""
        for iteration, current in enumerate(key_keybind):
            if iteration == 0:
                key_text_info += current
            else:
                key_text_info += ", " + current
        frame.itemconfig(key_text, text = key_text_info)
        tm.sleep(1)
        while running and not key_set and not confirm:
            if ky.is_pressed("enter") or ky.is_pressed("space"):
                confirm = True
                tm.sleep(1)
            window.update()

def right_click_switch():
    global right_click
    right_click = not right_click

def left_click_switch():
    global left_click
    left_click = not left_click

def light_switch():
    global light_mode
    light_mode = not light_mode

def reset():
    global hotkey_keybind
    global key_keybind
    global hotkey_set
    global key_set
    global right_click
    global left_click
    hotkey_keybind = []
    key_keybind = []
    hotkey_set = True
    key_set = True
    right_click = False
    left_click = False

def quiting():
    closing()

def bound(widget):
    return widget.winfo_width(), widget.winfo_height()

def middle(widget):
    width, height = bound(widget)
    return width / 2, height / 2

def dimensions(widget):
    width, height = bound(widget)
    return width, height, width / 2, height / 2

def style(back, fore):
    frame.config(bg = back)
    run_button.config(fg = fore, bg = back, highlightbackground = back)
    hotkey_button.config(fg = fore, bg = back, highlightbackground = back)
    frame.itemconfig(hotkey_text, fill = fore)
    key_button.config(fg = fore, bg = back, highlightbackground = back)
    frame.itemconfig(key_text, fill = fore)
    right_click_button.config(fg = fore, bg = back, highlightbackground = back)
    left_click_button.config(fg = fore, bg = back, highlightbackground = back)
    light_button.config(fg = fore, bg = back, highlightbackground = back)
    reset_button.config(fg = fore, bg = back, highlightbackground = back)
    quit_button.config(fg = fore, bg = back, highlightbackground = back)

run_button = tk.Button(frame, text = "start", bd = 0, command = run_switch)

hotkey_button = tk.Button(frame, text = "hotkey", bd = 0, command = set_hotkey)

hotkey_text = frame.create_text(0, 0, state = "hidden")

key_button = tk.Button(frame, text = "key", bd = 0, command = set_key)

key_text = frame.create_text(0, 0, state = "hidden")

right_click_button = tk.Button(frame, text = "right click", bd = 0, command = right_click_switch)

left_click_button = tk.Button(frame, text = "left click", bd = 0, command = left_click_switch)

light_button = tk.Button(frame, text = "light", bd = 0, command = light_switch)

reset_button = tk.Button(frame, text = "reset", bd = 0, command = reset)

quit_button = tk.Button(frame, text = "quit", bd = 0, command = quiting)

window.withdraw()

window.deiconify()

#####Operations#####

while running: #Loop until program terminated.
    #Get window dimensions.
    size = dimensions(window)
    size, centre = size[:2], size[2:4]

    #Place elements relative to the centre of the window.
    run_button_pos = middle(run_button)
    run_button_pos = [centre[0] - run_button_pos[0], 50 - run_button_pos[1]]

    hotkey_button_pos = middle(hotkey_button)
    hotkey_button_pos = [centre[0] - hotkey_button_pos[0] - 100, 50 - hotkey_button_pos[1]]
    
    hotkey_text_pos = [centre[0] - 100, 80]

    key_button_pos = middle(key_button)
    key_button_pos = [centre[0] - key_button_pos[0] + 100, 50 - key_button_pos[1]]
    
    key_text_pos = [centre[0] + 100, 80]

    right_click_button_pos = middle(right_click_button)
    right_click_button_pos = [centre[0] - right_click_button_pos[0] + 100, size[1] - 100 - right_click_button_pos[1]]
    
    left_click_button_pos = middle(left_click_button)
    left_click_button_pos = [centre[0] - left_click_button_pos[0] - 100, size[1] - 100 - left_click_button_pos[1]]
    
    light_button_pos = middle(light_button)
    light_button_pos = [centre[0] - light_button_pos[0], size[1] - 100 - light_button_pos[1]]
    
    reset_button_pos = middle(reset_button)
    reset_button_pos = [centre[0] - reset_button_pos[0] - 100, size[1] - 50 - reset_button_pos[1]]
    
    quit_button_pos = middle(quit_button)
    quit_button_pos = [centre[0] - quit_button_pos[0] + 100, size[1] - 50 - quit_button_pos[1]]

    #Deploy elements.
    run_button.place(x = run_button_pos[0], y = run_button_pos[1])

    hotkey_button.place(x = hotkey_button_pos[0], y = hotkey_button_pos[1])

    frame.coords(hotkey_text, hotkey_text_pos[0], hotkey_text_pos[1])
    frame.itemconfig(hotkey_text, state = "normal")

    key_button.place(x = key_button_pos[0], y = key_button_pos[1])

    frame.coords(key_text, key_text_pos[0], key_text_pos[1])
    frame.itemconfig(key_text, state = "normal")

    right_click_button.place(x = right_click_button_pos[0], y = right_click_button_pos[1])

    left_click_button.place(x = left_click_button_pos[0], y = left_click_button_pos[1])

    light_button.place(x = light_button_pos[0], y = light_button_pos[1])

    reset_button.place(x = reset_button_pos[0], y = reset_button_pos[1])
    
    quit_button.place(x = quit_button_pos[0], y = quit_button_pos[1])

    #Lighting control.
    if light_mode:
        style(white, black)
    else:
        style(grey, white)

    #Hotkey display control.
    hotkey_text_info = ""

    for iteration, current in enumerate(hotkey_keybind):
        if iteration == 0:
            hotkey_text_info += current
        else:
            hotkey_text_info += ", " + current

    frame.itemconfig(hotkey_text, text = hotkey_text_info)

    #Key display control.
    key_text_info = ""

    for iteration, current in enumerate(key_keybind):
        if iteration == 0:
            key_text_info += current
        else:
            key_text_info += ", " + current

    frame.itemconfig(key_text, text = key_text_info)

    #Mouse display control.
    if left_click:
        left_click_button.config(text = "enabled")
    elif not left_click:
        left_click_button.config(text = "left click")

    if right_click:
        right_click_button.config(text = "enabled")
    elif not right_click:
        right_click_button.config(text = "right click")

    #Detect hotkey toggle.
    hotkey_concatenation = ""
    for iteration, current in enumerate(hotkey_keybind):
        if iteration == 0:
            hotkey_concatenation += current
        else:
            hotkey_concatenation += "+" + current
    if hotkey_concatenation != "":
        if ky.is_pressed(hotkey_concatenation):
            run_state = not run_state
            tm.sleep(1)
    
    #Running display control.
    if run_state:
        run_button.config(text = "stop")
    elif not run_state:
        run_button.config(text = "start")

    #Mouse control.
    if run_state:
        if right_click:
            mouse.press(pnm.Button.right)
            tm.sleep(0.01)
        if left_click:
            mouse.press(pnm.Button.left)
            tm.sleep(0.01)
        if right_click:
            mouse.release(pnm.Button.right)
            tm.sleep(0.01)
        if left_click:
            mouse.release(pnm.Button.left)
            tm.sleep(0.01)

    #Keyboard control.
    if run_state:
        key_concatenation = ""
        for iteration, current in enumerate(key_keybind):
            if iteration == 0:
                key_concatenation += current
            else:
                key_concatenation += "," + current
        if key_concatenation != "":
            ky.press_and_release(key_concatenation)
            tm.sleep(len(key_keybind) * 0.02) #Pause to avoid complete occupation of inputs.

    tm.sleep(0.01) #Pause to avoid complete occupation of listenings.

    window.update() #Update the window.

s.exit() #Kill the program after the main program loop ends.

##########End##########