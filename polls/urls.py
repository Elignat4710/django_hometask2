from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path(
        'company/<int:pk>/details/',
        views.CompanyDetail.as_view(),
        name='company_details'
        ),
    path('', views.CompanyList.as_view(), name='companies_list'),
    path(
        'company/<int:pk>/details/work-create',
        views.WorkCreate.as_view(),
        name='work_create'
        ),
    path('workers/', views.WorkerList.as_view(), name='worker_list'),
    path(
        'workers/<int:pk>/detail',
        views.WorkerDetail.as_view(), name='worker_detail'
        ),
    path(
        'company/<int:pk>/manager',
        views.ManagerList.as_view(),
        name='manager_list'
    ),
    path(
        'workers/<int:pk>/detail/create',
        views.WorktimeCreate.as_view(),
        name='worktime_create'),
    path(
        'company/<int:company_id>/details/<int:work_id>',
        views.AssignWorker.as_view(),
        name='assign_worker')
]
