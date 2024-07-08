from django.shortcuts import render,redirect,reverse
from django.views.decorators.http import require_http_methods
from .models import VisitaModel
from .forms import VisitaForm

# Create your views here.
from django.http import HttpResponse


def index(request):
    now = datetime.datetime.now()
    return HttpResponse("Bienvenido al CRUD de Campo Mendoza.")

@require_http_methods(["GET"])
def home(request):
    return render(request,'crud_clientes/home.html')

@require_http_methods(["GET"])
def all(request):
    results=VisitaModel.objects.all()
    context={'objects':results}

    return render(request,'crud_clientes/all.html',context)


@require_http_methods(["POST"])
def create(request):
    form=VisitaForm(request.POST,request.FILES)

    if not form.is_valid():
        # TODO: mejorar esta cosa horripilante
        return HttpResponse(f"Error {form.errors}",status=400)

    form.save()

    return HttpResponse("Exito! Visita fue creada visita",status=204)

@require_http_methods(["POST","GET"])
def update(request,pk):
    obj=VisitaModel.objects.get(pk=pk)

    if request.method == 'POST':
        form=VisitaForm(request.POST,request.FILES,instance=obj)

        if form.is_valid():
            form.save()
            return redirect(reverse('all'))
    else:
        form=VisitaForm(instance=obj)

    context={'form':form}
    return render(request,'crud_clientes/update.html',context)


@require_http_methods(["DELETE", "GET"])  # GET para probar más fácilmente con navegadores
def delete(request, pk):
    VisitaModel.objects.filter(pk=pk).delete()

    # Obtener todos los registros después de la eliminación
    results = VisitaModel.objects.all()

    context = {'objects': results}
    return render(request, 'crud_clientes/all.html', context)

