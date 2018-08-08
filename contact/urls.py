from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.index, name='home'),
    path('list', v.list, name='list'),
    path('add', v.add, name='add'),
    path('delete/<int:id>', v.delete, name='delete')
]