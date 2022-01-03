# Scara GCode simulator

A simple scara simulator that reads GCode generated from [sandify](https://sandify.org/).

## How to use it

Parameters:

| Parameter | Type   | Description                                                        | Default value | Required |
|-----------|--------|--------------------------------------------------------------------|---------------|----------|
| -f        | String | Path to the gcode file                                             | -             | Yes      |
| -s        | Number | Simulation speed (must be in [1, 10])                              | 10            | No       |
| -w        | Number | The canvas width in px (must be >= 100)                            | 300           | No       |
| -H        | Number | The canvas height in px (must be >= 100)                           | 300           | No       |
| -ms       | Number | Number of microsteps per step (must be 1, 8, 16, 32, 64, 128, 256) | 16            | No       |

Example:

```
python .\main.py -w 1000 -H 1000 -ms 128 -s 10 -f "sample/sandify.gcode" 
```