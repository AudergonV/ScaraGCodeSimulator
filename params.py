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
Contains the Params class, reads and checks the parameters
"""

__author__ = "Vincent Audergon"
__date__ = "2022.01.04"
__version__ = "1.0"
__email__ = "vincent.audergon@bluewin.ch"
__userid__ = "vincent.audergon"

import argparse

# Constants
SPEED_DEFAULT = 10
CANVAS_HEIGHT_DEFAULT = 300  
CANVAS_WIDTH_DEFAULT = 300 
MICROSTEPS_DEFAULT = 16

class Params:
    """This class reads, checks and stores the invoking parameters"""

    def __init__(self):
        """ Constructor
        
        Args:
            None
        """
        args = self.get_args()
        self.speed = self.get_speed(args)
        self.width = self.get_canvas_width(args)
        self.height = self.get_canvas_height(args)
        self.microsteps = self.get_microsteps(args)
        self.filename = args.f


    def get_speed(self, args):
        """Get the speed or the default value"""
        speed = args.s;
        if (speed < 1 or speed > 10): 
            print("Warning: " + str(speed) + " is not a valid value for the -s parameter. It must be >= 1 and <= 10. "
                    +"Using the default value (" + str(SPEED_DEFAULT) + ").")
            return SPEED_DEFAULT
        return speed

    def get_canvas_width(self, args):
        """Get the width or the default value"""
        width = args.w;
        if (width < 100): 
            print("Warning: " + str(width) + " is not a valid value for the -w parameter. It must be >= 100. "
                    +"Using the default value (" + str(CANVAS_WIDTH_DEFAULT) + ").")
            return CANVAS_WIDTH_DEFAULT
        return width

    def get_canvas_height(self, args):
        """Get the height or the default value"""
        height = args.H;
        if (height < 100): 
            print("Warning: " + str(height) + " is not a valid value for the -H parameter. It must be >= 100. "
                    +"Using the default value (" + str(CANVAS_HEIGHT_DEFAULT) + ").")
            return CANVAS_HEIGHT_DEFAULT
        return height

    def get_microsteps(self, args):
        """Get the microsteps or the default value"""
        microsteps = args.ms;
        if (not microsteps in [1,8,16,32,64,128,256]): 
            print("Warning: " + str(microsteps) + " is not a valid value for the -ms parameter. It must be 1, 8, 16, 32, 64, 128 or 256. "
                    +"Using the default value (" + str(MICROSTEPS_DEFAULT) + ").")
            return CANVAS_HEIGHT_DEFAULT
        return microsteps

    def get_args(self):
        """Gets the arguments from the command line
    
        Returns the arguments"""
        parser = argparse.ArgumentParser()
        parser.add_argument("-s", type=int, default=SPEED_DEFAULT,
                            help="The speed of the animation [1, 10]")
        parser.add_argument("-w", type=int, default=CANVAS_HEIGHT_DEFAULT,
                            help="The width of the canvas in px (must be >= 100)")
        parser.add_argument("-H", type=int, default=CANVAS_HEIGHT_DEFAULT,
                            help="The height of the canvas in px (must be >= 100)")
        parser.add_argument("-ms", type=int, default=MICROSTEPS_DEFAULT,
                            help="Number of microsteps per step (1, 8, 16, 32, 64, 128 or 256)")
        parser.add_argument("-f", type=str, help="Path to the gcode file", required=True)
        return parser.parse_args()
