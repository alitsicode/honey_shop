from .models import Category

def show_category(request):
    categories=Category.objects.all()
    return {'categories':categories}