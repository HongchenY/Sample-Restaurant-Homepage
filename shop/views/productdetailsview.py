from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product

class ProductDetailsView(TemplateView):
    template_name = "shop/productdetails.html"

    def get(self, request, id):
        product = Product.objects.get(id=id)
        context = {
            "title": product.name,
            "description": product.description,
            "price": product.price,
            "volume": product.volume
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))