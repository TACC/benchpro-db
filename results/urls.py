from django.urls import path
from .views import result_detail_view, result_create_view, result_delete_view, result_list_view, test_view
from .views import app_detail_view, app_create_view, app_delete_view, app_list_view

urlpatterns = [
	path('', result_list_view.as_view(), name='results'),

	path('app', app_list_view.as_view(), name='apps'),

	path('app/<int:id>/', app_detail_view),
	path('app/<int:id>/delete', app_delete_view, name='app_delete'),
	path('app/create/', app_create_view),

    path('result/<int:id>/', result_detail_view),
    path('result/<int:id>/delete', result_delete_view, name='result_delete'),
    path('result/create/', result_create_view),
    path('test/', test_view)
]
