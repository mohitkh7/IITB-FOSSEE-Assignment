from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user"


class Foss(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "foss"


class TutorialDetail(models.Model):
    series = models.ForeignKey('Foss', on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    expected_submission_date = models.DateField()
    actual_submission_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tutorial_detail"


class Payment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    amount = models.IntegerField()
    month = models.CharField(max_length=10)  # must be upgraded to choice field

    def __str__(self):
        return str(self.user) + str(self.amount)

    class Meta:
        db_table = "payment"
