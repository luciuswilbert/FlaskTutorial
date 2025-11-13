from google import genai
from dotenv import load_dotenv
from flask import Flask, jsonify, request

import os

load_dotenv()

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

@app.route('/suggest-books', methods=['GET'])
def suggest_book():
    global books
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""
        You are a book recommender.

        Here is a list of books in JSON format:
        {books}

        Task:
        - Choose exactly ONE book from this list only.
        - Do NOT recommend any book that is not in the list.
        - Explain briefly why you chose it.

        Return the answer in plain text.
        """

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=prompt
    )
    response = response.text
    print(books)
    return jsonify({"response:": response})

if __name__ == '__main__':
    app.run(debug=True)