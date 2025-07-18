# from django.urls import path,re_path
# from . import views

# urlpatterns=[
#     path("test/",views.test)
# ]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ItemViewSet,res_func

# router = DefaultRouter()
# router.register(r'items', ItemViewSet)

# urlpatterns = [
#     # path('', include(router.urls)),
#     path('/api/items/', res_func),
# ]

from django.urls import path,re_path
from . import views

urlpatterns=[

    path("api/items/",views.res_func),

]