from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home),
    path('Search',views.search),
    path('borrow',views.borrow),
    path('confirm',views.confirm),
    path('returnbook',views.returnbook),
    path('returnbookconfirm/<int:id>',views.returnbookconfirm),
    path('borrowstats',views.borrowstat),
]
