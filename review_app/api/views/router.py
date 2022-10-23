from rest_framework import routers


from review_app.api.views.review import ReviewViewSet

api_router = routers.DefaultRouter()
api_router.register('review', ReviewViewSet)
