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

![Home Page Screenshot](https://github.com/user-attachments/assets/cf7df1d4-6d27-4a9e-a8a4-e3e063930ed4)

![Home Page Screenshot](https://github.com/user-attachments/assets/d6886cca-fa58-42dc-9a0d-150aedde0ebd)

## License

