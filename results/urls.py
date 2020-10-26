from django.urls import path
from .views import result_detail_view, result_create_view, result_delete_view, result_list_view, test_view


urlpatterns = [
	path('', result_list_view.as_view(), name='home'),
    path('result/<int:id>/', result_detail_view),
    path('result/<int:id>/delete', result_delete_view, name='delete'),
    path('create/', result_create_view),
    path('test/', test_view)
]
