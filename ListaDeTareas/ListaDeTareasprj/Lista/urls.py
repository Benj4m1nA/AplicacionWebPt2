from django.urls import path 
from.views import ListaDeTareas, Descripcion, CrearTarea, EditarTarea, Borrar, LoginView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', ListaDeTareas.as_view(), name="task"),  
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name ="logout"), 
    path('task-create/', CrearTarea.as_view(), name="task-create"),
    path('task/<int:pk>/', Descripcion.as_view(), name = "descripcion"),
    path('task-update/<int:pk>/', EditarTarea.as_view(), name = "task-update"),
    path('task-delete/<int:pk>/', Borrar.as_view(), name="task-delete"),
    
]