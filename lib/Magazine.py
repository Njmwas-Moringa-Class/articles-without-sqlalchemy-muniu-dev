class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self.additional_info = {}
        self.published_articles = []
        self.__class__.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @classmethod
    def all(cls):
        return cls.all_magazines

    @classmethod
    def find_by_name(cls, name):
        return [magazine for magazine in cls.all_magazines if magazine.name == name]

    def add_article(self, article):
        self.published_articles.append(article)

    def article_titles(self):
        return [article.title for article in self.published_articles]

    def contributors(self):
        contributors = set()
        for article in self.published_articles:
            contributors.add(article.author)
        return list(contributors)

    def __str__(self):
        return f"Magazine: {self._name}, Category: {self._category}, Additional Info: {self.additional_info}"

    def __eq__(self, other):
        if isinstance(other, Magazine):
            return self._name == other._name and self._category == other._category
        return False

    def __hash__(self):
        return hash((self._name, self._category))
