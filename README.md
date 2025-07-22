# Arxiv 🎓

Arxiv is a Django web app to manage student records (name, surname, faculty, group, grade) with a simple HTML/CSS frontend and Django admin support.

## 🚀 Features
- Add student info via form
- Store data in Django database
- Manage records from admin panel

## 🛠️ Tech Stack
- Python 3.x
- Django
- HTML/CSS
- SQLite

## 📦 Setup

```bash
git clone https://github.com/N0d1rb3k/arxiv.git
cd arxiv
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt  # or just: pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open in browser: http://127.0.0.1:8000

## 🔐 Admin Panel

```bash
python manage.py createsuperuser
```

Login at: http://127.0.0.1:8000/admin/

## 📂 Project Structure
```
arxiv/
├── main/         # App logic
├── templates/    # HTML files
├── static/       # CSS
├── db.sqlite3    # Default DB
└── manage.py     # Django tool
```

## 🤝 Contributing
Pull requests welcome!

## 📄 License
MIT

## 👤 Author
Xonimqulov Nodirbek — [github.com/N0d1rb3k](https://github.com/N0d1rb3k)
