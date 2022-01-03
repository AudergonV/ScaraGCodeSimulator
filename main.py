#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2021, Vincent Audergon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
Main file of the program
"""

__author__ = "Vincent Audergon"
__date__ = "2022.01.04"
__version__ = "1.0"
__email__ = "vincent.audergon@bluewin.ch"
__userid__ = "vincent.audergon"

import tkinter
import time

from scara import Scara
from gcode_reader import GCodeReader
from params import Params

def main():
    """Main method"""
    #Inital values
    params = Params()
    arms_length = params.height/4
    refresh_time = 0.1/params.speed
    origin = [params.width/2,params.height/2]
    old_position = [0,0]
    #Creating objects
    root = tkinter.Tk() # Window
    root.title("Scara GCode simulator")
    scara = Scara(arms_length, params.microsteps) # Scara simulator
    gcode = GCodeReader()
    canvas = tkinter.Canvas(root, bg="white", height=params.height, width=params.width)
    # Trying to open the gcode file
    gcode.OpenGCode(params.filename)
    # Display the canvas
    canvas.pack()
    # Arms lines
    armA = canvas.create_line(0,0,0,0, fill="blue");
    armB = canvas.create_line(0,0,0,0, fill="blue");
    # Main loop
    while gcode.HasMoreLines():
        instruction = gcode.GetNextInstruction()
        # Interpreting GCode
        if (len(instruction) >= 3):
            match instruction[0]:
                case "G01":
                    scara.rotate_A(float(instruction[1][1:]))
                    scara.rotate_B(float(instruction[2][1:]))
        # Refresh the canvas
        print_position(old_position, scara.get_head_position(), canvas, origin)
        print_arms(armA, armB, scara.get_B_position(), scara.get_head_position(), canvas, origin)
        old_position = scara.get_head_position()
        root.update()
        # Wait before the next iteration
        time.sleep(refresh_time)

def print_position(old_position, new_position, canvas, origin):
    """Prints a red line between the last position and the new position of the scara machine"""
    canvas.create_line(old_position[0]+origin[0], old_position[1]+origin[1], 
                       new_position[0]+origin[0], new_position[1]+origin[1], 
                       fill="red")

def print_arms(armA, armB, B_position, head_position, canvas, origin):
    """Updates the arms on the canvas"""
    canvas.coords(armA, origin[0], origin[1], B_position[0]+origin[0], B_position[1]+origin[0])
    canvas.coords(armB, B_position[0]+origin[0], B_position[1]+origin[1], 
                       head_position[0]+origin[0], head_position[1]+origin[1])
# main program entry point
if __name__ == "__main__":
    main()
