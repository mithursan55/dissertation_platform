Step-by-Step Instructions to Run the Project



Clone the Repository



Download the project from GitHub



git clone https://github.com/mithursan55/dissertation\_platform.git

cd dissertation\_platform



Backend Setup (Django + PostgreSQL)



Go into the backend folder:


cd backend\_new



1.Create a Virtual Environment


python -m venv venv



2.Activate the Virtual Environment



Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

venv\\Scripts\\Activate.ps1



You should now see (venv) at the beginning of your terminal line.



3. Install Required Dependencies



pip install django djangorestframework psycopg2-binary



4. Set Up Database Connection



Open backend\_new/dm\_platform/settings.py and check this section:



DATABASES = {

&nbsp;   'default': {

&nbsp;       'ENGINE': 'django.db.backends.postgresql',

&nbsp;       'NAME': 'dissertation\_db',

&nbsp;       'USER': 'postgres',

&nbsp;       'PASSWORD': 'your\_password\_here',

&nbsp;       'HOST': 'localhost',

&nbsp;       'PORT': '5432',

&nbsp;   }

}





Replace 'your\_password\_here' with the actual PostgreSQL password used during installation.



Ensure PostgreSQL is running on your system (via pgAdmin or PostgreSQL service).



5. Run Migrations

python manage.py makemigrations

python manage.py migrate



6. Create a Superuser (Admin)

python manage.py createsuperuser





Enter:

Username: admin



Email: (optional)



Password: (your choice)



7. Start the Django Server



python manage.py runserver



You can now open your browser and visit:



Admin Panel: http://127.0.0.1:8000/admin



API Endpoint: http://127.0.0.1:8000/api/moduleleaders/







Frontend Setup (React)



Open a new PowerShell window, then go to the frontend folder



cd C:\\Users\\ejuso\\dm-platform\\frontend



1. Install Node Modules



npm install



b. Start the React Development Server



npm start





The frontend will open automatically in your browser at:



http://localhost:3000



