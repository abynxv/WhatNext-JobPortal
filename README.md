# What Next - Job Portal

>This project is under development and not yet final; ongoing testing, feature additions, templates design and code adjustments are in progress 📈

What Next is a job portal web application built with Django. It facilitates connections between employers and job seekers, allowing employers to post jobs and employees to apply for them.

## Features

- User authentication (Employee and Employer signup/login)
- Employee and Employer dashboard
- Job posting and management for employers
- Job search and application for employees
- Profile management for both employers and employees

## Installation

1. Clone the repository:

       git clone https://github.com/your-username/WhatNext-JobPortal.git
       cd WhatNext-JobPortal
2. Create a virtual environment and activate it:

       python -m venv venv
       source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Install the requirements:
 
       pip install -r requirements.txt
4. Run migrations:

       python manage.py migrate
5. Create a superuser:

       python manage.py createsuperuser
6. Run the development server:

       python manage.py runserver

## Project Structure

The project consists of two main Django apps:

1. `jobs`: Handles job-related functionality
2. `accounts`: Manages user authentication and profiles

## API Endpoints

### Jobs App

- Home: `GET /`
- Search: `GET /search`
- Employer Dashboard: `GET /employer/dashboard`
- All Applicants: `GET /employer/dashboard/all-applicants`
- Applicants per Job: `GET /employer/dashboard/applicants/<int:job_id>`
- Mark Job as Filled: `GET /employer/dashboard/mark-filled/<int:job_id>`
- Edit Job: `GET, POST /employer/dashboard/edit/<int:pk>`
- Delete Job: `GET, POST /employer/dashboard/delete/<int:pk>`
- Apply for Job: `GET, POST /apply-job/<int:job_id>`
- Job List: `GET /jobs`
- Job Details: `GET /jobs/<int:id>`
- Create Job: `GET, POST /employer/jobs/create`
- Employer Profile: `GET /employer/profile/`
- Edit Employer Profile: `GET, POST /employer/edit-profile/`

### Accounts App

- Employee Registration: `GET, POST /employee/register`
- Employer Registration: `GET, POST /employer/register`
- Update Employee Profile: `GET, POST /employee/profile/update`
- Logout: `GET /logout`
- Login: `GET, POST /login`

## Usage

1. Employers can register and create job listings.
2. Job seekers can register as employees and browse job listings.
3. Employees can apply for jobs.
4. Employers can view applicants and manage their job postings.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Screenshots

![Project Image - 01](https://github.com/user-attachments/assets/c8daedc8-c5cc-4b08-a4d6-ef41e0f3d485)
![Project Image - 02](https://github.com/user-attachments/assets/a0c50537-405d-4ddf-a9e7-3d0878bf6ec7)
![Project Image - 03](https://github.com/user-attachments/assets/e52b1e29-04c1-41a4-9a37-9c8d5055a607)
![Project Image - 04](https://github.com/user-attachments/assets/99655554-8daf-4aaf-bc78-ad1ac5aded58)
![Project Image - 05](https://github.com/user-attachments/assets/a62bd6aa-969e-4aac-be89-ba7db8e96364)
![Project Image - 06](https://github.com/user-attachments/assets/7b02b012-f8d4-4bc3-9132-89b0f77332ef)
![Project Image - 07](https://github.com/user-attachments/assets/6a136ae8-8710-4694-a378-0ed093464b0b)

## License

