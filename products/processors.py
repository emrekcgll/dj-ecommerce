from products.models import Categories

def get_all_categories(request):
    categories = Categories.objects.all()
    return {"categories": categories}
