# team_app/urls.py
from django.urls import path
from .views import TeamMemberListView, TeamMemberUpdateView, TeamMemberCreateView

urlpatterns = [
    path('list/', TeamMemberListView.as_view(), name='team_member_list'),
    path('edit/<int:pk>/', TeamMemberUpdateView.as_view(), name='team_member_edit'),
    path('add/', TeamMemberCreateView.as_view(), name='team_member_add'),
]
