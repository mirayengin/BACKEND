from django.urls import path
from .views import DepartmentView, PersonnelView,PersonalGetUpdateDelete,DepartmentPersonnelView,Custom




urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personnel/", PersonnelView.as_view()),
    path("personnel/<int:pk>/",PersonalGetUpdateDelete.as_view()),
    # path("personnel/<str:department>/",DepartmentPersonnelView.as_view()),
    path("department/<str:name>/",Custom.as_view()),
    
]