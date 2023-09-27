# VarsityPro-Assignment-Task
# Django Blog Platform

Welcome to the Django Blog Platform project, created as part of the application for the Django Internship position at VarsityPro. This project is designed to showcase my skills in backend development using Django and Django Rest Framework.

I took on the challenge of implementing user authentication in two distinct ways. First, I created a separate Django app dedicated to user registration and authentication. This approach allowed me to customize the authentication process according to our project's specific requirements and create a seamless user experience.

Secondly, I leveraged Django Rest Framework's built-in session-based authentication for an alternative authentication method. This approach offered a more straightforward way for users to interact with the platform, using their existing session credentials for authentication. It demonstrated the flexibility of DRF in handling different authentication methods and provided users with options for accessing the platform securely.

These dual authentication methods not only added depth to the project but also showcased my ability to work with Django and DRF to provide a versatile and secure user authentication system. It further reinforced the importance of choosing the right authentication method depending on the project's specific needs and user expectations.
## Features

- Blog post creation, editing, and deletion.
- User profiles with optional profile pictures and bios.
- Comment system for blog posts.
- Optional features: - Tagging.
- Bonus: User registration and authentication.

## Getting Started

Follow these instructions to set up and run the project locally on your machine.

### Prerequisites

- Python (3.6 or higher)
- pip (Python package manager)
- Virtual environment (recommended for isolation)

### Installation

1. Clone this GitHub repository to your local machine:
   
```bash
git clone https://github.com/pranita28Dane/VarsityPro-Assignment-Task.git
```
2. Navigate to the project directory:

```bash
cd VarsityPro-Assignment-Task
```

3. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  
On Windows, use `venv\Scripts\activate`
```

4. Install project dependencies:

```bash
pip install -r requirements.txt
```

5. Perform database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser for admin access:

```bash
python manage.py createsuperuser
username: admin
password: admin
```

7. Start the development server:

```bash
python manage.py runserver
```

The project should now be running locally. You can access the admin panel at http://localhost:8000/ and use the superuser credentials you created to log in.

## API Documentation
For API documentation and usage examples, please refer to the API Documentation file.

## Testing
You can use tools like Postman to test the APIs provided by this project. Make sure the server is running locally before testing.




   
   
   
   
   
