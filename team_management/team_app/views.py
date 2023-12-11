# team_app/views.py
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import TeamMember
from .forms import TeamMemberForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

class TeamMemberListView(ListView):
    model = TeamMember
    template_name = 'team_app/team_member_list.html'

class TeamMemberUpdateView(UpdateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_app/team_member_form.html'
    success_url = reverse_lazy('team_member_list')

    def form_valid(self, form):
        if "delete" in self.request.POST:
            # Handle delete logic here
            return TeamMemberDeleteView.as_view()(self.request, pk=self.object.pk)
        else:
            # Handle save logic here
            return super().form_valid(form)

class TeamMemberCreateView(CreateView):
    model = TeamMember
    form_class = TeamMemberForm
    template_name = 'team_app/team_member_form.html'
    success_url = reverse_lazy('team_member_list')

class TeamMemberDeleteView(DeleteView):
    model = TeamMember
    success_url = reverse_lazy('team_member_list')
