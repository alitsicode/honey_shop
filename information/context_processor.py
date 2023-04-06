from .models import AboutUs

def show_about_us(request):
    about=AboutUs.objects.last()
    return {'about':about}

