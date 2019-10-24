from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.log_reg.routes')),
    url(r'^wall/', include('apps.wall_app.routes')),
]
