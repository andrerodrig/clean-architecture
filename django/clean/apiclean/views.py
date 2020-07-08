import json

from django.http import HttpResponse
from django.views import View
from .factories import GetProductInteractorFactory
from .serializers import ProductSerializer

# Create your views here.

class ProductView:

    def __init__(self, get_product_interactor):
        self.get_product_interactor = get_product_interactor

    def get(self, reference):
        try:
            self.get_product_interactor.set_params(reference=reference)
            product = self.get_product_interactor.execute()
        except EntityDoesNotExists:
            body = {'error': 'Product does not exists!'}
            status = 404
        else:
            body = ProductSerializer.serialize(product)
            status = 200

        return body, status


class ViewWrapper(View):

    view_factory = None

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create().get(**kwargs)

        return HttpResponse(
            json.dumps(body),
            status=status,
            content_type='application/json'
        )