## IIT Bombay FOSSEE Submission
### Assignment Details
The details of IIT Bombay FOSSEE fellowship screening task can be read [here](/docs/task.txt).

### Installation Instruction
1. Create a virtual environment on your machine.

    ```
    virtualenv -p python3 your_environment_name
    ```
    We recommend using python3-virtualenv. Any other packages would do fine though.
2. Activate the newly created virtual environment.
3. Clone this repository.
    ``` 
    git clone https://github.com/mohitkh7/IITB-FOSSEE-Assignment.git
    ```
4. Install the dependencies for the project.
    ```
    pip install -r requirements.txt
    ```
    
5. Migrate your database.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Load the sample data
    ```python manage.py loaddata db.json```
    
7. Run the live development server 
    ```
    python manage.py runserver 8000
    ```
    
### URLs Details
* To view list of tutorial for a particular month visit ```127.0.0.1:8000/tutorial/<month>/<year>/``` where <month> is an integer value between 1 to 12 and <year> will be replaced by appropriate year value.[ This is an example link](http://127.0.0.1:8000/tutorial/4/2018/).
* To view list of payment for a particular month visit ```127.0.0.1:8000/payment/<month>/<year>/``` where <month> is an integer value between 1 to 12 and <year> will be replaced by appropriate year value. [ This is an example link](http://127.0.0.1:8000/payment/4/2018/).