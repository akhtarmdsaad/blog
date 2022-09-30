from django.urls import path,include
from post import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.show_my_post,name="mypost"),
    path("create/",views.create_post,name="createpost"),
    path("edit/<int:id>",views.edit_post,name="editpost"),
    path("delete/<int:id>",views.delete_post,name="deletepost"),
    path("check/<int:id>",views.check,name="checkpost"),
    path("<int:id>",views.go_to_post,name="post_detail"),

] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
