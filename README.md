# Make sure have:
#### Python 3.x.x, Virtualenv and Pip for Python 3
#### NodeJS 12.x.x (stable)
#### NPM 6.x.x (It will come with the above NodeJS by default)
### 1. Clone this repository in the directory you wish

    $ git clone https://github.com/fredricksimi/schoolclearance.git

### 2. Navigate into the root directory of the project and create a virtual environment

    $cd schoolclearance

    $schoolclearance> virtualenv myvenv 

### 3. Activate the virtual environment
    #For Linux and MacOS
    $~schoolclearance> source myvenv/bin/activate #for linux and MacOS

    #For Windows
    $~schoolclearance> Scripts myvenv/bin/activate

### 4. Install Python Dependencies
    $~schoolclearance> pip install -r requirements.txt

### 5. After installing the Python Dependencies, navigate to the frontend folder to install the VueJS dependencies

    $~schoolclearance> cd frontend
    $~schoolclearance/frontend> npm install

### 6. After installing VueJS dependencies, open two separate terminals, One for running the Django Backend, and One for Vuejs
    #TERMINAL ONE FOR DJANGO

    #Run the Database Migrations
    $~schoolclearance> python3 manage.py migrate

    #Create the Superuser
    $~schoolclearance> python3 manage.py createsuperuser

    #Run the Server
    $~schoolclearance> python3 manage.py runserver



    #TERMINAL TWO FOR VUEJS

    $~schoolclearance> cd frontend
    $~schoolclearance/frontend> npm run serve

### 7. Open up the browser with two tabs and visit these links:
    http://127.0.0.1:8000 #Django Backend

    http://127.0.0.1:8080 #Vuejs Frontend
