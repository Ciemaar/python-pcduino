cimport arduino.carduino

# Import some functionality from Python and the C stdlib
from cpython.pycapsule cimport *


def pinMode(unsigned short int  pin, unsigned short int  mode):
    carduino.pinMode(pin, mode)
