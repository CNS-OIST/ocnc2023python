import numpy as np
import matplotlib.pyplot as plt

def plot_mandelbrot_set(x1, x2, y1, y2, dpi=500, steps=20, threshold=2):
    """Plot the Mandelbrot set."""
    # Compute the width and height of the image
    width = int(dpi * (x2 - x1))
    height = int(dpi * (y2 - y1))
    
    # Create the array of complex constants
    real, imag = np.meshgrid(
        np.linspace(x1, x2, width),
        np.linspace(y1, y2, height)
    )
    constants = real + 1j * imag

    # Create a complex array (dtype=complex) with the same shape as constants for the Mandelbrot set
    mandelbrot = np.zeros((height, width), dtype=complex)
    msk = np.ones(constants.shape) > 0
    result = np.zeros(constants.shape)
    # For each step, each value z in the mandelbrot array is updated according to:
    #   z = z ** 2 + c 
    #       with c the complex constant corresponding to z (in the same position in the array)
    #   If the absolute value of z is higher than threshold, we cap it at threshold.
    for i in range(steps):
        mandelbrot = mandelbrot ** 2 + constants
        passed = np.abs(mandelbrot) > threshold
        mandelbrot[passed] = threshold

        # Keep track at which step did we get above threshold
        result[msk & passed] = i
        msk &= ~passed

    plt.figure(figsize=(12, 10))
    plt.imshow(np.abs(result))

# Test the function
plot_mandelbrot_set(-1.7, 0.7, -1, 1)
