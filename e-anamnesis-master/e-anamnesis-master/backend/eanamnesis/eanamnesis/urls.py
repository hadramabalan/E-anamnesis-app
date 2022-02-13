from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from apiv1.views import PatientViewSet
from rest_framework.schemas import get_schema_view


router = routers.SimpleRouter()
router.register(r'patient', PatientViewSet, basename="Patient")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token, name="api_token_auth"),
    path('api/', include(router.urls)),
    path('api/openapi', get_schema_view(
        title="apiv1 Jana",
        description="API for Jana",
        version="1.0.0"
    ), name='openapi-schema'),
    ]