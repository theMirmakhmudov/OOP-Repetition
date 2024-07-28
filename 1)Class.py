# Obyektlarni yaratish uchun shablon..  # noqa
# https://github.com/theMirmakhmudov
# https://youtube.com/@Mirmakhmudov_coder # noqa

# class
class Book:
    def __init__(self, book_name, book_id, book_author):
        self.book_name = book_name
        self.book_id = book_id
        self.book_author = book_author

    def say_book_name(self):
        return f"Book name is {self.book_name}"

# objects

fairy_tale_book = Book("Harry Potter and secret room", 1, "Joanna Ketlin Rouling")
print(fairy_tale_book.say_book_name())
