from flask import Flask, jsonify, request
app = Flask(__name__)

books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_books_by_id(book_id):
    book = next((book for book in books if book['id'] == book_id), any)
    return jsonify(book)

@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.json
    print(request.json)
    books.append(new_book)
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['PUT'])
def edit_book(book_id):
    book = next((book for book in books if book['id'] == book_id), any)
    if not book:
        return jsonify({"error": "Book not Found"})
    
    data = request.json
    print(data)
    book.update(data)
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)