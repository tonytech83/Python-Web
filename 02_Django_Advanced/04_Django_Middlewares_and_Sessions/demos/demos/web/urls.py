from django.urls import path

from demos.web.views import Index2View, Index3View

urlpatterns = (
    path('', Index2View.as_view(), name='index'),
    path('load/', Index3View.as_view(), name='load-count')
)
