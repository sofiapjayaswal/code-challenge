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
#
# def subtract_times(time1, time2):
#
# def compare_times(time1, time2):

