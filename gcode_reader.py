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
Reads a gcode file and returns the instructions
"""

__author__ = "Vincent Audergon"
__date__ = "2022.01.04"
__version__ = "1.0"
__email__ = "vincent.audergon@bluewin.ch"
__userid__ = "vincent.audergon"



class GCodeReader:

    def __init__(self):
        """"""
    
    def OpenGCode(self, filename):
        """Opens a GCode file and reads its content"""
        try:
            self.gcode = open(filename, 'r')
        except FileNotFoundError:
            print(filename + " not found. Please verify the path to the gcode file.")
            exit(1)
        self.lines = self.gcode.readlines()
        self.gcode.close()
        
    def GetNextInstruction(self):
        """Returns the next gcode instruction, avoid the comments"""
        if self.HasMoreLines():
            line = self.lines[0]
            self.lines.pop(0)
            if line.startswith(';'):
                return [];
            return line.split(' ')

    def HasMoreLines(self):
        """Indicates if there is more lines in the gcode file"""
        return len(self.lines) > 0