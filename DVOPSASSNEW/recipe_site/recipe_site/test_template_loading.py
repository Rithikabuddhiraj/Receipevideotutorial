import os
import django
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_site.settings')
django.setup()

try:
    template = get_template('recipe/recipe_list.html')
    print("Template found!")
except TemplateDoesNotExist as e:
    print(f"Template error: {e}")
