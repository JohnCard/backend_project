from django.shortcuts import render
from datetime import datetime
from django.contrib import messages

# Create your views here.

def test_view(request):
    my_list = ['Mouse', 'Laptop',' Keyboard', 'Audiculares','Multicontactos','Celular','Consolador','Vibrados XD', 'Manubrio']
    context = {
        'view_title': 'A great title',
        'first_num': 675,
        'sec_num': 2000,
        'tod': datetime.now().today(),
        'my_list': my_list
    }
    return render(request, 'pages/test_view.html', context)

def test_sec(request):
    messages.add_message(request, messages.INFO, 'Mensaje de prueba 1')
    messages.add_message(request, messages.INFO, 'test message number second')
    return render(request, 'pages/test_view_sec.html')

def detail_obj(request):
    messages.add_message(request, messages.INFO, 'Mensaje de prueba 1')
    messages.add_message(request, messages.INFO, 'test message number second')
    context ={
        'today': datetime.now().today()
    }
    return render(request, 'pages/detail_view_sec.html', context)

def tests(request):
    return render(request,'pages/child.html')