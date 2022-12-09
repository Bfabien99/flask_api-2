from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
    {"id": 1, "author": "Chinua Achebe",
        "language": "English", "title": "Things Fall Apart"},
    {"id": 2, "author": "Saint Augustine", "language": "English",
        "title": "Saint Augustine’s Confessions"},
    {"id": 3, "author": "Cicero", "language": "English", "title": "On Obligations"},
    {"id": 4, "author": "Livy", "language": "English", "title": "The Rise of Rome"},
    {"id": 5, "author": "Lucretius", "language": "English",
        "title": "On the Nature of the Universe"},
    {"id": 6, "author": "Marcus Aurelius",
        "language": "English", "title": "Meditations"},
    {"id": 7, "author": "Ovid", "language": "English", "title": "Metamorphoses"},
    {"id": 8, "author": "Tacitus", "language": "English",
        "title": "Agricola and Germany"},
    {"id": 9, "author": "Virgil", "language": "English", "title": "Georgics"},
    {"id": 10, "author": "Pierrot", "language": "French",
        "title": "Au clair de la lune"}
]


@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list)>0:
            return jsonify(books_list)
        else:
            return 'Nothing found!'
        
    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id']+1
        
        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }
        books_list.append(new_obj)
        
        return jsonify(new_obj), 201


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book),200
            pass
           
        return jsonify({'error':'Book not found'}),404
            
    if request.method == 'PUT':
        return jsonify(''),204
    
    if request.method == 'DELETE':
        return jsonify(''),204
        


if __name__ == '__main__':
    app.run(debug=True)
