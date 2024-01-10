# Todo Application

## Introduction
The Todo application is a web-based task management tool designed to assist users in organizing and managing their to-do lists. Developed with the Django framework, this application offers a streamlined interface for tracking tasks, prioritizing work, and enhancing productivity.

## Technologies and Frameworks Used
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design. Chosen for its robustness, security, and built-in features.
- **SQLite**: The default database used by Django, ideal for development and smaller-scale applications.
- **Django Forms**: Utilized to handle user input with built-in data validation to maintain data integrity.
- **Bootstrap**: Integrated for its responsive grid system and pre-designed components, ensuring a visually appealing and consistent user interface across various devices.

## Project Structure
The project is structured following Django's model-view-template (MVT) architecture, promoting a clean separation of concerns:

#### `manage.py`
- **Description**: A command-line utility that lets you interact with this Django project in various ways.

#### `todo/`
- **Description**: The main directory for the Django project containing settings and configurations.

#### `tasks/`
- **Description**: This app directory contains the models, views, forms, and templates specific to the task management functionality.

#### `templates/`
- **Description**: Holds the HTML files that define the structure and layout of the application's web pages, styled with Bootstrap.

#### `static/`
- **Description**: Contains static files like CSS, JavaScript, and images used to enhance the frontend design.

## Design Decisions
- **Django Framework**: Selected for its comprehensive package that includes everything needed to build a web application, from an ORM to handle database operations to a templating system for dynamic HTML pages.
- **Default Database**: Django's default SQLite database was used to avoid the complexity of setting up a separate database server, making it more accessible for quick setup and development.
- **Django Forms**: Chosen for their ability to handle form rendering, data validation, and error handling, which streamlines the process of capturing and processing user input.
- **Bootstrap UI**: The decision to use Bootstrap was driven by the need for a responsive design that maintains visual appeal and usability across different devices and screen sizes.

## Setup and Installation
To set up the Todo application locally, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory and create a virtual environment.
3. Activate the virtual environment and install the required dependencies `pip install -r requirements.txt`.
4. Run the Django migrations to set up the database schema.
5. Start the development server with `python manage.py runserver`.

## Usage
Once the server is running, you can access the Todo application in your web browser at `http://localhost:8000/`. From there, you can create, update, and delete tasks, as well as mark them as completed.

<img width="1126" alt="to-do app" src="https://github.com/usaeedcs/todo-app-python/assets/85361194/f18b67cc-8330-4301-887e-8efe1be30179">

<img width="1124" alt="tasks" src="https://github.com/usaeedcs/todo-app-python/assets/85361194/2498860f-ef02-4393-98ca-6a888b466599">


