from django.contrib import admin
from django.urls import path
from Photo_shop import views
admin.site.site_header = "Photoshop Admin"
admin.site.site_title= "Photoshop Admin"
admin.site.index_title="Welcome Admin of Photoshop"
urlpatterns = [
    path("",views.index,name="Home"),
    path("about/",views.about,name="about"),
    path("services/",views.service,name="services"),
    path("contact/",views.contact,name="contact"),
    path("gallery/",views.gallery,name="gallery"),
    path("gallery_single/",views.gs,name="Gallery_single"),
    path("category/",views.cat,name="Categorys")
]