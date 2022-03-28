from django .urls import path, include
from Basic_Authentication_App.api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.Employee_ModelViewset)

urlpatterns = [
    path('',include(router.urls)),

]