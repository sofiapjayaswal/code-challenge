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
cleanup_time = 35
setup_time = 1

# determining today's opening and closing times
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]
if day in weekdays:
    today_open = weekday_open
    today_close = weekday_close
else:
    today_open = weekend_open
    today_close = weekend_close

print(today_open)
print(today_close)

# build movie array based on file passed
movie_array = build_movie_array(filename)

for movie in movie_array:
    runtime = movie.get_runtime()
    showtime = get_showtime(runtime, today_open, today_close, cleanup_time, setup_time)
    print(showtime)




