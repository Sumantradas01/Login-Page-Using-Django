# Login-Page-Using-Django

A simple and secure login page built using Django. This project demonstrates basic user authentication, registration, and session management with Django’s built-in authentication system. It is suitable for learning purposes or as a starting point for more complex applications.

## Features

- User registration and login
- Secure password handling using Django’s auth system
- Logout functionality
- Friendly error messages and form validation
- Modular Django project structure

## Setup Instructions

### Prerequisites

- Python 3.7+
- pip
- Virtualenv (optional, but recommended)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sumantradas01/Login-Page-Using-Django.git
    cd Login-Page-Using-Django/shop
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Django:**
    ```bash
    pip install django
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin account):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` in your browser.

## Usage Examples

- **Register a new user:** Go to the registration page, fill in the required details, and submit.
- **Login:** Enter your credentials on the login page.
- **Logout:** Click the logout button to end your session.
- **Admin Panel:** Visit `/admin` to access the Django admin panel (requires superuser).

## Project Structure

```
shop/
├── manage.py
├── <your_app_name>/
│   ├── migrations/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
└── shop/
    ├── settings.py
    ├── urls.py
    └── ...
```

## Contributing

Pull requests and suggestions are welcome!

## License

This project is licensed under the MIT License.
