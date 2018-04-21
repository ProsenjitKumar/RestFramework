from django.urls import path, include, re_path
from . views import LanguageView, ParadigmView, ProgrammerView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', LanguageView)
router.register('paradigms', ParadigmView)
router.register('programmers', ProgrammerView)


urlpatterns = [
    #re_path()
    path('', include(router.urls))
]