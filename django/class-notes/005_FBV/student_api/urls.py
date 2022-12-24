from django.urls import path
from .views import(
 home,
# students_list,
# student_create,
# student_detail,
# student_update,
# student_delete,
student_api,
student_api_get_update_delete,

)

urlpatterns = [
    path("", home),
    # path("students_list/", students_list, name='list'),
    # path("students_create/", student_create, name='create'),
    # path("students_detail/<int:pk>/", student_detail, name='detail'),
    # path("students_update/<int:pk>/", student_update, name='update'),
    # path("students_delete/<int:pk>/", student_delete, name='delete')

]