class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self.__class__.all_articles.append(self)
        magazine.published_articles.append(self)
        author.authored_articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @classmethod
    def all(cls):
        return cls.all_articles

    def __eq__(self, other):
        if isinstance(other, Article):
            return self._author == other._author and self._magazine == other._magazine and self._title == other._title
        return False

    def __hash__(self):
        return hash((self._author, self._magazine, self._title))
