# Dating Website

A fully functional dating website built with Django featuring user registration, profile management, and admin functionality.

## Features

### User Features
- **User Registration**: New users can register with username, first name, last name, email, phone, profile picture, and gender
- **Gender Options**: Male, Female, Couple, Others
- **User Authentication**: Secure login/logout functionality
- **Profile Management**: Users can view and edit their own profile
- **Profile Picture Upload**: Users can upload and update their profile pictures
- **Security**: Users can only edit their own profiles, not other users' profiles

### Admin Features
- **Admin Dashboard**: View all registered users in a comprehensive table
- **User Management**: Admins can edit any user's credentials including:
  - Username
  - First name and Last name
  - Email
  - Phone number
  - Gender
  - Profile picture
  - Role (User/Admin)
  - Account status (Active/Inactive)
  - Password (optional password reset)
- **User Deletion**: Admins can delete user accounts
- **Django Admin Panel**: Full access to Django's admin interface

### User Roles
- **Normal User**: Can register, login, and edit their own profile
- **Admin User**: Has all user permissions plus access to admin dashboard and can manage all users

## Project Structure

```
DatingApp/
├── manage.py
├── Dating_Website/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                    # Main app (landing page)
│   ├── templates/
│   │   ├── base.html
│   │   └── main/
│   │       └── landing.html
│   ├── views.py
│   └── urls.py
├── user/                    # User authentication and management
│   ├── models.py            # Custom User model
│   ├── forms.py             # Registration and profile forms
│   ├── views.py             # User and admin views
│   ├── admin.py             # Django admin configuration
│   ├── urls.py              # User-related URLs
│   └── templates/
│       └── user/
│           ├── register.html
│           ├── login.html
│           ├── profile.html
│           ├── admin_dashboard.html
│           ├── admin_edit_user.html
│           └── admin_delete_user.html
└── media/                   # User uploaded files (profile pictures)
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Steps

1. **Navigate to the project directory**
   ```bash
   cd /home/nadeem/Documents/DatingApp
   ```

2. **Activate the virtual environment** (already created)
   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies** (already installed)
   ```bash
   pip install Django Pillow
   ```

4. **Run migrations** (already done)
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account. Make sure to set the role to 'admin' either through the Django admin panel or by updating the database.

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Landing Page: http://127.0.0.1:8000/
   - User Registration: http://127.0.0.1:8000/user/register/
   - User Login: http://127.0.0.1:8000/user/login/
   - User Profile: http://127.0.0.1:8000/user/profile/
   - Admin Dashboard: http://127.0.0.1:8000/user/admin/dashboard/
   - Django Admin: http://127.0.0.1:8000/admin/

## Usage

### For Regular Users

1. **Registration**: Click "Register" on the landing page
   - Fill in all required fields (username, first name, last name, email, gender, password)
   - Optionally add phone number and profile picture
   - Submit the form to create your account

2. **Login**: Use your username and password to login

3. **View/Edit Profile**: 
   - After logging in, you'll be redirected to your profile page
   - View your current information on the left panel
   - Edit your details using the form on the right
   - Upload or change your profile picture

4. **Logout**: Click "Logout" in the navigation bar

### For Admin Users

1. **Access Admin Dashboard**: 
   - Login with an admin account
   - Click "Admin Dashboard" in the navigation bar

2. **View All Users**: See a comprehensive table of all registered users with their details

3. **Edit Users**:
   - Click "Edit" next to any user
   - Modify any field including username, email, role, etc.
   - Change user password (optional)
   - Activate/deactivate accounts

4. **Delete Users**:
   - Click "Delete" next to any user
   - Confirm deletion on the confirmation page

### Django Admin Panel

Access the Django admin panel at http://127.0.0.1:8000/admin/ for advanced user management and database operations.

## Technologies Used

- **Backend**: Django 5.2.8
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, Bootstrap 5.3.0
- **Image Processing**: Pillow (for profile picture uploads)

## Security Features

- Password hashing and validation
- CSRF protection
- User authentication required for profile access
- Role-based access control for admin features
- Profile editing restricted to profile owners
- Secure file upload handling

## Models

### User Model (Custom)
- Extends Django's AbstractUser
- Fields:
  - `username` (unique)
  - `first_name`
  - `last_name`
  - `email` (unique)
  - `phone` (optional, validated)
  - `profile_pic` (ImageField)
  - `gender` (choices: Male, Female, Couple, Others)
  - `role` (choices: User, Admin)

## Future Enhancements

- User matching algorithm
- Messaging system between users
- Advanced search and filters
- User preferences and interests
- Email verification
- Password reset functionality
- Social media integration
- User blocking/reporting system

## Contributing

Feel free to fork this project and submit pull requests for any enhancements.

## License

This project is for educational purposes.
