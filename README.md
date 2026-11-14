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

## ORM Part 1

These queries were performed in the Django shell.

### Setup: Applying migrations and opening the Django shell

```powershell
PS D:\Django_Learning_Youtube\Beginner> python manage.py makemigrations
Migrations for 'vege':
  vege\migrations\0003_recipe_recipe_view_count.py
    + Add field recipe_view_count to recipe
PS D:\Django_Learning_Youtube\Beginner> python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, home, sessions, vege
Running migrations:
  Applying vege.0003_recipe_recipe_view_count... OK
PS D:\Django_Learning_Youtube\Beginner> python manage.py shell
15 objects imported automatically (use -v 2 for details).

Python 3.13.17 (tags/v3.13.17:64e080d, Oct 21 2026, 14:08:53) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```

### Query 1: Retrieving all recipes and recipe details

```pycon
>>> vege = Recipe.objects.all()
>>> vege
<QuerySet [<Recipe: Recipe object (2)>, <Recipe: Recipe object (4)>, <Recipe: Recipe object (7)>]>
>>> vege[0] 
<Recipe: Recipe object (2)>
>>> vege[0].recipe_name
"Paneer Biryani Recipe (Bhayi's Favourite Dish)"
>>> vege[0].recipe_view_count
1
>>> vege[0].recipe_description
'Chef:-  Sneha from Dandeli\r\n\r\nPaneer Biryani is a traditional, dum-cooked vegetarian biryani made by layering yogurt-marinated paneer with par-cooked basmati rice, fried onions (birista), herbs, saffron milk and ghee. Mildly spiced and delicately flavored, it’s a hearty one-pot dish that pairs perfectly with raita. Though it takes time to prepare, the result is always worth it – flavorful, filling, and simply irresistible. Cook it on the stovetop or in the oven.'
```

### Query 2: Updating recipe view counts

```pycon
>>> import random
>>> for veg in vege:
...     veg.recipe_view_count=random.randit(10,100)
... vege[0].recipe_view_count
  File "<console>", line 3
    vege[0].recipe_view_count
    ^^^^
SyntaxError: invalid syntax
>>> vege
<QuerySet [<Recipe: Recipe object (2)>, <Recipe: Recipe object (4)>, <Recipe: Recipe object (7)>]>
>>> vege[0] 
<Recipe: Recipe object (2)>
>>> vege[0].recipe_name
"Paneer Biryani Recipe (Bhayi's Favourite Dish)"
>>> vege[0].recipe_view_count
1
>>> vege[1].recipe_view_count
1
```

The first attempt uses the misspelled `random.randit` method and raises an error. The corrected query uses `random.randint`.

```pycon
>>> for veg in vege:
...     veg.recipe_view_count = random.randit(10,100)
...     veg.save()
... 
Traceback (most recent call last):
  File "<console>", line 2, in <module>
AttributeError: module 'random' has no attribute 'randit'. Did you mean: 'randint'?
>>> vege[0].recipe_view_count
1
>>> vege[1].recipe_view_count
1
>>> for veg in vege:
...     veg.recipe_view_count = random.randint(10,100)
...     veg.save()
... 
>>> vege[0].recipe_view_count
89
>>> vege[1].recipe_view_count
79
>>> vege[2].recipe_view_count
43
```

### Query 3: Ordering recipes by view count

```pycon
>>> vege = Recipe.objects.all().order_by('recipe_view_count')
>>> vege
<QuerySet [<Recipe: Recipe object (7)>, <Recipe: Recipe object (4)>, <Recipe: Recipe object (2)>]>
>>> vege = Recipe.objects.all().order_by('-recipe_view_count')
>>> vege
<QuerySet [<Recipe: Recipe object (2)>, <Recipe: Recipe object (4)>, <Recipe: Recipe object (7)>]>
```

### Query 4: Retrieving the most-viewed recipes

```pycon
>>> vege = Recipe.objects.all().order_by('-recipe_view_count')[0:1]
>>> vege
<QuerySet [<Recipe: Recipe object (2)>]>
>>> vege = Recipe.objects.all().order_by('-recipe_view_count')[0:2]
>>> vege
<QuerySet [<Recipe: Recipe object (2)>, <Recipe: Recipe object (4)>]>
```

### Query 5: Filtering recipes by view count

```pycon
>>> Recipe.objects.filter(recipe_view_count__gte = 50)
<QuerySet [<Recipe: Recipe object (2)>, <Recipe: Recipe object (4)>]>
>>> Recipe.objects.filter(recipe_view_count__gte = 50)[0]
<Recipe: Recipe object (2)>
>>> Recipe.objects.filter(recipe_view_count__gte = 50)[0].recipe_view_count
89
>>> Recipe.objects.filter(recipe_view_count__gte = 50)[1].recipe_view_count
79
>>> Recipe.objects.filter(recipe_view_count__lte = 50)
<QuerySet [<Recipe: Recipe object (7)>]>
>>> Recipe.objects.filter(recipe_view_count__lte = 50)[0].recipe_view_count
43
>>>
```

