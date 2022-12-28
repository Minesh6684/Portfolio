# Final Assignment - PORTFOLIO
    A WEB-Based Portfolio that provides information about skills, education and projects.

    CREATED BY:

    NAME:        Mineshkumar Dayalbhai Tandel
    STUDENT ID:  2110050



# FLASK MODULE

flask is a website application development module, based on python interpreter.</br>
It consists of FLASK class, which has it's instances</br><br>


## Installation

1. Make a folder where you can setup all your web applications setting, such as here environmentSettings;</br>
    and then perform the below code in terminal of that folder
    
    ```bash
    mkdir venv #Creates a folder for virtual environment
    python3 -m venv venv #storing virtual environment to venv folder
    ```

2. Activation of virtual environment.

    ```bash
    . venv/bin/activate
    ```

3. flask has it's dependency. When you install flask it installs other dependencies as well.</br>
   Other optionaal dependencies can be installed externally.

   such as FLASK ENVIRONMENT as a development for development purpose

    ```bash
    echo FLASK_ENV = development > .env # stores flask environment as development mode
    pip install python-dotenv # execute environment mentioned in .env file
    ```

4. After setting the environments required for flask</br>
   we can install flask

    ```bash
    pip install flask
    ```

5. Know the installed modules and their version

    pip freeze is used to store the installed modules in a perticular with with it's versions
    
    ```python
    pip freeze > requirements.txt
    ``` 
    <br>


## FLASK RUN
    
1. If we have given our flask app a name app.py and wsgi.py we can run our app by instructing the terminal as below
    
    ```bash
    flask run
    ```

2. In case if the fileName-('hello.py' here) is different the instruction to terminal will be as below

    ```bash
    export FLASK_APP=hello
    flask run
    ```
    <br>



## CREATING THE APPLICATION

1. INITIALIZING THE FLASK APP : In app.py 

    ```python
    app = Flask(__name__)
    ```

    The snippet defines the app name using Flask<br><br>

2. Different templates are created to add functionality in the application. Here, we have created base.html which is the root instruction file to render it within  every templates as an extension, where navbar and footer instructions reside.<br><br>

3. Creating Home page route:<br>
Endpoint: **'/'**<br>
We are not requesting any data from database in the app, therefore method definition is not required<br>
The route redirects to the webpage stored as home.html<br><br>

4. About web-page Creation:<br>
Endpoint: **'/about'**<br>
The endpoint access the about.html template and present the web-page
<br>

5. Projects Web-page Route:<br>
Endpoint: **'/projects'** <br>
Upon calling the route in a browser it renders the projects.html template.

## FILE STRUCTURE

File structure playes an important role in Flask Application
Flask Module looks for templates in templates directories and css file in Static directory.
As a 
Therefore following file structure convention is imperative to prevent conflicting behaviour of the app.


    ├── static
    │   └── css                     --- css directory contains all the bootstrap styling files
    │   ├── img                     --- img diectory contains all the images used in the app
    │   └── js                      --- Stores functionality files of bootstrap
    │
    ├── templates
    │   ├── parts
    │   │     └──navbar.html        --- It has instructions for navbar
    │   ├── base.html               --- Layout for the entire application, and footer. It is extended to other templates 
    │   ├── about.html              --- It uses accordion, cards styling elements to display personal information
    │   ├── home.html               --- Contains instructions in html form as image and links to github, linkedin and mailing address
    │   └── projects.html           --- presentation of projects done
    │
    ├── venv                        --- It contains virtual environment to support app functionality      
    ├── .env                        --- .env contains a FLASK_APP=development variable, to support development mode of the application
    ├── .gitignore                  --- .gitignore file contains names of the files that needs to be ignored while version controlling     
    ├── app.py                      --- It conatains routes for different web-pages as well as database connection instructions
    ├── requirements.txt            --- To know the used modules, packages and libraries along with it's version    
    └── readme.md                




# USER GUIDE

PORTFOLIO is a web based application, which provides information about the author's Projects, Skills and Education:
1. HOME 
2. ABOUT
3. PROJECTS

## ENDPOINTS

1. HOME 

    Home web-page gives general information about the author:<br>
    
    Endpoint: /<br>
    URL : http://127.0.0.1:5000/<br><br>
  

2. ABOUT

    About page has all the information such as Academics and Skills<br>
    Endpoint: /about<br>
    URL : http://127.0.0.1:5000/about<br><br>

3. PROJECTS 

    Projects page contains details of projects done <br>
    endpoint: **/projects**<br>
    URL : http://127.0.0.1:5000/projects<br><br>    
 




