# This script should be executed just after all the contains are built and the started for first time

# Making migrations files
docker-compose -f docker-compose.prod.yml exec backend python manage.py makemigrations
# Migrating changes into the database
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate
# Calling collectstatic to dump all the static files
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --no-input
# Creating a superuser using the environment variables 
docker-compose -f docker-compose.prod.yml exec backend python manage.py createsuperuser --no-input

