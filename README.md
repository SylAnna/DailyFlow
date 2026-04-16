# DailyFlow

DailyFlow is a Django-based task planner that combines a to-do list with a calendar view. It lets users create dated tasks, organize them by category, mark them complete, edit them later, and see scheduled tasks on a calendar.

## Features

- Add tasks with a date and optional category
- Mark tasks as complete or incomplete
- Edit or delete existing tasks
- View all tasks in a table layout
- Display scheduled tasks in a calendar view
- Store data locally with SQLite

## Tech Stack

- Python
- Django
- SQLite
- HTML templates
- CSS
- JavaScript
- FullCalendar loaded by CDN for the calendar page

## Project Structure

```text
DailyFlow/
|- manage.py
|- db.sqlite3
|- DailyFlow/
|  |- settings.py
|  |- urls.py
|- todo/
|  |- models.py
|  |- views.py
|  |- services.py
|  |- forms.py
|  |- templates/
|- static/
   |- css/
   |- js/
```

## Data Model

The app currently uses two main models:

- `Category`: stores a category name and color
- `List`: stores a task item, completion state, category, and date

## How To Run

1. Create and activate a virtual environment if you want an isolated setup.
2. Install Django:

```bash
pip install django
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Open the app in your browser at `http://127.0.0.1:8000/`

## Main Pages

- Home page
- To-do list page
- Edit task page
- Calendar page

## Notes

- The repository includes a local `db.sqlite3` file for development.
- The calendar UI depends on FullCalendar assets loaded from a CDN.
