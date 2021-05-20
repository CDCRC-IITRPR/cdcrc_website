# This script should be executed just after all the contains are built and the started for first time

# Making migrations files
docker-compose -f docker-compose.prod.yml exec backend python manage.py makemigrations
# Migrating changes into the database
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate
# Calling collectstatic to dump all the static files
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --no-input


# Creating a superuser using the environment variables 
docker-compose -f docker-compose.prod.yml exec -T backend python manage.py shell -c "from django.contrib.auth import get_user_model; \
import os; \
User = get_user_model(); \
username=os.environ.get('DJANGO_SUPERUSER_USERNAME'); \
password=os.environ.get('DJANGO_SUPERUSER_PASSWORD'); \
email=os.environ.get('DJANGO_SUPERUSER_EMAIL'); \
User.objects.filter(username=username).exists() or User.objects.create_superuser(username, email, password)"


