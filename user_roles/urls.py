from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/', views.register, name='register'),
    url(r'^enter/', views.enterpage, name='enterpage'),
    url(r'^permohonan/', views.PermohonanNew, name='permohonan'),
    url(r'^approve/', views.approvebutton, name='approve'),
    url(r'^reject/', views.rejectbutton, name='reject'),
]
