# Django Foundation Project

A beginner-friendly Django project that demonstrates basic pages, templates, database models, and recipe CRUD operations. The project includes a home page, informational pages, an admin site, and a recipe manager with image uploads.

## Features

- Home, About, Contact, and success pages
- Add recipes with a name, description, and optional image
- List all saved recipes
- Update and delete recipes
- SQLite database for local development
- Django admin interface
- Bootstrap styling loaded from a CDN

## Tech Stack

- Python
- Django 6.1.2
- SQLite
- Bootstrap

## Learning Progress



1. **Django project setup** - Installed Django, created the development environment, and learned the basic Django project structure.
2. **Django apps** - Learned why Django projects are divided into reusable apps and created apps for different areas of the project.
3. **Views and URLs** - Connected URL patterns to view functions and returned HTTP responses or rendered templates.
4. **Django templates** - Used template inheritance, template variables, loops, conditionals, and shared layouts with `base.html`.
5. **Models and migrations** - Defined database models, created migrations, and applied schema changes to the SQLite database.
6. **Django shell** - Practiced interacting with models and database records through Django's interactive shell.
7. **CRUD operations** - Implemented the create, read, update, and delete workflow for database-backed data.
8. **Recipe project, part 1** - Started the recipe application and created the recipe page and form structure.
9. **Recipe project, part 2** - Added the recipe model, form submission, image uploads, and recipe listing logic.
10. **Recipe project, part 3** - Completed recipe update and delete operations and connected the full recipe workflow to URLs and templates.
11. **Advanced authentication** - Learned the concepts and implementation approach for user registration, login, logout, and protected Django views.

The current codebase demonstrates the fundamentals from the early lessons and the recipe project. Authentication is the next area to integrate into the application.

## Project Structure

```text
.
├── Beginner/
│   ├── Beginner/       # Django project configuration and URL routes
│   ├── accounts/       # Accounts app
│   ├── home/           # Home and informational pages
│   ├── vege/           # Recipe model, views, and templates
│   ├── manage.py
│   └── db.sqlite3
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Create and activate a virtual environment

From the repository root in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, activate the environment from Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Apply migrations

```powershell
cd Beginner
python manage.py migrate
```

### 4. Start the development server

```powershell
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser.

## Application Routes

| URL | Description |
| --- | --- |
| `/` | Home page |
| `/about/` | About page |
| `/contact/` | Contact page |
| `/recipes/` | View and add recipes |
| `/update-recipe/<id>/` | Update a recipe |
| `/delete-recipe/<id>/` | Delete a recipe |
| `/admin/` | Django administration |

## Admin User

Create an administrator account with:

```powershell
python manage.py createsuperuser
```

Then visit <http://127.0.0.1:8000/admin/>.

## Running Tests

Run the Django test suite from the `Beginner` directory:

```powershell
python manage.py test
```

## Notes

- Uploaded recipe images are stored in `Beginner/public/static/recipe/` during local development.
- The project uses Django's development server and should be configured with production settings before deployment.
