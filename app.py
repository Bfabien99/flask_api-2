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


@app.route('/books')
def index():
    return 'Hello world'


@app.route('/<name>')
def print_name(name):
    return 'His , {}'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
