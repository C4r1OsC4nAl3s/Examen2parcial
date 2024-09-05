from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import FormView, View , UpdateView , DeleteView
from .forms import TaskForm
import requests ,json
from datetime import date
from django.shortcuts import redirect
from django.contrib.auth.models import User

#=
class BaseView(TemplateView):

    template_name = 'pendings/tasks.html'

class TaskListView(TemplateView):
    template_name = 'pendings/tasks.html' 
    api_url = 'http://127.0.0.1:8000/api/tasks/list/'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

     
        response = requests.get(self.api_url)

        if response.status_code == 200:
            data = response.json()  
        else:
            data = {'error': 'Failed to fetch data'}

        context['data'] = data  

        return context
    
class TaskCreateView(FormView):
    template_name = 'pendings/forms/form_insert.html'
    form_class = TaskForm
    success_url = '/template/tasks/' 

    def form_valid(self, form):
        data = form.cleaned_data
        
        # Convertir fechas a strings ISO
        data['created_at'] = data['created_at'].isoformat()
        data['due_date'] = data['due_date'].isoformat()

        # Obtener el ID del usuario seleccionado
        userID = data.pop('userID')

        # Agregar solo el ID del usuario al payload de datos
        data['userID'] = userID

        # Convertir datos a JSON
        json_data = json.dumps(data)

        # URL de la API para crear tareas
        api_url = 'http://127.0.0.1:8000/api/tasks/list/'  # Ajusta con tu URL real
        headers = {'Content-Type': 'application/json'}

        # Enviar la solicitud POST con los datos JSON
        response = requests.post(api_url, data=json_data, headers=headers)
        
        if response.status_code == 200:
            self.request.session['api_response'] = response.json()
        else:
            self.request.session['api_response'] = {'error': 'Failed to submit data'}

        return super().form_valid(form)

API_TASK_URL = 'http://127.0.0.1:8000/api/tasks/'
API_USERS_URL = 'http://127.0.0.1:8000/api/users/'

class TaskListByIdView(TemplateView):
    template_name = 'pendings/tasks_just_id.html'
    api_url = 'http://127.0.0.1:8000/api/tasks/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json() 
        else:
            data = {'error': 'Failed to fetch data'}
        context['data'] = data
        return context
    
class TaskListByIdTitleView(TemplateView):
    template_name = 'pendings/tasks_just_id_title.html'
    api_url = 'http://127.0.0.1:8000/api/tasks/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json() 
        else:
            data = {'error': 'Failed to fetch data'}
        context['data'] = data
        return context
    
class TaskListUndoneByIdTitleView(TemplateView):
    template_name = 'pendings/tasks_undone_id_title.html'
    api_url = 'http://127.0.0.1:8000/aptasks/done/id/title/i/tasks/undone/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json() 
        else:
            data = {'error': 'Failed to fetch data'}
        context['data'] = data
        return context
    
class TaskListDoneByIdTitleView(TemplateView):
    template_name = 'pendings/tasks_done_id_title.html'
    api_url = 'http://127.0.0.1:8000/api/tasks/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json() 
        else:
            data = {'error': 'Failed to fetch data'}
        context['data'] = data
        return context

class TaskListDoneIdsView(TemplateView):
    template_name = 'pendings/tasks_done_ids.html'
    api_url = 'http://127.0.0.1:8000/api/tasks/done/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json() 
        else:
            data = {'error': 'Failed to fetch data'}
        context['data'] = data
        return context
    
class TaskListUndoneIdsView(TemplateView):
    template_name = 'pendings/tasks_undone_ids.html'
    api_url = 'http://127.0.0.1:8000/api/tasks/undone/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json() 
        else:
            data = {'error': 'Failed to fetch data'}
        context['data'] = data
        return context


API_TASK_URL = 'http://127.0.0.1:8000/api/tasks/'

class TaskUpdateView(FormView):
    template_name = 'pendings/forms/form_insert.html'
    form_class = TaskForm
    success_url = reverse_lazy('pendings:task_list')  # Ajusta la URL de éxito según tu aplicación
    url_get = "http://127.0.0.1:8000/api/tasks/detail/"
    url_put = "http://127.0.0.1:8000/api/tasks/detail/"

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        # Asegurarse de que el queryset de userID esté cargado
        form.fields['userID'].queryset = User.objects.all()

        return form

    def get_initial(self):
        pk = self.kwargs['pk']
        url_get = f"{self.url_get}{pk}/"
        response = requests.get(url=url_get)
        
        try:
            initial = response.json()  # Intentar decodificar JSON
        except json.JSONDecodeError:
            initial = {}  # Si falla, usar un diccionario vacío
            print("Error al decodificar JSON:", response.text)

        # Convertir fechas de strings ISO a objetos date
        if 'created_at' in initial:
            initial['created_at'] = date.fromisoformat(initial['created_at'])
        if 'due_date' in initial:
            initial['due_date'] = date.fromisoformat(initial['due_date'])

        return initial

    def form_valid(self, form):
        pk = self.kwargs['pk']
        url_put = f"{self.url_put}{pk}/"
        data = form.cleaned_data

        # Convertir fechas a strings ISO
        data['created_at'] = data['created_at'].isoformat()
        data['due_date'] = data['due_date'].isoformat()

        # Obtener el ID del usuario seleccionado
        userID = data.pop('userID')

        # Agregar solo el ID del usuario al payload de datos
        data['userID'] = userID

        # Convertir datos a JSON
        json_data = json.dumps(data)
        headers = {'Content-Type': 'application/json'}

        # Imprimir datos para depuración
        print(f"URL: {url_put}")
        print(f"Datos JSON: {json_data}")
        
        # Enviar la solicitud PUT con los datos JSON
        response = requests.put(url_put, data=json_data, headers=headers)
        
        if response.status_code == 200:
            return redirect(self.success_url)  # Redirigir a la URL de éxito después de una actualización exitosa
        else:
            form.add_error(None, 'Error al actualizar la tarea.')
            print(f"Error al actualizar la tarea. Status code: {response.status_code}")
            print(f"Response content: {response.text}")
            return self.form_invalid(form)
        
API_TASK_URL = 'http://127.0.0.1:8000/api/tasks/'

class TaskDeleteView(DeleteView):
    success_url = reverse_lazy('pendings:task_list')  # Ajusta la URL de éxito según tu aplicación
    url_delete = "http://127.0.0.1:8000/api/tasks/detail/"

    def get(self, request, *args, **kwargs):
        # Obtener el ID de la tarea desde los argumentos
        pk = self.kwargs['pk']
        url_delete = f"{self.url_delete}{pk}/"

        # Enviar la solicitud DELETE a la API
        response = requests.delete(url_delete)
        
        if response.status_code == 204:  # Suponiendo que la API responde con 204 No Content en una eliminación exitosa
            return redirect(self.success_url)
        else:
            # Manejar el error en la eliminación
            print(f"Error al eliminar la tarea. Status code: {response.status_code}")
            print(f"Response content: {response.text}")
            return redirect(self.success_url)  