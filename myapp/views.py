from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    data = {
        'title': 'About Page',
        'content1': 'Welcome to MyApp! We are dedicated to providing the best service possible.',   
        'content2': 'Our team is composed of experienced professionals who are passionate about what they do. We strive to exceed your expectations and deliver high-quality results.',
        'content3': 'Thank you for choosing MyApp. We look forward to working with you!' ,
        'number': 32.578858,
        'my_list': ['item1', 'item2', 'item3', 'item4', 'item5'],
        'my_date': datetime.now() - timedelta(days=5),
        'mystring': "alert('Hello World!')",
        'my_html': '<b>Hello world</b>',
        'my_var': None,
        'isBD': True,
        'my_dict': [
            {'name': 'John', 'age': 25},
            {'name': 'Jane', 'age': 30},
            {'name': 'Tom', 'age': 28},
            {'name': 'Alice', 'age': 22},
            {'name': 'Bob', 'age': 32}
        ]
    }
    return render(request, 'about.html', data)