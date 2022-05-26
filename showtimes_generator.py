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
day = today.strftime("%A")  # have to get day individually to get hours for the day

# initializing opening and closing variables (subject to change)
weekday_open = "8:00"
weekday_close = "23:00"
weekend_open = "10:30"
weekend_close = "23:30"

# initialize variables for minutes taken to set up theatre in morning and clean up in between each movie
setup_time = 60
cleanup_time = 35

# determining today's opening and closing times based on the day
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday"]
if day in weekdays:
    today_open = weekday_open
    today_close = weekday_close
else:  # weekend
    today_open = weekend_open
    today_close = weekend_close

# build an array of Movie objects based on file passed
movie_array = build_movie_array(filename)

# getting showtimes for each movie
for movie in movie_array:
    # get_showtimes function returns an array of arrays (inner arrays represent individual showtimes with end and start)
    showtimes = get_showtimes(movie.get_runtime(), today_open, today_close, cleanup_time, setup_time)
    movie.set_showtimes(showtimes)  # setting instance variable equal to returned array

# print schedule in correct format
print_schedule(sys.argv, date, movie_array)




