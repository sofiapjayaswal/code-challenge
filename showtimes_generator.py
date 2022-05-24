# Author: Sofia Jayaswal
# Date: 05/23/2022
# Purpose: generate show times for movies in a theatre based on a given file of movies showing

import sys
from datetime import *
from showtimes_funcs import *

# check if number of arguments passed is correct, if not exit
if len(sys.argv) > 2:
    print("Error: Too many arguments passed. Usage: showtimes_generator.py filename")
    quit()

# set variable equal to argument passed
filename = sys.argv[1]
# get today's date
today = date.today()
date = today.strftime("%A %m/%d/%Y")
print(date)


# initializing other variables
weekday_open = "8:00"
weekday_close = "11:00"
weekend_open = "10:30"
weekend_close = "11:30"

# build movie array based on file passed
movie_array = build_movie_array(filename)

for movie in movie_array:




