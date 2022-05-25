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


def get_showtimes(movie_runtime, opening_time, closing_time, cleanup_time, setup_time):
    # initialize array of showtimes (will be an array of arrays -> inner array being start and end time of movies)
    show_times = []

    # accounting for cleanup and setup time (limits in when the movies can start/end)
    upper_bound = closing_time - cleanup_time
    lower_bound = opening_time + setup_time
    # start_time set to closing because we will loop backwards using the last start_time to find the next start_time
    start_time = closing_time
    # looping to find last shows first and first shows last as long as the next start_time is within bounds
    while lower_bound <= (start_time - cleanup_time - movie_runtime) <= upper_bound:
        show_time = []
        # end_time is equal to the start time coming after this showing minus cleanup_time
        end_time = start_time - cleanup_time
        start_time = end_time - movie_runtime
        # checking if time is clean (ending in 0 or 5)
        remainder = start_time % 10  # gives us last digit of start_time
        if remainder != 0 or remainder != 5:
            # checking whether to subtract down so last digit is 0 or 5
            if remainder > 5:
                start_time = start_time - (remainder - 5)
                end_time = end_time - (remainder-5)  # also have to account for change in end_time
            else:
                start_time = start_time - remainder
                end_time = end_time - remainder
        # converting start and end times back to strings (displaying hours and minutes) so readable for the schedule
        string_start_time = convert_to_hours_minutes(start_time)
        string_end_time = convert_to_hours_minutes(end_time)
        # add singular showtime to inner list and add inner list to bigger list of all showtimes for the movie
        show_time.append(string_start_time)
        show_time.append(string_end_time)
        # more efficient to append (will loop over list backwards when printing to print first show first)
        show_times.append(show_time)
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
    string_time = str(hours) + ":" + str(minutes).zfill(2)
    return string_time


def print_schedule(user_input, date, movies_array):
    print(user_input[0] + " " + user_input[1] + "\n")
    print(date + "\n")
    for movie in movies_array:
        print(movie)




