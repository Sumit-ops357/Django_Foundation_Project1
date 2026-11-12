from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home , name='home'),
    path('success-page/', success_page , name='success_page'),
    path('recipes/', recipes, name='recipes'),
    path('delete-recipe/<recipe_id>/', delete_recipe, name='delete_recipe'),
    path('update-recipe/<recipe_id>/', update_recipe, name='update_recipe'),
    path('about/',about, name='about'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('contact/',contact, name='contact'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()                          