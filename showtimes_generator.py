# Author: Sofia Jayaswal
# Date: 05/23/2022
# Purpose: generate show times for movies in a theatre based on a given file of movies showing

import sys
from showtimes_funcs import *

# check if number of arguments passed is correct, if not exit
if len(sys.argv) > 4:
    print("Error: Too many arguments passed. Usage: showtimes_generator.py filename Day date(MM/DD/YYYY)")
    quit()

# set variables equal to arguments passed
filename = sys.argv[1]
day = sys.argv[2]
date = sys.argv[3]

# validating day passed
if day == ("Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday" or "Saturday" or "Sunday"):
    print(day + " is not a valid day in the week")
    quit()

# initializing other variables
weekday_open = "8:00"
weekday_close = "11:00"
weekend_open = "10:30"
weekend_close = "11:30"

# build movie array based on file passed
movie_array = build_movie_array(filename)

for movie in movie_array:



