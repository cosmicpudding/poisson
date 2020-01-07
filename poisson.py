# Poisson chance coincidence calculator: estimates chance given radius and density of a survey
# Usage: >> python poisson.py -r radius -d density
# V.A. Moss (vmoss.astro@gmail.com)
__author__ = "V.A. Moss"
__date__ = "$22-oct-2018 22:00:00$"
__version__ = "0.2"

import os
import sys
from math import *
from numpy import *
from argparse import ArgumentParser, RawTextHelpFormatter

parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument('-r', '--radius',
		default=30,
		type=float,
		help='Specify radius in arcsec (default: %(default)s)')
parser.add_argument('-d', '--density',
		default=195,
		type=float,
		help='Specify density of sources in deg^-2 (default: %(default)s)')
parser.add_argument('-s', '--sources',
		default=4,
		type=int,
		help='Specify number of sources to calculate chance alignment (default: %(default)s)')

# Parse the arguments above
args = parser.parse_args()
radius = args.radius/3600.0 # convert to degrees
density = args.density 
area = pi * radius**2
rate = area * density
num = arange(args.sources + 1)

# # S82 VLA
# radius = 35/3600. # deg
# density = 195 # deg^-2
# area = pi * radius**2
# rate = area * density
# num = arange(5)

# # NVSS
# radius = 30/3600. # deg
# density = 0.02 # deg^-2
# area = pi * radius**2
# rate = area * density
# num = arange(2)

# # XMM
# radius = 30/3600. # deg
# density = 469 # deg^-2 # from catalogue
# #density = 14 # deg^-2 # > brightness of 1657
# area = pi * radius**2
# rate = area * density
# num = arange(2)

# Get distribution.
# Note: probability sums to 1.
total = 0
for x in num:
	prob = (rate**x * exp(-rate))/factorial(x)

	print ('Chance of %i sources: %.6f%%' % (x,prob*100))

	if x == 0 or x == 1:
		total +=prob

print ('\nChance of 2 or more sources: %.6f%%' % ((1-total)*100))

