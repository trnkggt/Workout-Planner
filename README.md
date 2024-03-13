# Workout Planner

API Collection with JWT authorization


## Installation


```bash
mkdir mainfolder
cd mainfolder
git clone https://github.com/trnkggt/Workout-Planner.git
python -m venv venv
venv\Scripts\Activate
pip install requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py loaddata exercises.json
python manage.py runserver
```

## Usage

To view Swagger API endpoints: localhost:8000/api/swagger
