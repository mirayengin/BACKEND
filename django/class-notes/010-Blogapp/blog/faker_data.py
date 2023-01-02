from .models import Category, Blog
from faker import Faker
from datetime import datetime

def run():
    fake = Faker(['en-US'])
    categories = (
        "Politics",
        "Sports",
        "Millitary",
        "Travel",
        "Showbiz"
    )

    for category_name in categories:
        new_category = Category.objects.create(category_name = category_name)
        for _ in range(30):
            Blog.objects.create(category_id = new_category, title = fake.company(), content = fake.text(), status = fake.pybool(), created_date = fake.date_time_this_year(), updated_date = fake.date_time_this_year() )
    
    print('Finished')