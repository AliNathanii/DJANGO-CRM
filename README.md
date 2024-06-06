# CRM Project

This is a Customer Relationship Management (CRM) system built using Django, Python, and MySQL.

## Features

- User authentication (login, logout, register)
- Add, view, update, and delete customer records
- Display a list of all customer records
- Flash messages for user feedback

## Prerequisites

- Python 3.x
- Django 4.x
- MySQL
- Virtual environment (optional but recommended)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    - Update your `settings.py` file with your database credentials:

      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'crmdatabase',
              'USER': 'your_db_user',
              'PASSWORD': 'your_db_password',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }
      ```

5. **Run migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

8. **Access the application:**

    Open your browser and go to `http://localhost:8000/`

## Project Structure

- `manage.py`: Django's command-line utility for administrative tasks.
- `ourcrm/settings.py`: Settings and configuration for the Django project.
- `ourcrm/urls.py`: URL declarations for the Django project.
- `crmweb/models.py`: Definition of the `Record` model.
- `crmweb/views.py`: Views to handle user requests.
- `crmweb/forms.py`: Forms for user input.
- `crmweb/templates/`: HTML templates for the application.
- `crmweb/migrations/`: Database migrations for the `Record` model.

## Usage

- **Home Page:** Displays a list of all customer records.
- **Register:** Allows a new user to register an account.
- **Login:** Allows an existing user to log in.
- **Logout:** Logs out the current user.
- **Add Record:** Allows a logged-in user to add a new customer record.
- **Update Record:** Allows a logged-in user to update an existing customer record.
- **Delete Record:** Allows a logged-in user to delete a customer record.
- **View Record:** Allows a logged-in user to view details of a customer record.

## Example Code

### `manage.py`

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ourcrm.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
