from django.core.management.base import BaseCommand
from restapp.models import User, ActivityPeriod


class Command(BaseCommand):

    def load_data(self):
        user1 = User(real_name = 'Sagar Chakravarthy', tz = 'Asia/Bengaluru')
        user2 = User(real_name = 'Vishal Kumar', tz = 'America/Los Angeles')
        user3 = User(real_name = 'Praveen Kumar', tz = 'Asia/Mumbai')
        user1.save()
        user2.save()
        user3.save()

        ActivityPeriod.objects.bulk_create([
            ActivityPeriod(user = user1, start_time = 'Feb 1 2020  1:33PM' , end_time = 'Feb 1 2020  1:54PM' ),
            ActivityPeriod(user = user2, start_time = 'Feb 1 2020  1:39PM' , end_time = 'Feb 1 2020  1:57PM'),
            ActivityPeriod(user = user1, start_time = 'Feb 1 2020  1:33PM', end_time = 'Feb 1 2020  1:43PM'),
            ActivityPeriod(user = user3, start_time = 'Feb 2 2020  9:05AM', end_time = 'Feb 2 2020  10:32AM'),
            ActivityPeriod(user = user1, start_time = 'Feb 2 2020  11:33AM', end_time = 'Feb 2 2020  1:43PM'),
            ActivityPeriod(user = user3, start_time = 'Feb 2 2020  1:39PM', end_time = 'Feb 2 2020  2:25PM'),
            ActivityPeriod(user = user2, start_time = 'Feb 2 2020  4:30PM', end_time = 'Feb 2 2020  4:59PM')
        ])


    def handle(self, **options):
        self.load_data()
