#!/usr/bin/env python3

# MIT License
# 
# Copyright (c) 2020 burturt
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

config_lines = []

# Set start values here
ticks = 0
ticks_exp = 1
size = 0
health = 20.0
speed = 0.7
follow_distance = 16.0
attack_damage = 6.0

while size <= 64:

    config_lines.append("'" + str(round(ticks)) + "':\n")
    config_lines.append("  size: " + str(round(size)) + "\n")
    config_lines.append("  health: " + str(round(health,1)) + "\n")
    config_lines.append("  speed: " + str(round(speed,1)) + "\n")
    config_lines.append("  follow_distance: " + str(round(follow_distance,1)) + "\n")
    config_lines.append("  attack_damage: " + str(round(attack_damage,1)) + "\n")

    # Set increase between each size here
    size += 1
    ticks = round(ticks * 1.02) + 24000
    health += 4.0
    speed += 0.3
    follow_distance += 4.0
    attack_damage += 0.0


f = open("output.txt","w")
f.writelines(config_lines)
f.close()