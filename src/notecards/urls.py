from django.urls import path
from .views import index, NotecardListView, NotecardDetailView, notecard_create, notecard_update, notecard_delete

app_name = "notecards"

urlpatterns = [
    path('', index, name='index'),
    path('list/', NotecardListView.as_view(), name='list'),
    path('detail/<int:pk>/', NotecardDetailView.as_view(), name='detail'),
    path('create/', notecard_create, name='create'),
    path('update/<int:pk>/', notecard_update, name='update'),
    path('delete/<int:pk>/', notecard_delete, name='delete'),
]
