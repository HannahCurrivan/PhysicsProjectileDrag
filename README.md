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

Now you need to name and direct your window to your layout above.

```
window = sg.Window('Projectile Drag', tab1_layout)
```

## Add action to both the "Calculate" & "Exit" buttons by including the needed calculations for a projectile with drag.

**1. Equations to calculate projectile with drag:**

   **1.1** The equation for Drag:

    ![alt text](https://github.com/HannahCurrivan/PhysicsProjectileDrag/blob/main/drag.JPG)

    K = Drag Coefficient.

    V = Internal Velocity in m/s

   **1.2 The initial velocity of the projectile includes the "Internal Velocity in m/s" which is one of the user's inputs by the angle.**

   First, convert the angle into θ (radians):
    
      ![alt text](https://github.com/HannahCurrivan/PhysicsProjectileDrag/blob/main/degree_radians.JPG)

    The degree is given by the user's input.

    Apply to both "Internal Velocity in m/s" and "θ (radians)" to the initial velocity equation:
   
      ![alt text](https://github.com/HannahCurrivan/PhysicsProjectileDrag/blob/main/Initial_V.JPG)

   **1.3 Calculate the initial acceleration of both X and Y:**
   
    ![alt text](https://github.com/HannahCurrivan/PhysicsProjectileDrag/blob/main/Initial_A.JPG)

### The Python code to add the action to the button:

```
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Calculate':
```

Outline the variables including the inputs from the GUI user.

```
            M = int(values['-mass-']) #mass in kg
            g = 9.8 #gravity (m/s^2)
            V = int(values['-IV-']) # Internal Velocity in m/s
            ang = int(values['-degree-']) #Angle to X-axis in degree
            K = 0.05 #Drag Coefficient 

```

Calculate the initial velocity of X and Y:

```
            Vx = [V*np.cos(ang/180 * np.pi)]
            Vy = [V*np.sin(ang/180 * np.pi)]

```
   
Calculate the Drag Force:

```
  F = K*V**2 
```

Calculate the initial acceleration of X and Y:

```
ax = [-(F*np.cos(ang/180 * np.pi))/M]
ay = [-g-(F*np.cos(ang/180 * np.pi))/M]
```

## Calculate the time value of an object.

Append time (t), and the initial velocity of both X (vx) and Y (vy). Two new lists have been made named "x" and "y" which will append the data from both Vx and Vy over a period of time. In addition, this while loop includes the calculation of the magnitude of the new velocity, which is then appended to a list called ax and ay. 

```
t = [0]
counter = 0
dt = 0.2
x = [0]
y = [0]
while (counter < 10):
    t.append(t[counter] + dt)
    Vx.append(Vx[counter] + dt * ax[counter])
    Vy.append(Vy[counter] + dt * ay[counter])
                
    x.append(x[counter] + dt * Vx[counter])
    y.append(y[counter] + dt * Vy[counter])
                
    # Calculate the Magnitude of the new velocity
    Vel = np.sqrt(Vx[counter + 1] **2 + Vy[counter + 1] **2)
    F = K * Vel**2
    ax.append(-(F*np.cos(ang/180 * np.pi))/M)
    ay.append(-g-(F*np.cos(ang/180 * np.pi))/M)
    counter = counter + 1
```

## Plot the outcome:

The final step is to display your data using "matplotlib.pyplot".

```
plt.figure()    
plt.plot(t, Vx) #plot velocity-X against t
plt.title("The change in velocity over a period of time")
plt.ylabel("Velocity (X)")
plt.xlabel("time")
plt.show()
            
plt.figure()
plt.plot(x, y, "go") 
plt.title("Distance the projective has travelled")
plt.ylabel("y (m)")
plt.xlabel("x (m)")
plt.show()
```
