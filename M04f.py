from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'book_name': 'War and Peace',
        'author': 'Leo Tolstoy',
        'publisher': 'Russian Publishing House'
    },
    {
        'id': 2,
        'book_name': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'publisher': "Charles Scribner's Sons"
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        return jsonify({'error': 'Book not found'}), 404
    return jsonify(book[0])

@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        'id': books[-1]['id'] + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    book['book_name'] = request.json.get('book_name', book['book_name'])
    book['author'] = request.json.get('author', book['author'])
    book['publisher'] = request.json.get('publisher', book['publisher'])
    return jsonify(book)

@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book is None:
        return jsonify({'error': 'Book not found'}), 404
    books.remove(book)
    return jsonify({'result': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)
