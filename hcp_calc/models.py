from django.db import models
from login_reg_app.models import User

# Create your models here.



class Handicap(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    handicap_index = models.DecimalField(max_digits=4, decimal_places=2, null=False)

    def __str__(self):
        return self.user.first_name

class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Tee(models.Model):
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    teeName = models.CharField(max_length=10)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    slope = models.DecimalField(max_digits=5, decimal_places=2)

    # def __repr__(self):
    #     return f" Course: {self.course} Tee:{self.teeName}>"

    def __str__(self):
        return f" Course: {self.course}, Tee's: {self.teeName}"

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    tee = models.ForeignKey(Tee, on_delete=models.CASCADE)
    score = models.IntegerField()
    diff = models.IntegerField()

    def __str__(self):
        return f" {self.user}, {self.date}, {self.tee}, {self.score}"
