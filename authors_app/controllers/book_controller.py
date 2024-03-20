from flask import Blueprint, request, jsonify
from datetime import datetime
from authors_app.extensions import db,Books


book = Blueprint('book', __name__, url_prefix='/api/v1/book')

@book.route('/register', methods=['POST'])
def register_book():
    try:
        # Extracting request data
        id = request.json.get('id')
        title=request.json.get('title')
        description=request.json.get('description')
        price=request.json.get('price')
        price_unit=request.json.get('price_unit')
        pages= request.json.get('pages')
        genre=request.json.get('genre')
        created_at=request.json.get('created_at')
        updated_at=request.json.get('updated_at')

        # Basic input validation
        if not id:
            return jsonify({"error": 'Your book ID is required'})

        if not title:
            return jsonify({"error": 'Your book title is required'})

        if not description:
            return jsonify({"error": 'The description is required'})

        if not price:
            return jsonify({"error": 'The price is required'})

        if not price_unit:
            return jsonify({"error": 'The price_unit is required'})

        if not genre:
            return jsonify({"error": 'Please specify the genre'})

        # Creating a new book
        new_book = Books(
            id=id,
            title=title,
            description=description,
            price=price,
            price_unit=price_unit,
            pages=pages,
            genre=genre,
            created_at=created_at,
            updated_at=updated_at
        )

        # Adding and committing to the database
        db.session.add(new_book)
        db.session.commit()

        # Building a response message
        return jsonify({"message": f"Book '{new_book.title}', ID '{new_book.id}' has been uploaded"})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)})