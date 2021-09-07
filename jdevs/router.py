from api.viewsets import ArticleViewset, UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', ArticleViewset)
router.register('authors', UserViewset)