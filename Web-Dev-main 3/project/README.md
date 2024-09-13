Follow the given steps in a linux machine(In Windows use wsl(in vs code or cmd) to do same steps)

git clone https://github.com/LightY-01/Web-Dev.git
cd Web-Dev/project

# Install virtualenv if not already installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
source venv/bin/activate

pip install django

django-admin startproject project .

mv project/settings.py project/project
mv project/urls.py project/project
mv authentication/ project/
mv tweet/ project/

python3 manage.py makemigrations
python3 manage.py migrate

#create a superuser if required
python manage.py createsuperuser

python3 manage.py runserver

Visit http://127.0.0.1:8000/ in your web browser to see your application. Check the admin interface at http://127.0.0.1:8000/admin/.
