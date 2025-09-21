from django.core.management.base import BaseCommand, CommandError
from listings.models import *
import uuid
from faker import Faker
import random


fake = Faker()



class Command(BaseCommand):
    help = "Seed the database with demo data for Listings and Bookings in the Airbnb clone"

    def handle(self, *args, **kwargs):
        users = []
        for _ in range(100):
            username = fake.unique.user_name()
            user = User.objects.create_user(
                    username = username,
                    first_name = fake.first_name(),
                    last_name = fake.last_name(),
                    email = fake.email(),
                    password = "ThePassword1234"
            )
            users.append(user)

        listings = []
        for _ in range(50):
            listing = Listing.objects.create(
                host = fake.random_element(users[:50]),
                name = fake.company(), 
                description = fake.paragraph(),
                location = fake.address().replace("\n",", "),
                city = fake.city(),
                country = fake.country(),
                price_per_night = random.randint(250, 1000),
                created_at = fake.date_time()
            )
            listings.append(listing)

        for _ in range(50):
              start_date = fake.date_time_this_year()
              end_date = fake.date_time_between(start_date=start_date)
              Booking.objects.create(
                    listing = random.choice(listings),
                    guest = random.choice(users[50:]),
                    check_in = start_date, 
                    check_out = end_date,
                    total_price = random.randint(100, 1000),
                    status = random.choice([s[0] for s in Booking.STATUS])

              )
        self.stdout.write(self.style.SUCCESS('Database seeded with users, listings, and bookings!'))