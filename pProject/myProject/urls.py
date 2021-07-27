
## myProject 서브앱의 urls
## 서브앱의 urls는 같은 위치의 views.py 의 함수로 연결을 담당
## 같은 위치의 views.py 를 식별 못하면 import

from django.contrib import admin
from django.urls import path, include
from . import views ## 같은 위치의 views를 참조할 수 있게 import

urlpatterns = [
    path('', views.index, name='index'),
    path('wonhyo', views.index2, name='index2'),
]