# Django Basic CRUD

A simple Django project demonstrating basic CRUD (Create, Read, Update, Delete) operations for managing products.

## Features

- Add new products with name, description, and price.
- View a list of all products.
- Update existing product details.
- Delete products from the database.
- Utilizes Django's built-in admin interface for product management.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/WaqasAly/Django-Basic-Crud.git
   cd Django-Basic-Crud
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\activate
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   - Frontend: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure

```
Django-Basic-Crud/
├── crud/
│   ├── migrations/
│   ├── templates/
│   │   └── crud/
│   │       ├── create_product.html
│   │       ├── product_list.html
│   │       └── update_product.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── crud_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

## Usage

- **Create Product:** Navigate to `/create/` to add a new product.
- **View Products:** Visit `/` to see the list of all products.
- **Update Product:** Click on the "Edit" link next to a product to update its details.
- **Delete Product:** Click on the "Delete" link next to a product to remove it.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.
