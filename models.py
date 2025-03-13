from bson import ObjectId

class Movie:
    def __init__(self, title, genre, release_date, popularity, rating, revenue=None, budget=None, bookmarked=False):
        self.title = title
        self.genre = genre
        self.release_date = release_date
        self.popularity = popularity
        self.rating = rating
        self.revenue = revenue
        self.budget = budget
        self.bookmarked = bookmarked

    def to_dict(self):
        return self.__dict__
