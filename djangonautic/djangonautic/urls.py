
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hello.urls')),
    path('guest/', include('guestBook.urls')),
    path('todo/', include('todo.urls'))
]
