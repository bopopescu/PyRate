#   This Python module is part of the PyRate software package.
#
#   Copyright 2020 Geoscience Australia
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import os
from collections import namedtuple

import numpy as np

__version__ = "0.4.0"
CLI_DESCRIPTION = """
PyRate workflow: 

    Step 1: conv2tif
    Step 2: prepifg
    Step 3: process
    Step 4: merge 

Refer to https://geoscienceaustralia.github.io/PyRate/usage.html for 
more details.
"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
NO_OF_PARALLEL_PROCESSES = comm.Get_size()

CONV2TIF = "conv2tif"
PREPIFG = "prepifg"
PROCESS = "process"
MERGE = "merge"

REF_COLOR_MAP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "utils", "colormap.txt")
# distance division factor of 1000 converts to km and is needed to match legacy output
DISTFACT = 1000
# mappings for metadata in header for interferogram
GAMMA_DATE = "date"
GAMMA_TIME = "center_time"
GAMMA_WIDTH = "width"
GAMMA_NROWS = "nlines"
GAMMA_CORNER_LAT = "corner_lat"
GAMMA_CORNER_LONG = "corner_lon"
GAMMA_Y_STEP = "post_lat"
GAMMA_X_STEP = "post_lon"
GAMMA_DATUM = "ellipsoid_name"
GAMMA_FREQUENCY = "radar_frequency"
GAMMA_INCIDENCE = "incidence_angle"
# RADIANS = 'RADIANS'
# GAMMA = 'GAMMA'
# value assigned to no-data-value
LOW_FLOAT32 = np.finfo(np.float32).min * 1e-10

# lookup keys for the metadata fields in PyRate GeoTIFF files
PYRATE_NCOLS = "NCOLS"
PYRATE_NROWS = "NROWS"
PYRATE_X_STEP = "X_STEP"
PYRATE_Y_STEP = "Y_STEP"
PYRATE_LAT = "LAT"
PYRATE_LONG = "LONG"
MASTER_DATE = "MASTER_DATE"
MASTER_TIME = "MASTER_TIME"
SLAVE_DATE = "SLAVE_DATE"
SLAVE_TIME = "SLAVE_TIME"
EPOCH_DATE = "EPOCH_DATE"
PYRATE_DATUM = "DATUM"
PYRATE_TIME_SPAN = "TIME_SPAN_YEAR"
PYRATE_WAVELENGTH_METRES = "WAVELENGTH_METRES"
PYRATE_INCIDENCE_DEGREES = "INCIDENCE_DEGREES"
PYRATE_INSAR_PROCESSOR = "INSAR_PROCESSOR"
PYRATE_WEATHER_ERROR = "WEATHER_ERROR"
PYRATE_APS_ERROR = "APS_ERROR"
PYRATE_MAXVAR = "CVD_MAXVAR"
PYRATE_ALPHA = "CVD_ALPHA"
COHERENCE = "COHERENCE_MASKED_MULTILOOKED_IFG"
MULTILOOKED = "MULTILOOKED_IFG"
ORIG = "ORIGINAL_IFG"
DEM = "ORIGINAL_DEM"
MLOOKED_DEM = "MULTILOOKED_DEM"
INCIDENCE = "INCIDENCE_ANGLE_MAP"
MLOOKED_INC = "MULTILOOKED_INCIDENCE_ANGLE_MAP"
INCR = "INCREMENTAL_TIME_SLICE"
CUML = "CUMULATIVE_TIME_SLICE"
STACKRATE = "STACKED_RATE_MAP"
STACKERROR = "STACKED_RATE_ERROR"
STACKSAMP = "STACKED_RATE_SAMPLES"
PYRATE_ORBITAL_ERROR = "ORBITAL_ERROR"
ORB_REMOVED = "REMOVED"
APS_REMOVED = "REMOVED"
PYRATE_REF_PHASE = "REFERENCE_PHASE"
REF_PHASE_REMOVED = "REMOVED"
NAN_STATUS = "NAN_STATUS"
NAN_CONVERTED = "CONVERTED"
DATA_TYPE = "DATA_TYPE"
DATA_UNITS = "DATA_UNITS"

DAYS_PER_YEAR = 365.25  # span of year, not a calendar year
YEARS_PER_DAY = 1 / DAYS_PER_YEAR
SPEED_OF_LIGHT_METRES_PER_SECOND = 3e8
MM_PER_METRE = 1000

# prepifg helpers
CustomExts = namedtuple("CustExtents", ["xfirst", "yfirst", "xlast", "ylast"])
MINIMUM_CROP = 1
MAXIMUM_CROP = 2
CUSTOM_CROP = 3
ALREADY_SAME_SIZE = 4
CROP_OPTIONS = [MINIMUM_CROP, MAXIMUM_CROP, CUSTOM_CROP, ALREADY_SAME_SIZE]
GRID_TOL = 1e-6

# GDAL projection list
GDAL_X_CELLSIZE = 1
GDAL_Y_CELLSIZE = 5
GDAL_X_FIRST = 0
GDAL_Y_FIRST = 3

MINIMUM_CROP = 1
MAXIMUM_CROP = 2
CUSTOM_CROP = 3
ALREADY_SAME_SIZE = 4

# mpi process identification
MASTER_PROCESS = 0

# ROIPAC RSC header file constants
WIDTH = "WIDTH"
FILE_LENGTH = "FILE_LENGTH"
XMIN = "XMIN"
XMAX = "XMAX"
YMIN = "YMIN"
YMAX = "YMAX"
X_FIRST = "X_FIRST"
X_STEP = "X_STEP"
X_UNIT = "X_UNIT"
Y_FIRST = "Y_FIRST"
Y_STEP = "Y_STEP"
Y_UNIT = "Y_UNIT"
TIME_SPAN_YEAR = "TIME_SPAN_YEAR"

# Old ROIPAC headers (may not be needed)
ORBIT_NUMBER = "ORBIT_NUMBER"
VELOCITY = "VELOCITY"
HEIGHT = "HEIGHT"
EARTH_RADIUS = "EARTH_RADIUS"
WAVELENGTH = "WAVELENGTH"
DATE = "DATE"
DATE12 = "DATE12"
HEADING_DEG = "HEADING_DEG"

# DEM specific
Z_OFFSET = "Z_OFFSET"
Z_SCALE = "Z_SCALE"
PROJECTION = "PROJECTION"
DATUM = "DATUM"

# custom header aliases
MASTER = "MASTER"
SLAVE = "SLAVE"
X_LAST = "X_LAST"
Y_LAST = "Y_LAST"
# RADIANS = "RADIANS"
# ROIPAC = "ROIPAC"

# store type for each of the header items
INT_HEADERS = [WIDTH, FILE_LENGTH, XMIN, XMAX, YMIN, YMAX, Z_OFFSET, Z_SCALE]
STR_HEADERS = [X_UNIT, Y_UNIT, ORBIT_NUMBER, DATUM, PROJECTION]
FLOAT_HEADERS = [X_FIRST, X_STEP, Y_FIRST, Y_STEP, TIME_SPAN_YEAR, VELOCITY, HEIGHT, EARTH_RADIUS, WAVELENGTH, HEADING_DEG]
DATE_HEADERS = [DATE, DATE12]

ROIPAC_HEADER_LEFT_JUSTIFY = 18
ROI_PAC_HEADER_FILE_EXT = "rsc"

# Constants
PHASE_BAND = 1
RADIANS = "RADIANS"
MILLIMETRES = "MILLIMETRES"
GAMMA = "GAMMA"
ROIPAC = "ROIPAC"

# GDAL projection list
GDAL_X_CELLSIZE = 1
GDAL_Y_CELLSIZE = 5
GDAL_X_FIRST = 0
GDAL_Y_FIRST = 3


# required by conversation module
NO_DATA_VALUE = 0.0
DATA_BANDS = 1
SPEED_OF_LIGHT_METRES_PER_SECOND = 3e8
DAYS_PER_YEAR = 365.25  # span of year, not a calendar year
GDAL_CACHE_MAX = 2 ** 15
GDAL_WARP_MEMORY_LIMIT = 2 ** 10


# Constants
MINIMUM_CROP = 1
MAXIMUM_CROP = 2
CUSTOM_CROP = 3
ALREADY_SAME_SIZE = 4
CROP_OPTIONS = [MINIMUM_CROP, MAXIMUM_CROP, CUSTOM_CROP, ALREADY_SAME_SIZE]
