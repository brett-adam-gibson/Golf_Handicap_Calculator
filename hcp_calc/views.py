import math
from django.shortcuts import render, redirect
from django.contrib import messages
from login_reg_app.models import User
from .models import *

# from quotes.models import Quote

# Create your views here.
#after login homepage/dashboard
def dashboard(request):
    user_that_logged_in = User.objects.get(id=request.session['user_id'])
    if Handicap.objects.filter(user=user_that_logged_in).count() == 0:
        Handicap.objects.create(
            user=user_that_logged_in,
            handicap_index=99.00
        )

    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'courses': Course.objects.all(),
        'tees': Tee.objects.all(),
        'handicap': Handicap.objects.get(user=user_that_logged_in),
        'scores': Score.objects.filter(user=user_that_logged_in),
    }
    return render(request, 'dashboard.html', context)


def render_add_course(request):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'courses': Course.objects.all(),
        'tees': Tee.objects.all(),
    }
    return render(request, 'add_course.html', context)

def add_course(request):
    Course.objects.create(
        name=request.POST['name'],
    )
    print(Course.objects.last())
    return redirect('/hcp/new_course')

def add_tee(request):
    Tee.objects.create(
        course=Course.objects.get(id=request.POST['course']),
        teeName=request.POST['teeName'],
        rating=request.POST['rating'],
        slope=request.POST['slope']
    )
    print(Course.objects.last())
    return redirect('/hcp/new_course')

def post_a_score(request):
    user_that_logged_in = User.objects.get(id=request.session['user_id'])
    # print(user_that_logged_in)
    tee = Tee.objects.get(id=request.POST['tee'])
    diff = calc_diff(request.POST['score'], tee)

    Score.objects.create(
        user=user_that_logged_in,
        date=request.POST['date'],
        tee=tee,
        score=request.POST['score'],
        diff=diff
    )
    user_rounds = Score.objects.filter(user=user_that_logged_in)
    if len(user_rounds) > 2:
        calc_handicap_index(user_rounds, user_that_logged_in)
    return redirect('/hcp/')


def calc_diff(score, tee):
    diff = (int(score) - tee.rating) * 113 / tee.slope
    return math.floor(diff*100)/100


def calc_handicap_index(user_rounds, user_that_logged_in):
    total = 0
    for i in user_rounds:
        total += i.diff
    handicap = total / len(user_rounds)
    if Handicap.objects.filter(user=user_that_logged_in).count() > 0:
        users_handicap = Handicap.objects.get(user=user_that_logged_in)
        users_handicap.handicap_index = handicap
        users_handicap.save()
    else:
        Handicap.objects.create(
            user=user_that_logged_in,
            handicap_index=handicap
        )







# def create(request):
#     user_that_logged_in = User.objects.get(id=request.session['user_id'])
#     errors = Course.objects.validate(request.POST)
#     if errors:
#         for value in errors.values():
#             messages.error(request, value)

#         return redirect('/hcp')
#     # # request.POST has the data from the form!!!

#     GolfCourse.objects.create(
#         course=request.POST['course_name'],
#         tee_color=request.POST['tee_color'],
#         gender=request.POST['gender'],
#         rating=request.POST['rating'],
#         slope=request.POST['slope'],
#         par=request.POST['par'],
#     )
#     return redirect('/hcp')
