from django.shortcuts import render, redirect
from ratelyyDatabase.models import Product, Concern, Rating
from mvpScanWebApp.forms import AddNewProductForm

# Create your views here.

def gtin(request):
    return render(request, "mvpScanWebApp/gtin.html")

def add(request, code):
    if request.method == "POST":
        form = AddNewProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/gtin")
        else:
            # TODO: need a better logic for too long codes inserted
            return render(request,"mvpScanWebApp/error.html")
    else:
        try:
            print("In Try", code, Product.objects.get(code=code))
            product = Product.objects.get(code=code)
            args = {
                "product":product,
            }
            return render(request,"mvpScanWebApp/show_already_exists.html",args)
        except Exception as e:
            print("type error: " + str(e))
            form = AddNewProductForm(initial={"code":code})
            args = {
                "form": form,
                }
            return render(request, "mvpScanWebApp/add.html", args)

def show(request, code):
    product = Product.objects.get(code=code)
    concern = Concern.objects.get(name=product.concern)
    rating = Rating.objects.get(concern=concern.id)
    if rating.animals == None or rating.humans == None  or rating.environment == None:
        total_rating = 0
    else:
        total_rating = round((rating.animals+rating.humans+rating.environment)/3)*10
    args = {
        "product":product,
        "rating_result":total_rating,
        "rating":rating,
        "concern":concern,
    }
    return render(request, "mvpScanWebApp/show.html",args)
