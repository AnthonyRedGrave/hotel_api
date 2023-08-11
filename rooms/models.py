from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    number = models.IntegerField()
    count_places = models.IntegerField(default = 1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    hotel = models.ForeignKey("Hotel", related_name="rooms", on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Комната {self.number}, Отель: {self.hotel.title}"


class Hotel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    stars = models.IntegerField(default=3)

    def __str__(self):
        return f"Отель: {self.title} Кол-во звезд: {self.stars}"


class Book(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField()

    def __str__(self):
        return f"Бронь: {self.owner.username} {self.date_start} - {self.date_finish}"

