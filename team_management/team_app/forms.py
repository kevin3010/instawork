# team_app/forms.py
from django import forms
from .models import TeamMember


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TeamMemberForm, self).__init__(*args, **kwargs)

        # Add CSS class to form fields
        self.fields['first_name'].widget.attrs['class'] = 'shadow appearance-none border rounded py-2 px-3 text-gray-500 mb-3 leading-tight focus:outline-none focus:shadow-outline'
        self.fields['last_name'].widget.attrs['class'] = 'shadow appearance-none border rounded py-2 px-3 text-gray-500 mb-3 leading-tight focus:outline-none focus:shadow-outline'
        self.fields['email'].widget.attrs['class'] = 'shadow appearance-none border rounded py-2 px-3 text-gray-500 mb-3 leading-tight focus:outline-none focus:shadow-outline'
        self.fields['phone_number'].widget.attrs['class'] = 'shadow appearance-none border rounded py-2 px-3 text-gray-500 mb-3 leading-tight focus:outline-none focus:shadow-outline'
        self.fields['role'].widget.attrs['class'] = ''
