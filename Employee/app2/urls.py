

from django.urls import path
from .views import (
    display,
    addEmpData,
    updateEmpData,
    deleteEmpData
)

urlpatterns = [

    path(
        'empdata/',
        display,
        name='empdata'
    ),

    path(
        'addemp/',
        addEmpData,
        name='addemp'
    ),

    path(
        'editdata/<int:id>/',
        updateEmpData,
        name='editdata'
    ),

    path(
        'delete/<int:id>/',
        deleteEmpData,
        name='delete'
    ),
]

