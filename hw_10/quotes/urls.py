from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.main, name='root'),
    path("<int:page>", views.main, name='root_page'),
    path("about_author/<int:author_id>", views.about_author, name='about'),
    path("add_author/", views.add_author, name='add_author'),
    path("add_quote/", views.add_quote, name='quote'),
    path("show_quote/<int:tag_id>", views.show_quote, name='show_quote'),
]
