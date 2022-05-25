# Author: Sofia Jayaswal
# Date: 05/23/2022
# Purpose: helper functions for generating showtimes

from movie import Movie


def build_movie_array(filename):
    movie_array = []
    lines_in_file = []
    movie_file = open(filename)
    lines_in_file = movie_file.readlines()
    movie_file.close()
    # deleting first line with headers
    del lines_in_file[0]

    # creating movie objects for each line and adding to array
    for line in lines_in_file:
        # get list split up by commas, separating info of movie
        stripped_line = line.strip()
        movie_info = stripped_line.split(", ")
        movie_name = movie_info[0]
        movie_release_year = movie_info[1]
        movie_rating = movie_info[2]
        movie_runtime = movie_info[3]
        movie = Movie(movie_name, movie_release_year, movie_rating, movie_runtime)
        # add to array
        movie_array.append(movie)

    return movie_array

def get_showtime(movie_runtime, opening_time, closing_time, cleanup_time, setup_time):
    # initialize array of showtimes (will be an array of arrays -> inner array being start and end time of movies)
    show_times = []
    # converting all times to total number of minutes to make math simpler
    runtime_in_minutes = convert_to_minutes(movie_runtime)
    open_in_minutes = convert_to_minutes(opening_time)
    close_in_minutes = convert_to_minutes(closing_time)
    # accounting for cleanup and setup time (limits in when the movies can start/end)
    upper_bound = close_in_minutes - cleanup_time
    lower_bound = open_in_minutes + setup_time

    # initialize start and end times
    end_time = close_in_minutes  # will account for clean up time in the while loop
    start_time = close_in_minutes  # need this to be equal to close time initially so you can calculate correct end time
    # looping from closing to opening to find last shows first and first shows last
    while lower_bound <= (end_time - cleanup_time - runtime_in_minutes) <= upper_bound:
        # thing to think about: what about the last go do I want to subtract 35 minutes still?
        show_time = []
        temp = end_time
        # end_time is equal to the start time coming after this showing minus cleanup_time
        end_time = start_time - cleanup_time
        start_time = temp - cleanup_time - runtime_in_minutes
        # checking if time is clean (ending in 0 or 5)
        remainder = start_time % 10 # gives us last digit of start_time
        if remainder != 0 or remainder != 5:
            # checking whether to subtract down so last digit is 0 or 5
            if remainder > 5:
                start_time = start_time - (remainder - 5)
            else:
                start_time = start_time - remainder
        # converting start and end times back to strings (displaying hours and minutes) so readable for the schedule
        string_start_time = convert_to_hours_minutes(start_time)
        string_end_time = convert_to_hours_minutes(end_time)
    return show_times


def convert_to_minutes(time):
    # splitting up hours and minutes
    hours_minutes = time.split(":")
    # checking if time has hours and minutes or just minutes (more important for runtime)
    if len(hours_minutes) == 1:
        return int(hours_minutes[0])
    # calculating total minutes through multiplying hours by 60 and adding minutes
    total_minutes = int(hours_minutes[0])*60 + int(hours_minutes[1])
    return total_minutes


def convert_to_hours_minutes(time):
    # dividing time by 60 to get hours
    hours = time // 60
    # get remainder indicating minutes
    minutes = time % 60
    # convert to string and add colon in between hours and minutes
    string_time = str(hours) + ":" + str(minutes)
    return string_time

# def subtract_times(time1, time2):
#
# def compare_times(time1, time2):

