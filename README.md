# PhysicsProjectileDrag
This python script is a projectile with drag including a GU Interface to give users an easy option to input variables.
![alt text](https://th.bing.com/th/id/OIP.uXaOyjOJQfmEgc6iCrMifQHaDS?pid=ImgDet&rs=1)

This graph can be found here: https://pediaa.com/how-to-solve-projectile-motion-problems/

To start you need to make sure you have the following Python packages downloaded:
```
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
```
## First lets make the layout of the GUI:

First, we select the colour of the GUI, in this case, it is ```sg.theme('DarkBlue14')```.
Then followed by the layout if the GUI, in this case, we are using both text and input text. 

```
tab1_layout = [
    [sg.Text('Mass in Kg', size =(45, 1)), sg.Text('Internal Velocity (m/s)', size =(20, 1))],
    [sg.InputText(key = '-mass-'), sg.InputText(key=('-IV-'))],
    [sg.Text('Angle to x-axis in degree', size =(32, 1))],
    [sg.InputText(key=('-degree-'))],
    [sg.Text('Calculated Outcome and Graph', size =(26, 1))],
    [sg.Button('Calculate'), sg.Button('Exit')]] 

```
