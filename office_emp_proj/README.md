# 🏢 Office Employee Management System

A Django-based web application designed to manage employee records, attendance, and payroll efficiently. This system provides an easy-to-use interface for handling employee data in an organization.

---

## 🚀 Features

- 👨‍💼 Employee Management (Add, Update, Delete)
- 📅 Attendance Tracking
- 💰 Payroll Management
- 📊 Structured Database using SQLite
- 🔐 Admin-controlled system
- 🌐 Clean and responsive UI

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite3

---

## 📂 Project Structure
office_emp_proj/
│
├── attendance/ # Handles attendance functionality

├── emp_app/ # Employee management module
 
├── payroll/ # Payroll management module

├── office_emp_proj/ # Main project settings

├── db.sqlite3 # Database

├── manage.py # Django management script

├── erd.png # Database ER diagram

└── erd.dot # ERD source file


---

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/ritigyas/office_emp_proj.git
cd office_emp_proj
```

2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```
4. Install dependencies
```bash
pip install django
```
5. Run migrations
```bash
python manage.py migrate
```
6. Start the server
```bash
python manage.py runserver
```
7. Open in browser:
```bash
http://127.0.0.1:8000/
```
## 🔑 Admin Access

Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

Then login at:
```bash
http://127.0.0.1:8000/admin/
```

## 📌 Future Improvements
REST API integration
Role-based authentication
Dashboard analytics
Deployment (AWS/Heroku)

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## 📄 License

This project is open-source and available under the MIT License.

## 👩‍💻 Author

Ritigya Singh
