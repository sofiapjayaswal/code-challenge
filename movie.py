
class Movie:
    def __init__(self, name, release_year, rating, runtime):
        self.name = name
        self.rating = rating
        self.release_year = release_year
        self.runtime = runtime
        self.showtimes = []

    def get_runtime(self):
        return self.runtime

    # def set_showtimes(self, showtimes_array):
    #     self.showtimes = showtimes_array

    def __str__(self):
        showtime_string = "  "
        for i in range(len(self.showtimes)-1, -1, -1):
            showtime_string = showtime_string + self.showtimes[i][0] + " - " + self.showtimes[i][1] + "\n  "
        return self.name + " - Rated " + self.rating + ", " + self.runtime + "\n" + showtime_string

