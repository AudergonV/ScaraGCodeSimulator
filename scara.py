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
Contains the Scara class, representing a scara machine.
"""

__author__ = "Vincent Audergon"
__date__ = "2022.01.04"
__version__ = "1.0"
__email__ = "vincent.audergon@bluewin.ch"
__userid__ = "vincent.audergon"

import math

class Scara:
    """This class simulates a scara machine"""

    def __init__(self, length, microsteps):
        self.units_per_rad = math.pi/3
        self.steps_per_rotation = 200*microsteps
        self.steps_per_unit = 200/6*microsteps
        self.position_motor_A = 0.0
        self.position_motor_B = 100*microsteps
        self.length = length

    def rotate_A(self, units):
        """Rotates the motor A by x units"""
        self.position_motor_A = units*self.steps_per_unit

    def rotate_B(self, units):
        """Rotates the motor B by x units"""
        self.position_motor_B = units*self.steps_per_unit

    def get_B_position(self):
        """Returns the x,y position of the motor B"""
        alpha = self.get_alpha_rad()
        return  [math.cos(alpha)*self.length, 
                 math.sin(alpha)*self.length]

    def get_head_position(self):
        """Returns the position of the head"""
        alpha = self.get_alpha_rad()
        beta = self.get_beta_rad()
        return [(math.cos(alpha) + math.cos(beta))*self.length, 
                (math.sin(alpha)+ math.sin(beta))*self.length]

    def get_alpha_rad(self):
        """Returns the angle alpha (motor A) in radians [0, 2*PI]"""
        return (self.position_motor_A%self.steps_per_rotation)/self.steps_per_rotation*math.pi*2

    def get_beta_rad(self):
        """Returns the angle beta (motor B) in radians [0, 2*PI]"""
        return (self.position_motor_B%self.steps_per_rotation)/self.steps_per_rotation*math.pi*2

