# team_app/views.py
from django.views.generic import ListView, UpdateView, CreateView
from .models import TeamMember
from .forms import TeamMemberForm
from django.urls import reverse_lazy

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team_app/team_member_list.html'

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_app/team_member_form.html'
    success_url = reverse_lazy('team_member_list')

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_app/team_member_form.html'
    success_url = reverse_lazy('team_member_list')
