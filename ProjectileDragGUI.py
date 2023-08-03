# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 15:59:28 2023

@author: Hannah Currivan
"""
 
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt

#GUI information      
sg.theme('DarkBlue14')

#Entering the data
tab1_layout = [
    [sg.Text('Mass in Kg', size =(45, 1)), sg.Text('Internal Velocity (m/s)', size =(20, 1))],
    [sg.InputText(key = '-mass-'), sg.InputText(key=('-IV-'))],
    [sg.Text('Angle to x-axis in degree', size =(32, 1))],
    [sg.InputText(key=('-degree-'))],
    [sg.Text('Calculated Outcome and Graph', size =(26, 1))],
    [sg.Button('Calculate'), sg.Button('Exit')]] 
 
window = sg.Window('Projectile Drag', tab1_layout)
event, values = window.read()   

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Calculate':
            # Variables
            M = int(values['-mass-']) #mass in kg
            g = 9.8 #gravity (m/s^2)
            V = int(values['-IV-']) # Internal Velocity in m/s
            ang = int(values['-degree-']) #Angle to X-axis in degree
            K = 0.05 #Drag Coefficient 
            
            # calculate velocities in the X and Y  axis
            Vx = [V*np.cos(ang/180 * np.pi)]
            Vy = [V*np.sin(ang/180 * np.pi)]
            
            #Drag Force
            F = K*V**2 
            
            # calculate initial acceleration of X and Y
            ax = [-(F*np.cos(ang/180 * np.pi))/M]
            ay = [-g-(F*np.cos(ang/180 * np.pi))/M]
            
            # Calculate the time value on an object
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
                
                # Calculate Magnitude of new velocity
                Vel = np.sqrt(Vx[counter + 1] **2 + Vy[counter + 1] **2)
                F = K * Vel**2
                ax.append(-(F*np.cos(ang/180 * np.pi))/M)
                ay.append(-g-(F*np.cos(ang/180 * np.pi))/M)
                counter = counter + 1
             
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

window.close()
