from django.db import models


class Counter(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'Counter: {self.count}'

    def increment(self):
        self.count += 1
        self.save()
        return self.count
