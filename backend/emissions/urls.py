from .views import upload_csv
from django.urls import path
from .views import get_records, update_status

urlpatterns = [
    path('records/', get_records),
    path("upload/", upload_csv),
    path('records/<int:pk>/update/', update_status),
]

