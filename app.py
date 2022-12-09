from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('books.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/books', methods=['GET', 'POST'])
def books():
    conn = db_connection()
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor = conn.execute("SELECT * FROM book")
        books = [
            dict(id=row[0], author=row[1], language=row[2], title=[row[3]])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)
        else:
            return jsonify({'message':'Nothing found!'}), 200
        
    if request.method == 'POST':
        new_author = request.form['author'].capitalize()
        new_lang = request.form['language'].capitalize()
        new_title = request.form['title'].capitalize()
        sql = """INSERT INTO book (author, language, title) VALUES (?, ?, ?)"""
        cursor = conn.execute(sql, (new_author, new_lang, new_title))
        conn.commit()
        new_obj = {
            'id': cursor.lastrowid,
            'author': new_author,
            'language': new_lang,
            'title': new_title
        }
        
        return jsonify(new_obj), 201


@app.route('/book/<id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id=?", (id,))
        
        for row in cursor.fetchall():
            book = dict(id=row[0], author=row[1], language=row[2], title=[row[3]])
            
        if book is not None:
            return jsonify(book), 200
        else:
            return jsonify({'message':'Nothing found!'}), 404
            
    if request.method == 'PUT':
        sql = "UPDATE book SET author=?, language=?, title=? WHERE id=?"
        
        author = request.form['author']
        language = request.form['language']
        title = request.form['title']
        
        book_update = {
            'id': id,
            'author': author,
            'language': language,
            'title': title
        }
        cursor.execute(sql, (author, language, title, id))
        conn.commit()
        return jsonify(book_update),202
    
    if request.method == 'DELETE':
        sql = "DELETE FROM book WHERE id=?"
        cursor.execute(sql, (id,))
        conn.commit()
        return jsonify({'message':'Book {} was deleted'.format(id)}),202
        


if __name__ == '__main__':
    app.run(debug=True)
