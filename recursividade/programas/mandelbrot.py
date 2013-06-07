#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
mandelbrot.py

 Simple program that calculates and displays the Mandelbrot set.
(c) Paulo Marques, pmarques@dei.uc.pt

June 2005
"""

import sys
import os





#############################################################################

def mandel(z0, MAX_ITER=100):
    """Calculates the number of iterations for point <z0> for the Mandelbrot
    set"""

    iter = 0
    z    = 0
    while (iter < MAX_ITER):
        z = z*z + z0
        iter = iter + 1
        if abs(z) > 2:
            break

    return iter

#############################################################################

def calc_mandel(width, height, zmin, zmax):
    """Calculates the mandelbrot set for a certain image size (width, height)
    over a certain complex box (zmin->zmax)"""

    # This function maps an (i,j) position of the screen to a complex number
    def real_pos(i, j):
        return zmin + j*(zmax-zmin).real/width + i*(zmax-zmin).imag/height*1j

    # Actually calculate the mandelbrot set for all points
    img = [[mandel(real_pos(i,j)) for j in range(width)] for i in range(height)]

    return img


##############################################################################

## This section is for testing purposes only

def simple_mandel():

    # Calculate mandelbrot
    mandel_img = calc_mandel(1020, 768, -2.2-1.5j, +1.2+1.5j)

    # Show image
    title('The Mandelbrot Set and the Corresponding Iteration Count', fontsize='16')
    axis('off')
    imshow(mandel_img)
    colorbar()
    show()

if __name__ == "__main__":
    from pylab import *
    simple_mandel()


