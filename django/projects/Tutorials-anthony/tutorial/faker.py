from .models import Tutorial
from faker import Faker
def run():
    '''
        # https://faker.readthedocs.io/en/master/
        $ pip install faker # install faker module
        python manage.py flush # delete all exists data from db. dont forget: createsuperuser
        python manage.py shell
        from student_api.faker import run
        run()
        exit()
    '''
    fake = Faker(['tr-TR'])
    titles = (
        "FullStack",
        "DataScience",
        "AwsDevops",
        "CyberSec",
    )
    for title in titles:
        title = titles.objects.create(new_title = title)
        for _ in range(50):
          Tutorial.objects.create(title = title, description = fake.description())
    print('Finished')