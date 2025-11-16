from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('submit/', v.submit, name='submit'),
    path('view/', v.view, name='view'),
    path('delete/<int:id>/', v.delete, name='delete'),
    path('update/<int:id>/', v.update, name='update'),
]
