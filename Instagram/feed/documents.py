from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Category

@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'category'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Category
         fields = [
             'name',
             'desc',
         ]

category = Category(
    name="Computer and Accessories",
    desc="abc desc"
)
category.save()