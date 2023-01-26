from rest_framework.routers import DefaultRouter
from rest import views

router = DefaultRouter()

router.register('reminders', views.ReminderViewSet)
