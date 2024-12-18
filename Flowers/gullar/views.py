
from django.shortcuts import render, get_object_or_404
from .models import Type, Flower

def flower_list(request):
    flowers = Flower.objects.select_related('type')
    return render(request, 'flowers/flower_list.html', {'flowers': flowers})

def flowers_by_type(request, type_id):
    type_obj = get_object_or_404(Type, id=type_id)
    flowers = type_obj.flowers.all()
    return render(request, 'flowers/flowers_by_type.html', {'type': type_obj, 'flowers': flowers})

def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})

def type_list(request):
    types = Type.objects.all()
    return render(request, 'flowers/type_list.html', {'types': types})
