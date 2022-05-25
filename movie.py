# Author: Sofia Jayaswal
# Date: 05/25/2022
# Purpose: create a Movie class containing important information for movies

class Movie:
    # Purpose: initialize Movie object
    # Parameters: name, release_year, rating, runtime
    # Return: none
    def __init__(self, name, release_year, rating, runtime):
        self.name = name
        self.rating = rating
        self.release_year = release_year
        self.runtime = runtime
        self.showtimes = []  # initialized as empty for all instances since show times need to be calculated

    # Purpose: return the runtime for the Movie object
    # Parameters: none
    # Return: runtime for the object that the function is called on
    def get_runtime(self):
        return self.runtime

    # Purpose: set the showtimes array of arrays equal to given array of arrays
    # Parameters: showtimes_array
    # Return: none
    def set_showtimes(self, showtimes_array):
        self.showtimes = showtimes_array

    # Purpose: prints movie object out with correct format (name, rating, and runtime + list of showtimes)
    # Parameters: none
    # Return: string representing the Movie object and its information
    def __str__(self):
        showtime_string = "  "  # initialize the string with two spaces (indentation)
        # looping backwards through the list since earlier showtimes are last in the list
        for i in range(len(self.showtimes)-1, -1, -1):
            showtime_string = showtime_string + self.showtimes[i][0] + " - " + self.showtimes[i][1] + "\n  "
        return self.name + " - Rated " + self.rating + ", " + self.runtime + "\n" + showtime_string

