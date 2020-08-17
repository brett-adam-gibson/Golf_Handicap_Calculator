from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/hcp/ -> views.dashboard
    path('', views.dashboard),
    # localhost:8000/hcp/add_course -> views.add_course
    path('new_course/', views.render_add_course),
    # localhost:8000/hcp/add_course -> views.add_course
    path('add_course/', views.add_course),
    # localhost:8000/hcp/add_course -> views.add_course
    path('post_a_round/', views.post_a_score),
    # localhost:8000/hcp/add_tee -> views.add_tee
    path('add_tee/', views.add_tee),
]
