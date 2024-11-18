from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('requests/', include('requests.urls')),
    path('customers/', include('customers.urls')),
    path('support/', include('support.urls')),
]