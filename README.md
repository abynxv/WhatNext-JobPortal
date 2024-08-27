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

### Main URLs
- `/admin/`: Django admin interface
- All other routes are included from the `jobs` and `accounts` apps

### Accounts App
- `/employer/register`: Register a new employer account
- `/candidate/register`: Register a new candidate account
- `/candidate/profile`: View candidate profile
- `/candidate/profile/edit`: Edit candidate profile
- `/candidate/applications`: View candidate's job applications
- `/candidate/applications/delete/<int:pk>/`: Delete a specific job application
- `/logout`: Log out the current user
- `/login`: Log in a user

### Jobs App
- `/`: Home page
- `/search`: Search for jobs
- `/employer/dashboard/`: Employer dashboard
- `/employer/dashboard/all-applicants`: View all applicants
- `/employer/dashboard/applicants/<int:job_id>`: View applicants for a specific job
- `/employer/dashboard/edit/<int:pk>`: Edit a job posting
- `/employer/dashboard/delete/<int:pk>`: Delete a job posting
- `/employer/dashboard/job/<int:job_id>/applicant/<int:applicant_id>/update-status/`: Update application status
- `/apply-job/<int:job_id>`: Apply for a job
- `/jobs`: List all jobs
- `/jobs/<int:id>`: View details of a specific job
- `/employer/jobs/create`: Create a new job posting
- `/employer/profile/`: View employer profile
- `/employer/edit-profile/`: Edit employer profile


## Usage

1. Employers can register and create job listings.
2. Job seekers can register as employees and browse job listings.
3. Employees can apply for jobs.
4. Employers can view applicants and manage their job postings.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Screenshots

![Project - Image 01](https://github.com/user-attachments/assets/2aea055e-1f1b-4fe9-844a-8b16f2d614d4)
![Project - Image 02](https://github.com/user-attachments/assets/4a09661a-9c05-46c9-aacd-dcf0430b1459)
![Project - Image 03](https://github.com/user-attachments/assets/a04028b1-3720-4c44-a6ba-c74e6ebbec56)
![Project - Image 04](https://github.com/user-attachments/assets/a5981d0e-303a-4761-a24e-0ded028b3cb3)
![Project - Image 05](https://github.com/user-attachments/assets/41404507-6dad-480c-b52a-b82dbe73bc18)
![Project - Image 06](https://github.com/user-attachments/assets/c76f483f-7a42-47ee-a4b8-28ffc034d4e9)
![Project - Image 07](https://github.com/user-attachments/assets/46785a5f-1763-4005-8759-079ea5ec9bb7)
![Project - Image 08](https://github.com/user-attachments/assets/34a9cb95-70e9-4ca0-9567-8c183a43e09f)
![Project - Image 09](https://github.com/user-attachments/assets/d379b057-4d70-4d23-8637-167db6ff2bc3)
![Project - Image 10](https://github.com/user-attachments/assets/f7380f7f-ecc8-44ee-8b08-13da878d8a7c)




## License

