from django.shortcuts import render, get_list_or_404
from .models import Product
import datetime
from django.contrib import messages


# find the type of day
def datetype(date):
    date_ = datetime.datetime.strptime(date, '%Y-%m-%d')
    holi_day = [[1, 1], [13, 1], [14, 1], [15, 1], [26, 1], [14, 4], [15, 8], [24, 12], [25, 12]]
    no_day = date_.weekday()
    dat_mon = [date_.day, date_.month]
    if dat_mon in holi_day:
        return 'Holiday'

    elif no_day > 4:
        return 'Weekend'

    else:
        return 'Weekday'


# recommended shelf
def shelf(val):
    if val <= 2:
        return 'Lower shelf - Rear'
    elif val <= 4:
        return 'Top shelf - Rear'
    elif val <= 7:
        return 'Top shelf - Front'
    elif val <= 20:
        return 'Lower shelf - Front'
    elif val <= 50:
        return 'Middle shelf - Rear'
    else:
        return 'Middle shelf - Front'


# home page
def home(request):
    if request.method == "POST":
        date = request.POST.get("date")
        dat_type = datetype(date)
        product = request.POST.get("product")
        products = product.split(',')
        prod_list = []
        for check in products:
            checking = get_list_or_404(Product, product_id=check)


        for pro in products:
            product_id_day = Product.objects.filter(product_id=pro)
            days = [day.day for day in product_id_day]
            if dat_type in days:
                pro_id = Product.objects.filter(product_id=pro, day=dat_type)[0]
                prod_list.append(pro_id)
                percentage = pro_id.profit_percentage
                shelf_name = shelf(percentage)
                fav = Product.objects.filter(product_id=pro).order_by('-profit_percentage')[0]
                fav_day = fav.day
                prod_list.append({'product': pro_id, 'shelf': shelf_name, 'favorite': fav_day})
            else:
                pro_id = Product.objects.filter(product_id=pro)[0]
                prod_list.append(pro_id)
                percentage = pro_id.profit_percentage
                shelf_name = shelf(percentage)
                fav = Product.objects.filter(product_id=pro).order_by('-profit_percentage')[0]
                fav_day = fav.day
                prod_list.append({'product': pro_id, 'shelf': shelf_name, 'favorite': fav_day})

        context = {'products': prod_list}
        return render(request, "home.html", context)

    return render(request, "home.html")
