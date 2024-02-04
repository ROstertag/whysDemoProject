"""
URL configuration for whysDemoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from whys_rest.views import ImportDataView, DetailDataView, DetailRecordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', ImportDataView.as_view(), name='import-data'),
    path('detail/<str:model_name>/', DetailDataView.as_view(), name='detail-data'),
    path('detail/<str:model_name>/<int:id>/', DetailRecordView.as_view(), name='detail-record'),
]
