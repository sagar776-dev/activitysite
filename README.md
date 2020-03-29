# activitysite
Django application to monitor user timings

git clone https://github.com/sagar776-dev/activitysite.git

# Change into project directory
cd activitysite

# Make virtual environment
mkvirtualenv activitysite

# Activate virtual environment
workon activitysite

# Install requirements
pip install -r requirements.txt

# Populate database
python manage.py populate

# Start the development server
python manage.py runserver
