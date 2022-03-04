n = int(input("enter the number of book details:"))
booklist = []
for i in range(0,n):
    book_name = input("enter the book name:")
    author_name = input("enter the author name:")
    price = input("enter the book price:")
    publish = input("enter the pulisher name:")
    book = {
        "book name" : book_name,
        "author name": author_name,
        "price": price,
        "publisher": publish
    }
    booklist.append(book)
    print(booklist)

