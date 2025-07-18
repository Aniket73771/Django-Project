# 🧑‍💻 UserManagement – Django REST Framework Project

A simple user management system built with **Django** and **Django REST Framework**, featuring CRUD APIs and an optional **gRPC integration**.

---

## 🚀 Features

- Custom User model with:
  - `username`, `email`, `first_name`, `last_name`, `date_joined`
- Full CRUD API using ViewSets and Routers
- Field validations (e.g., unique email)
- Optional **gRPC Request** integrated as a Django management command

---

## 📁 Project Structure

UserManagement/
├── users/ # App with models, views, serializers
├── grpc_requests/ # gRPC request script
├── manage.py
├── README.md
└── Task_2_Scalability_Answer.pdf


---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone [https://github.com/Aniket73771/Django-Project.git]
   cd UserManagement

2. **Create a virtual environment**

python -m venv venv
source venv/bin/activate     # On Linux/macOS
venv\Scripts\activate        # On Windows

3. **Install dependencies**

pip install -r requirements.txt

4. **Run migrations**

python manage.py makemigrations
python manage.py migrate

5. **Run the server**

python manage.py runserver

6. **Access API**

Visit: http://127.0.0.1:8000/api/users/

---

## 🧪 API Endpoints


| Method | Endpoint           | Description            |
| ------ | ------------------ | ---------------------- |
| GET    | `/api/users/`      | List all users         |
| POST   | `/api/users/`      | Create a new user      |
| GET    | `/api/users/{id}/` | Retrieve a single user |
| PUT    | `/api/users/{id}/` | Update user info       |
| DELETE | `/api/users/{id}/` | Delete a user          |


----

## ⚙️ gRPC Integration (Optional Task)
A gRPC call is integrated as a Django management command for demonstration purposes.

## 📂 Script Location
grpc_requests/sample_request.py

Management command: users/management/commands/grpc_call.py


▶️ **To Run the gRPC Request**

python manage.py grpc_call

🧾 **Sample Output**

Making gRPC call to external API...
Sample gRPC response: Sunny, 25°C







