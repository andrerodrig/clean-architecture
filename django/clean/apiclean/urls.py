from django.urls import path
from .views import ViewWrapper
from .factories import ProductViewFactory

urlpatterns = [
    path('products/<reference>/',
        ViewWrapper.as_view(view_factory=ProductViewFactory))
]