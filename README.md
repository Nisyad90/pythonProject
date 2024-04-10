# FastAPI CRUD Operations

This repository contains a simple CRUD (Create, Read, Update, Delete) operations implementation using FastAPI framework in Python.

## Requirements

- Python 3.7+
- FastAPI
- uvicorn (ASGI server)
- SQLAlchemy (optional, for database integration)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi-crud.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fastapi-crud
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2. Open your web browser and go to `http://localhost:8000/docs` to access the interactive API documentation (provided by Swagger UI).

3. You can test the CRUD operations using the Swagger UI or make HTTP requests using tools like curl, Postman, or your preferred API testing tool.

## API Endpoints

- `GET /items`: Retrieve all items.
- `GET /items/{item_id}`: Retrieve a single item by ID.
- `POST /items`: Create a new item.
- `PUT /items/{item_id}`: Update an existing item.
- `DELETE /items/{item_id}`: Delete an item.

## Database Integration (Optional)

If you want to integrate with a database (e.g., SQLite, PostgreSQL), you can modify the `database.py` file and the models in `models.py` accordingly. Don't forget to update the SQLAlchemy connection string in `main.py`.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for any improvements or features you'd like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
