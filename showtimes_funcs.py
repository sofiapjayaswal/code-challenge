# Author: Sofia Jayaswal
# Date: 05/25/2022
# Purpose: helper functions for generating schedule

from movie import Movie

# Purpose: build an array of Movie objects based on the file passed
# Parameters: filename
# Return: array of Movie objects
def build_movie_array(filename):
    movie_array = []
    movie_file = open(filename)
    lines_in_file = movie_file.readlines()  # add each line to an array
    movie_file.close()
    # deleting first line with headers
    del lines_in_file[0]

    # creating movie objects for each line and adding to array
    for line in lines_in_file:
        stripped_line = line.strip()  # stripping white space
        movie_info = stripped_line.split(",")  # splitting by commas
        for component in movie_info:
            component.strip()  # stripping any spaces
        # setting variables to items in the array
        movie_name = movie_info[0]
        movie_release_year = movie_info[1]
        movie_rating = movie_info[2]
        movie_runtime = movie_info[3]
        # create Movie object
        movie = Movie(movie_name, movie_release_year, movie_rating, movie_runtime)
        # add to array
        movie_array.append(movie)

    return movie_array


# Purpose: get show times for a movie
# Parameters: movie_runtime, opening_time, closing_time, cleanup_time, setup_time
# Return: array of arrays (inner array: individual show time with start and end time)
def get_showtimes(movie_runtime, opening_time, closing_time, cleanup_time, setup_time):
    # initialize array of all show times
    show_times = []

    # converting all times to total number of minutes to make math simpler
    movie_runtime = convert_to_minutes(movie_runtime)
    opening_time = convert_to_minutes(opening_time)
    closing_time = convert_to_minutes(closing_time)

    # accounting for cleanup and setup time (limits in when the movies can start/end)
    upper_bound = closing_time - cleanup_time
    lower_bound = opening_time + setup_time

    # start_time set to closing because we will loop backwards using the last start_time to find the next start_time
    start_time = closing_time
    # looping to find last shows first and first shows last as long as the next start_time is within bounds
    while lower_bound <= (start_time - cleanup_time - movie_runtime) <= upper_bound:
        show_time = []  # initializing array for the individual show time
        # end_time is equal to the start time coming after this showing minus cleanup_time
        end_time = start_time - cleanup_time
        start_time = end_time - movie_runtime
        # checking if time is clean (ending in 0 or 5)
        remainder = start_time % 10  # gives us last digit of start_time
        if remainder != 0 or remainder != 5:
            start_time = get_clean_time(remainder, start_time)
            end_time = get_clean_time(remainder, end_time)
        # converting start and end times back to strings (displaying hours and minutes) so readable for the schedule
        string_start_time = convert_to_hours_minutes(start_time)
        string_end_time = convert_to_hours_minutes(end_time)
        # add singular showtime to inner list and add inner list to bigger list of all show times for the movie
        show_time.append(string_start_time)
        show_time.append(string_end_time)
        # more efficient to append (will loop over list backwards when printing to print first show first)
        show_times.append(show_time)
    return show_times


# Purpose: make a time 'clean' (ending in 0 or 5)
# Parameters: remainder, time
# Return: cleaned up time
def get_clean_time(remainder, time):
    # checking whether to subtract down so last digit is 0 or 5
    if remainder > 5:  # if greater than 5, want to subtract down to 5 instead of all the way to 0
        time = time - (remainder - 5)
    else:  # want to subtract down to 0 if remainder is less than 5
        time = time - remainder
    return time


# Purpose: convert a time that is in string format (hours:minutes or just minutes) to total number of minutes
# Parameters: time
# Return: total_minutes representing the time in only minutes
def convert_to_minutes(time):
    # splitting up hours and minutes
    hours_minutes = time.split(":")
    # checking if time has hours and minutes or just minutes (for runtime)
    if len(hours_minutes) == 1:
        return int(hours_minutes[0])
    # calculating total minutes through multiplying hours by 60 and adding minutes
    total_minutes = int(hours_minutes[0])*60 + int(hours_minutes[1])
    return total_minutes


# Purpose: converting an integer time to a string time (format-> 'hours:minutes')
# Parameters: time
# Return: string_time in correct format
def convert_to_hours_minutes(time):
    # dividing time by 60 to get hours
    hours = time // 60
    # get remainder indicating minutes
    minutes = time % 60
    # convert to string and add colon in between hours and minutes
    string_time = str(hours) + ":" + str(minutes).zfill(2)
    return string_time


# Purpose: print the schedule for each movie
# Parameters: user_input (command line), date, movies_array
# Return: none
def print_schedule(user_input, date, movies_array):
    print(user_input[0] + " " + user_input[1] + "\n")  # print call by user
    print(date + "\n")
    for movie in movies_array:
        print(movie)  # use __str__ in Movie class function to print each Movie object out in correct format




