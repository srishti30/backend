# Pen App

## Installation

### Setup and activate a python virtual environment (perferrably in a folder outside your project)
    virtualenv -p python3 venv

    source venv/bin/activate

### Install dependencies
    cd frontend && npm install && cd ..
### If you have both pip and pip3 installed, then use pip3
    pip install -r dev-requirements.txt
### Make Django aware of models 
    python manage.py makemigrations

    python manage.py migrate

### To run the applcation
#### Open two terminals
##### Terminal 1 for React inside ./frontend
    npm run dev
##### Terminal 2 for Django
    python manage.py runserver