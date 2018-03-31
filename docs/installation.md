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