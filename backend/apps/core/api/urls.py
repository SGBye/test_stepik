from django.urls import path

from apps.core.api.endpoints import ping, SolutionList, SolutionDetail, get_last_user_solution, check_solution_status

urlpatterns = [
    path(r'ping/', ping, name='ping'),
    path(r'solutions/', SolutionList.as_view(), name='solutions_list'),
    path(r'solutions/<int:id>/', SolutionDetail.as_view(), name='solutions_detail'),
    path(r'last_user_solution/', get_last_user_solution, name='last_solution'),
    path(r'check_solution_status/<int:solution_id>/', check_solution_status, name='check_status'),
]
