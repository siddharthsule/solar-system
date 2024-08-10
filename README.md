# A Simple Solar System Simulation

This code simulates the sun and the planets revolving around it in two Dimensions. For now, a simple Euler's Method is incorporated with Object-Oriented Programming for Planets and Stars.

## Usage

The Simulation can be run using Python but can be accelerated using PyPy:

```bash
# Python Users
py main.py --years YEARS --dt DT # Defaults Exist, so not required

# PyPy Users
pypy main.py --years YEARS --dt DT
```

The data can be plotted into a GIF using the `animate.py` script:

```bash
py animate.py
```

Alternatively, the script `runcode.sh` can be used to automate this process.

***

Siddharth Sule, August 2024
