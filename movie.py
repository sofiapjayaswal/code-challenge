
class Movie:
    def __init__(self, name, release_year, rating, runtime):
        self.name = name
        self.rating = rating
        self.release_year = release_year
        self.runtime = runtime
        # self.showtimes = showtimes

    def get_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def get_runtime(self):
        return self.runtime

    def __str__(self):
        # return "["+self.name + ", " + self.rating + ", " + self.release_year + ", " + self.runtime+"]"
        return self.name+","+self.rating

