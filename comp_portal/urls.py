from django.urls import path
from . import views
from .views import (
    #PostListView,
    #PostDetailView,
    ComplaintCreateView,
    ComplaintUpdateView,
    ComplaintDeleteView,
)
urlpatterns = [
        path('create', ComplaintCreateView.as_view(), name='complaint-create'),
        #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
        path('update/<int:pk>', ComplaintUpdateView.as_view(), name='complaint-update'),
        path('delete/<int:pk>', ComplaintDeleteView.as_view(), name='complaint-delete'),
        path('showcomplaints/<str:i>',views.showcomplaints,name='showcomplaints'),
        path('usercomplaints',views.user_complaints,name='user-complaints'),
        path('/solvecomplaint',views.solvecomplaint,name='solvecomplaint'),
]