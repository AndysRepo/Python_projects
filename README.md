# Python_projects

This folder contains a certain number of python codes that I wrote.
Usually the codes will address somewhow maths-related questions, going from solving some physics problem to performing a certain statistical analysis on a set of data. Some other times the codes will regard other things, like simple games. Most of the codes have been written just for fun, without any other aim.
Most of the codes are heavily commented, however in some cases comments will be in italian. 


1. Folder "**moto_pianeti**" : a simple implementation of the velocity-verlet algorithm to solve ordinary differential equations (https://en.wikipedia.org/wiki/Verlet_integration). Specifically we apply velocity-verlet integration to the equation governing the motion of planets (without considering general relativity effects). We generate a set of orbits featuring a different value of their eccentricity and se verify Kepler's second law (https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion) for the elliptical orbit.

2. Folder "**linear_fit**": a simple code taking a data file and performing a numerical linear regression (https://en.wikipedia.org/wiki/Linear_regression) on the dataset contained in the file. The script will make use of the scipy.optimize library (https://docs.scipy.org/doc/scipy/reference/optimize.html) to perform the calculation.

3. File "**snake_game.py**": a very simple version of the snake game, composed of just two different levels for now. The code requests to have python 3 installed and the "numpy", "graphics" and "secrets" library available.

4. File "**bmp_reader.py**": a (working) attempt to implement an algorithm reading the bmp file format. The code will recostruct, pixel by pixel, a bmp picture and allow the user to visualize it. It makes only use of the "graphics" library.
