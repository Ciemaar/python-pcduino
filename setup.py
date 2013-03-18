from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    name='pcDuino',
    version='',
    packages=['python-pcduino.Samples.blink_led.gpio', 'python-pcduino.arduino'],
    url='',
    license='',
    author='andriod',
    author_email='',
    description='',
    cmdclass = {'build_ext': build_ext},
    ext_modules=[Extension(
        'arduino',
        ["arduino/arduino.pyx"],
        libraries=['Arduino'],
        ## Not clear when this is used, seem to be specified on the command line only
        # library_dirs=["../arduino/hardware/arduino/cores/arduino",
        #               "../python-pcduino/arduino"]
    )])