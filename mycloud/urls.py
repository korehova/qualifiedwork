from django.urls import path
#from django.conf.urls import url
from mycloud.views import *
from django.views.static import serve

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('workspace/', workspace, name='workspace'),
    path('view/<str:pk>/', viewFile, name='view'),
    path('add/', addFile, name='add'),
    path('remove/<str:pk>/', remove_file, name='remove'),
    path('share/<str:pk>/<str:username>/', share, name='share'),
    path(r'^download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]