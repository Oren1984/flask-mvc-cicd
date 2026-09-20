# Architecture

## What

The application is a small Flask app that follows the MVC (Model-View-Controller) pattern, providing CRUD (Create, Read, Update, Delete) management of `User` records backed by MySQL.

```text
app/
├── __init__.py               # Application factory (create_app)
├── controllers/
│   └── main.py                # Routes / request handling
├── models/
│   └── user.py                 # SQLAlchemy data model
└── views/
    └── templates/               # Jinja2 templates (Bootstrap 5 UI)
        ├── base.html
        ├── index.html
        ├── add_user.html
        └── edit_user.html
```

## Why

Separating routes (controller), data model, and templates (view) keeps the app easy to extend and mirrors the structure most Flask CRUD tutorials and production apps use, which is the point of this project — demonstrating a realistic, conventional layout rather than a single-file script.

## How

### Application factory

`app/__init__.py` defines `create_app()`, which:

1. Creates the Flask app and points its template folder at `app/views/templates`.
2. Loads configuration from `config.Config`.
3. Initializes Flask-SQLAlchemy (`db`).
4. Registers the `main` blueprint (`app/controllers/main.py`).
5. Calls `db.create_all()` inside the app context so tables are created automatically on startup.

`run.py` calls `create_app()` and starts the Flask development server on `0.0.0.0:5000` with `debug=True`.

> Note: schema creation happens via `db.create_all()`, not migrations. There is no Alembic (or similar) migration tooling in this repo, so schema changes require manual intervention against the database.

### Routes (`app/controllers/main.py`)

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/` | List all users |
| `GET`, `POST` | `/add` | Show the add-user form / create a user |
| `GET`, `POST` | `/edit/<int:user_id>` | Show the edit form / update a user |
| `POST` | `/delete/<int:user_id>` | Delete a user |

All write operations flash a status message and redirect back to `/`.

### Data model (`app/models/user.py`)

```text
User
├── id            Integer, primary key
├── username      String(64), unique, required
├── email         String(120), unique, required
└── created_at    DateTime, defaults to UTC now
```

### Views

Templates extend `base.html`, which loads Bootstrap 5 from a CDN and renders flashed messages. `index.html` lists users in a table with Edit/Delete actions; `add_user.html` and `edit_user.html` provide the create/update forms.
