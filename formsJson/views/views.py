from django.shortcuts import render , redirect
from ..forms import CategoryForm ,SubCategoryForm
from django.http import JsonResponse
from ..models import Product ,Category ,Subcategory
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")  
def home(request):
    count_form=0
    category =Category.objects.all()
    if request.method == "POST":
        if request.POST.get('action') == "cat":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else :
                CategoryForm(request.POST)
        elif request.POST.get('action') == "subcat":
            form = SubCategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else :
                SubCategoryForm(request.POST)
        elif request.POST.get('action') == "addproduct":
                subcategory_id = request.POST.get('subcategory')

                try:
    
                    subcategory = Subcategory.objects.get(id=subcategory_id)

                    product = Product(
                        name=request.POST.get('name'),
                        price=request.POST.get('price'),
                        quantity=request.POST.get('quantity'),
                        subcategory=subcategory
                    )

                    product.save()
                    

                except Subcategory.DoesNotExist:
                    return JsonResponse({"error": "Subcategory not found"}, status=400)

                except Exception as e:
                    return JsonResponse({"error": str(e)}, status=400)


    if request.method == "GET" and request.headers.get('X-Requested-With') == 'XMLHttpRequest' and request.GET.get('action') =="getSubcategory":
        cat_id = request.GET.get('categories')
        subcategory = Subcategory.objects.filter(category__id=cat_id).values()
        return JsonResponse({"subcat":list(subcategory)})            
    context={
        "count_form":count_form,
        "formsCategory":CategoryForm,
        "formsSubCategory":SubCategoryForm,
        "categories":category,
        "products":Product.objects.all()
    }
    return render(request, 'home/index.html',context)


@login_required(login_url="login")
@login_required(login_url="login")  
def getdata(request):
    data = Product.objects.all()
    return JsonResponse({"data":list(data.values())})
