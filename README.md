# flask349
This is a project for CPSC 349. The project allow users to create and take quizzes. 

- Chao Wu
- Dalisa Nguyen
- Graciela Orozco
- Ismael Barajas


## Introduction
Flask is a micro web framework that uses Python functions to develop website pages. SQLAlchemy is an object-relational mapper for Python that essentially converts Python models into SQL code. The database that this application is connected to is SQLite. Virtualenv is a tool to create a Python environment for a project. All of the installed packages that run within the virtual environment will only be installed within itself, not globally. 

## Directions
- Clone the repository.
- Use the command 'pip3 install virtualenv' to install the packages for virtualenv.
- Use the command 'virtualenv env' to create a new environment.
- To activate the environment (needs to be running when testing): 
  - On Mac: source env/bin/activate
  - Windows and git bash: source env/Scripts/activate

Within the virtual environment in the terminal [example: (venv) C:/Files]
- Use the command 'pip3 install flask' to install Flask.
- Use the command 'pip3 install flask-sqlalchemy' to install SQLAlchemy for Flask
- Use the command 'python3 app.py' to run the application. It should default to 127.0.0.1:5000
  - If the above three steps (flask, flasksqlalchemy and python3 app.py) do not work, then use the same commands, but remove 3 such as 'pip install flask' and 'python app.py'
  
After setting up, to view the application on the browser, activate the environment (step 4) and then run the application (last step). 

## Additional Information
Flask basics: https://www.youtube.com/watch?v=Z1RJmh_OqeA
