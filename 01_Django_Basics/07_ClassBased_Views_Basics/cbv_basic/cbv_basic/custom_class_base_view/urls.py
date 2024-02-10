from django.urls import path

from cbv_basic.custom_class_base_view.views import index, IndexView

urlpatterns = (
    path('', index, name='fbv-index' ),
    path('cbv/', IndexView.as_view(), name='cbv-index'),
)
