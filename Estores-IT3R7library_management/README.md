# 📚 Library Management System - Django

A complete library management system built with Django featuring full CRUD operations based on the ERD design from IT3R7 course.

## ✨ Features

- ✅ **Library Management** - Create and manage multiple libraries
- ✅ **Author Management** - Add, update, and delete authors
- ✅ **Book Management** - Track books with author and library relationships
- ✅ **Member Management** - Register members and track borrowed books
- ✅ **Full CRUD Operations** - Create, Read, Update, Delete for all entities
- ✅ **Beautiful UI** - Modern gradient design with intuitive navigation
- ✅ **Admin Panel** - Django's built-in admin interface for advanced management

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher installed
- pip (Python package manager)

### Installation Steps

1. **Extract the project folder** to your desired location

2. **Open Terminal/Command Prompt** and navigate to the project folder:
   ```bash
   cd path/to/library_management_complete
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   # On Windows:
   python -m venv venv
   venv\Scripts\activate

   # On Mac/Linux:
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install Django**:
   ```bash
   pip install django
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create an admin user** (optional but recommended):
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set username, email, and password.

7. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Open your browser** and visit:
   - **Main Application**: http://127.0.0.1:8000/
   - **Admin Panel**: http://127.0.0.1:8000/admin/

## 📖 Usage Guide

### Using the Web Interface

1. **Create a Library First**
   - Navigate to Libraries → Create New Library
   - A unique ID will be automatically assigned

2. **Add Authors**
   - Go to Authors → Add New Author
   - Fill in the author's details (name, phone, gender, birth year)

3. **Add Books**
   - Go to Books → Add New Book
   - Select an author and library from the dropdowns
   - Enter book name and publication date

4. **Register Members**
   - Go to Members → Register New Member
   - Fill in member details
   - Select a book they're borrowing

### Using the Admin Panel

1. Visit http://127.0.0.1:8000/admin/
2. Login with your superuser credentials
3. You can manage all entities with advanced filtering and search

## 🗂️ Project Structure

```
library_management_complete/
├── library_project/          # Django project settings
│   ├── __init__.py
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── library/                  # Main application
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   └── library/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── author_list.html
│   │       ├── book_list.html
│   │       └── ... (other templates)
│   ├── __init__.py
│   ├── admin.py            # Admin panel configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models (ERD)
│   ├── urls.py             # App URL routing
│   └── views.py            # Business logic
├── manage.py                # Django management script
└── README.md               # This file
```

## 💾 Database Models (ERD)

### Library
- `library_id` (Primary Key, Auto)

### Author
- `author_id` (Primary Key, Auto)
- `author_name` (CharField)
- `phone_number` (CharField)
- `gender` (CharField with choices)
- `date_birth_year` (DateField)

### Book
- `book_id` (Primary Key, Auto)
- `book_name` (CharField)
- `author` (Foreign Key → Author)
- `library` (Foreign Key → Library)
- `date_published` (DateField)

### Member
- `member_id` (Primary Key, Auto)
- `member_name` (CharField)
- `phone_number` (CharField)
- `gender` (CharField with choices)
- `birth_year` (DateField)
- `book` (Foreign Key → Book)

## 🔧 Common Commands

```bash
# Run development server
python manage.py runserver

# Create new migrations (after model changes)
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Access Python shell with Django
python manage.py shell
```

## 📝 Assignment Notes

This project fulfills the requirements for the IT3R7 assignment dated 2/3/2026:

1. ✅ Implemented Create, Read, and Delete operations
2. ✅ Used the ERD created during face-to-face session
3. ✅ **BONUS**: Implemented Update operation for all entities

### Submitting to GitHub

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Library Management System - IT3R7 Assignment"

# Add remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/YOUR_USERNAME/library-management-django.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Don't forget to fill out the Google Form: https://forms.gle/6jhjeGScExE3JRzv9

## 🎨 Technologies Used

- **Backend**: Python 3.x, Django 5.x
- **Database**: SQLite (default)
- **Frontend**: HTML5, CSS3 (embedded in templates)
- **Design**: Gradient UI with modern styling

## 📚 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Python Documentation](https://docs.python.org/)

## 👨‍💻 Author

**Student**: IT3R7 Group 1  
**Course**: Library Management System  
**Date**: February 3, 2026  
**Instructor**: Mario Marlon D. Tumamak

## 📄 License

This project is created for educational purposes as part of IT3R7 coursework.

---

**Enjoy managing your library! 📖✨**

For any questions or issues, please contact your instructor.
