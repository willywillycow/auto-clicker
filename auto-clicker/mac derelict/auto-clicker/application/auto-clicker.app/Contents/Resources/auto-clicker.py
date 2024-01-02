##########auto clicker##########

#####import######

import os as o

import sys as s

import tkinter as tk

#import mouse as ms

import pynput.mouse as pnm

import keyboard as ky

import time as tm

import threading as tr

#####window#####

window = tk.Tk()

window.title("auto clicker")

window.geometry("500x250")

window.resizable(False, False)

#window.iconphoto(False, tk.PhotoImage(file = o.path.split(o.path.split(__file__)[0])[0] + "/icon/auto-clicker.png")) #Used for the development environment.

#window.iconphoto(False, tk.PhotoImage(file = o.path.split(o.path.split(s.executable)[0])[0] + "/icon/auto-clicker.png")) #Used for the windows executable environment.

window.iconphoto(False, tk.PhotoImage(file = o.path.split(o.path.split(o.path.split(o.path.split(o.path.split(s.executable)[0])[0])[0])[0])[0] + "/icon/auto-clicker.png")) #Used for the mac application environment.

frame = tk.Canvas(window, width = window.winfo_width(), height = window.winfo_height(), bg = "#FFFFFF")

frame.pack()

def fill(event):
    frame.config(width = window.winfo_width(), height = window.winfo_height())
    
window.bind("<Configure>", fill)

running = True

def closing():
    global running
    running = False
    window.destroy()
    
window.protocol("WM_DELETE_WINDOW", closing)

window.unbind_all("<<NextWindow>>")
window.unbind_all("<<PrevWindow>>")

window.withdraw()
window.deiconify()

#####elements#####

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

light_mode = "light"

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
    key_set = True
    if not hotkey_set:
        hotkey_keybind = []
    while running and not hotkey_set:
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
    hotkey_set = True
    if not key_set:
        key_keybind = []
    while running and not key_set:
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
    if light_mode == "light":
        light_mode = "dark"
    elif light_mode == "dark":
        light_mode = "light"

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

#####operation#####

while running:
    #Place elements to place relative to the centre of the window.
    run_button.place(x = window.winfo_width() / 2 - run_button.winfo_width() / 2, y = 50 - run_button.winfo_height() / 2)
    hotkey_button.place(x = window.winfo_width() / 2 - hotkey_button.winfo_width() / 2 - 100, y = 50 - hotkey_button.winfo_height() / 2)
    frame.coords(hotkey_text, window.winfo_width() / 2 - 100, 80)
    frame.itemconfig(hotkey_text, state = "normal")
    key_button.place(x = window.winfo_width() / 2 - key_button.winfo_width() / 2 + 100, y = 50 - key_button.winfo_height() / 2)
    frame.coords(key_text, window.winfo_width() / 2 + 100, 80)
    frame.itemconfig(key_text, state = "normal")
    right_click_button.place(x = window.winfo_width() / 2 - right_click_button.winfo_width() / 2 + 100, y = window.winfo_height() - 100 - right_click_button.winfo_height() / 2)
    left_click_button.place(x = window.winfo_width() / 2 - left_click_button.winfo_width() / 2 - 100, y = window.winfo_height() - 100 - left_click_button.winfo_height() / 2)
    light_button.place(x = window.winfo_width() / 2 - light_button.winfo_width() / 2, y = window.winfo_height() - 100 - light_button.winfo_height() / 2)
    reset_button.place(x = window.winfo_width() / 2 - reset_button.winfo_width() / 2 - 100, y = window.winfo_height() - 50 - reset_button.winfo_height() / 2)
    quit_button.place(x = window.winfo_width() / 2 - quit_button.winfo_width() / 2 + 100, y = window.winfo_height() - 50 - quit_button.winfo_height() / 2)
    
    #Lighting control.
    if light_mode == "light":
        frame.config(bg = "#FFFFFF")
        run_button.config(fg = "#000000", bg = "#FFFFFF", highlightbackground = "#FFFFFF")
        hotkey_button.config(fg = "#000000", bg = "#FFFFFF", highlightbackground = "#FFFFFF")
        frame.itemconfig(hotkey_text, fill = "#000000")
        key_button.config(fg = "#000000", bg = "#FFFFFF", highlightbackground = "#FFFFFF")
        frame.itemconfig(key_text, fill = "#000000")
        right_click_button.config(fg = "#000000", bg = "#FFFFFF", highlightbackground = "#FFFFFF")
        left_click_button.config(fg = "#000000", bg = "#FFFFFF", highlightbackground = "#FFFFFF")
        light_button.config(fg = "#000000", bg = "#FFFFFF", highlightbackground = "#FFFFFF")
        reset_button.config(fg = "#000000", bg = "#FFFFFF", highlightbackground = "#FFFFFF")
        quit_button.config(fg = "#000000", bg = "#FFFFFF", highlightbackground = "#FFFFFF")
    elif light_mode == "dark":
        frame.config(bg = "#333333")
        run_button.config(fg = "#FFFFFF", bg = "#333333", highlightbackground = "#333333")
        hotkey_button.config(fg = "#FFFFFF", bg = "#333333", highlightbackground = "#333333")
        frame.itemconfig(hotkey_text, fill = "#FFFFFF")
        key_button.config(fg = "#FFFFFF", bg = "#333333", highlightbackground = "#333333")
        frame.itemconfig(key_text, fill = "#FFFFFF")
        right_click_button.config(fg = "#FFFFFF", bg = "#333333", highlightbackground = "#333333")
        left_click_button.config(fg = "#FFFFFF", bg = "#333333", highlightbackground = "#333333")
        light_button.config(fg = "#FFFFFF", bg = "#333333", highlightbackground = "#333333")
        reset_button.config(fg = "#FFFFFF", bg = "#333333", highlightbackground = "#333333")
        quit_button.config(fg = "#FFFFFF", bg = "#333333", highlightbackground = "#333333")

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

    #Detect hotkey toggles.
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

    #Running.
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
            tm.sleep(len(key_keybind) * 0.02)

    tm.sleep(0.01)

    window.update()

s.exit() #Kill the program after the loop ends.

##########end##########
