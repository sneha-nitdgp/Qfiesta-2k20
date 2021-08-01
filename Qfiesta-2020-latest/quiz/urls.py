from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('audio', views.audio, name='audio'),
    path('video', views.video, name='video'),
    path('image', views.image, name='image'),
    path('index3', views.index3, name='index3'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('signout/', views.logout_view, name='logout'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('get_question', views.get_question, name='get_question'),
    path('end_page', views.end_page, name='endpage'),
    path('quiz1', views.quiz1, name='quiz1'),
    path('quiz2', views.quiz2, name='quiz2'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('timeout/', views.timeout, name='timeout'),
    # <- Here
]
if settings.DEBUG is True:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
