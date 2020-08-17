from django.contrib import admin
from .models import User, Handicap, Course, Tee, Score
# Register your models here.
admin.site.register(User)
admin.site.register(Handicap)
admin.site.register(Course)
admin.site.register(Tee)
admin.site.register(Score)
