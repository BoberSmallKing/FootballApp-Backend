# Django + React Project Setup

## Backend

```bash
cd backend

python -m venv venv

# Активация виртуального окружения:
# Bash (Linux/Mac/Git Bash):
source venv/Scripts/activate

# CMD/PowerShell:
venv\Scripts\activate.bat

pip install -r ../requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Frontend

cd ..
cd frontend
npm install
npm run dev
