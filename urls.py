from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
app_name='hangman'

urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('lookup/(<int:pk>)(<int:wid>)(?P<wk>\w+)/game/', views.GameView.as_view(), name='game'),
    path('lookup/lost',views.LostView.as_view(), name='lost'),
    path('lookup/scoreboard',views.ScoreboardView.as_view(), name='scoreboard'),
    path("", views.logout_request, name="logout"),
    url(r'^admin/', admin.site.urls),
]