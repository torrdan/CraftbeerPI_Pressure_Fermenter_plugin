# CraftbeerPI_costum_plugin
I have 4 unitanks, 600 L each in my brewery. 
I am currently controlling the temperature during fermentation with the software Craftbeerpi. Actors are solenoid valves controlling a water-glycol cooling jacket. 

I would like to upgrade the system with the possibility to monitor the pressure in the tank and adjust it with a solenoid valve. I usually ferment pressureless during primary and start recovering pressure before end of secondary. It would be awesome to have in Craftbeerpi a tab for the fermenter control where I can set temperature and pressure as variables to control and for each of them have a different actor (solenoid valve) and setpoint (e.g. 20 °C for temperature and 1 bar for pressure).

At moment I am trying first to read the values from the pressure sensor (8 Bar, output 0.5-4.5 V). I can do it with the python script Pressure_Sensor.py but the same command lines on the _init_py file for the Craftbeerpi plugin do not work. 