## ORM (Advanced Queries) Part 3

These queries were performed in the Django shell.

### Query 1: Retrieving student names starting with specific letters

```pycon
>>> from vege.models import *
>>> queryset = Student.objects.filter(student_name__startswith = "su")
>>> queryset
<QuerySet [<Student: Sumit Rathod>]>
>>> queryset = Student.objects.filter(student_name__startswith = "s")
>>> queryset
<QuerySet [<Student: Stephanie Jones>, <Student: Sumit Rathod>]>
>>> queryset = Student.objects.filter(student_name__startswith = "a")
>>> queryset
<QuerySet [<Student: Amy Curry>, <Student: Ashley Douglas>]>
>>>
```

### Query 2: Retrieving student emails ending with specific domains

```pycon
>>> queryset = Student.objects.filter(student_email__endswith = ".org")
>>> queryset
<QuerySet [<Student: Barbara Torres>, <Student: Bridget Riley>, <Student: Chris Burns>, <Student: James Tucker>, <Student: Mallory Stephens>, <Student: Randy Schaefer>, <Student: Richard Mitchell>, <Student: Tammy Brooks>]>
>>> queryset = Student.objects.filter(student_email__endswith = ".com")
>>> queryset
<QuerySet [<Student: Amy Curry>, <Student: Colleen Chavez>, <Student: Heather Gonzalez>, <Student: Jacob Ingram>, <Student: Justin Ibarra>, <Student: Robert Brown>, <Student: Robert Foster>, <Student: Robert Larson>, <Student: Stephanie Jones>, <Student: Sumit Rathod>, <Student: Tom Walls>, <Student: Zachary Thomas>]>
>>>
```

### Query 3: Retrieving student names containing a substring

```pycon
>>> queryset = Student.objects.filter(student_name__icontains = "an")
>>> queryset
<QuerySet [<Student: Christian Conley>, <Student: Daniel Stone>, <Student: Emily Daniels>, <Student: Randy Schaefer>, <Student: Stephanie Jones>]>
>>> queryset = Student.objects.filter(student_name__icontains = "um")
>>> queryset
<QuerySet [<Student: Sumit Rathod>]>
>>>
```

### Query 4: Retrieving student names from a department

The foreign key relationship between `Student` and `Department` is used here.

```pycon
>>> queryset = Student.objects.filter(department__department = "Civil")
>>> queryset
<QuerySet [<Student: Amy Curry>, <Student: Ashley Douglas>, <Student: Pamela Schneider>, <Student: Raymond Brown>]>
>>> queryset = Student.objects.filter(department__department = "Computer Science")
>>> queryset
<QuerySet [<Student: Christian Conley>, <Student: Colleen Chavez>, <Student: Daniel Stone>, <Student: Emily Daniels>, <Student: Heather Gonzalez>, <Student: Robert Brown>, <Student: Robert Foster>, <Student: Sumit Rathod>]>
>>>
```

### Query 5: Retrieving students belonging to Civil or Electrical

```pycon
>>> d = ["Civil", "Electrical"]
>>> d
['Civil', 'Electrical']
>>> queryset = Student.objects.filter(department__department__in = d)
>>> queryset
<QuerySet [<Student: Amy Curry>, <Student: Ashley Douglas>, <Student: Bridget Riley>, <Student: Chris Burns>, <Student: James Tucker>, <Student: Jeff Frey>, <Student: Justin Ibarra>, <Student: Michael Wilson>, <Student: Oscar Terrell>, <Student: Pamela Schneider>, <Student: Randy Schaefer>, <Student: Raymond Brown>, <Student: Richard Mitchell>, <Student: Stephanie Jones>, <Student: Tammy Brooks>, <Student: Zachary Thomas>]>
>>>
```

### Query 6: Retrieving students from all departments except Civil

```pycon
>>> queryset = Student.objects.exclude(department__department = "Civil")
>>> queryset
<QuerySet [<Student: Barbara Torres>, <Student: Bridget Riley>, <Student: Chris Burns>, <Student: Christian Conley>, <Student: Colleen Chavez>, <Student: Daniel Stone>, <Student: Emily Daniels>, <Student: Heather Gonzalez>, <Student: Jacob Ingram>, <Student: James Tucker>, <Student: Jeff Frey>, <Student: Justin Ibarra>, <Student: Mallory Stephens>, <Student: Michael Wilson>, <Student: Michaela Hall>, <Student: Oscar Terrell>, <Student: Randy Schaefer>, <Student: Richard Mitchell>, <Student: Robert Brown>, <Student: Robert Foster>, '...(remaining elements truncated)...']>
>>> queryset.count()
27
>>>
```

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
