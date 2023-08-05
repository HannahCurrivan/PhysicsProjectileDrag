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
## First let's make the layout of the GUI:

First, we select the colour of the GUI, in this case, it is ```sg.theme('DarkBlue14')```.

Then followed by the layout of the GUI, in this case, we are using both text and input text. 

```
tab1_layout = [
    [sg.Text('Mass in Kg', size =(45, 1)), sg.Text('Internal Velocity (m/s)', size =(20, 1))],
    [sg.InputText(key = '-mass-'), sg.InputText(key=('-IV-'))],
    [sg.Text('Angle to x-axis in degree', size =(32, 1))],
    [sg.InputText(key=('-degree-'))],
    [sg.Text('Calculated Outcome and Graph', size =(26, 1))],
    [sg.Button('Calculate'), sg.Button('Exit')]] 

```

The options given to the user using this GUI are the input of "Mass in kg", "Internal Velocity", and "Angle to the x-axis in degrees". Each of these variables is needed for the projectile with drag equation. 

Now you need to name your window and direct it back to your layout above.

```
window = sg.Window('Projectile Drag', tab1_layout)
```

## Add action to both the "Calculate" & "Exit" buttons by including the needed calculations for a projectile with drag.

1. Equations to calculate projectile with drag:

   1.1 The equation for Drag:

    

   1.2 The initial velocity of the projectile includes the "Internal Velocity in m/s" which is one of the user's inputs by the angle.

   First, convert the angel into \Theta (radians):
    
      $ \Theta (radians) = degrees / 180 * \pi $
    
   Apply to both "Internal Velocity in m/s" and "\Theta (radians)" to the initial velocity equation:
   
      $ vx = v*x*cos\Theta $

   










