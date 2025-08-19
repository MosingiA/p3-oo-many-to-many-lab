# lib/many_to_many.py

class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        """Return all contracts related to this book"""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Return all authors related to this book via contracts"""
        return [contract.author for contract in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return all contracts related to this author"""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return all books this author has contracts for"""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract for this author and a book"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Sum of all royalties from this author's contracts"""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        # Validate book
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        # Validate date
        if not isinstance(date, str):
            raise Exception("date must be a string")
        # Validate royalties
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts with a given date"""
        return [contract for contract in cls.all if contract.date == date]
