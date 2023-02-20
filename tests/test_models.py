import pytest
from modules.catalog.product.models import Product

@pytest.mark.django_db
def test_create_product():
    Product.objects.create(name="Product")
    assert Product.objects.count() == 1
