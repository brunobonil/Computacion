from repository import Repository


class BookService():
    def add_book(self, book):
        ultKey = -1
        for key in Repository.booksList:
            ultKey = key
        ultKey = ultKey + 1
        Repository.booksList[ultKey] = book.__dict__
        return (ultKey)

    def update_book(self, key, update):
        existe = False
        for books in Repository.booksList:
            if books == key:
                existe = True
                break
        if existe:
            Repository.booksList[key] = update.__dict__
        else:
            raise ValueError

    def assign_book(self, book_id, memberLegajo):
        existe = False
        for book in Repository.booksList:
            if book == book_id:
                existe = True
                break
        if existe:
            Repository.booksList[book_id]['_memberLegajo'] = memberLegajo
        else:
            raise ValueError
