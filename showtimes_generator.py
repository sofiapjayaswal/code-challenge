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

# initiating all variables
# set variable equal to argument passed
filename = sys.argv[1]
# get today's date
today = date.today()
date = today.strftime("%A %m/%d/%Y")
day = today.strftime("%A")

# initializing opening and closing variables and other important theatre variables (subject to change)
weekday_open = "8:00"
weekday_close = "23:00"
weekend_open = "10:30"
weekend_close = "23:30"

# initialize variables for minutes taken to set up theatre in morning and clean up in between each movie
setup_time = 60
cleanup_time = 35

# determining today's opening and closing times
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]
if day in weekdays:
    today_open = weekday_open
    today_close = weekday_close
else:
    today_open = weekend_open
    today_close = weekend_close

# print(today_open)
# print(today_close)

# build movie array based on file passed
movie_array = build_movie_array(filename)

# getting all showtimes for
for movie in movie_array:
    # converting all times to total number of minutes to make math simpler
    runtime_in_minutes = convert_to_minutes(movie.get_runtime())
    open_in_minutes = convert_to_minutes(today_open)
    close_in_minutes = convert_to_minutes(today_close)

    showtimes = get_showtimes(runtime_in_minutes, open_in_minutes, close_in_minutes, cleanup_time, setup_time)
    movie.showtimes = showtimes

print_schedule(sys.argv, date, movie_array)




