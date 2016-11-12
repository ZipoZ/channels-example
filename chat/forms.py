from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from allauth.account.forms import SetPasswordField, PasswordField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from models import Topic


class SignupForm(forms.Form):

    username = forms.CharField(max_length=80, required=True)
    email = forms.EmailField(required=True)
    password1 = SetPasswordField()
    password2 = PasswordField()
    language =forms.TypedChoiceField(choices=settings.LANGUAGE_CHOICES,
                                    widget=forms.Select(attrs={'class': 'input-lg'}),
                                    required=True)   
    topic1 = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.Select(attrs={'class': 'input-lg'}),
        empty_label='Select topic'
    )
    choice1 = forms.ChoiceField(
                choices = (
                          ('pro', "I agree with this."), 
                          ('against', "I disagree with this."))
                          ,widget=forms.RadioSelect())
    topic2 = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.Select(attrs={'class': 'input-lg'}),
        empty_label='Select topic'
    )
    choice2 = forms.ChoiceField(
                choices = (
                          ('pro', "I agree with this."), 
                          ('against', "I disagree with this."))
                          ,widget=forms.RadioSelect())
    topic3 = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.Select(attrs={'class': 'input-lg'}),
        empty_label='Select topic'
    )
    choice3 = forms.ChoiceField(
                choices = (
                          ('pro', "I agree with this."), 
                          ('against', "I disagree with this."))
                          ,widget=forms.RadioSelect())
    topic4 = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.Select(attrs={'class': 'input-lg'}),
        empty_label='Select topic'
    )
    choice4 = forms.ChoiceField(
                choices = (
                          ('pro', "I agree with this."), 
                          ('against', "I disagree with this."))
                          ,widget=forms.RadioSelect())

    class Meta:
        model = get_user_model() # use this function for swapping user model
        fields = ('email', 'username', 'password1',  'password2', 'language')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'signup_form'
        self.helper.label_class = 'col-xs-6'
        self.helper.field_class = 'col-xs-12'
        self.helper.form_method = 'post'
        self.helper.form_action = 'accounts_signup'
        self.helper.add_input(Submit('submit', 'Sign up'))

    def signup(self, request, user):
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.language = self.cleaned_data['language']
        topic1 = Topic.objects.get(title=self.cleaned_data['topic1'])
        choice1 = self.cleaned_data['choice1']
        if choice1 == "pro":
            user.topics_pro.add(topic1)
        else:
            user.topics_against.add(topic1)
        topic2 = Topic.objects.get(title=self.cleaned_data['topic2'])
        choice2 = self.cleaned_data['choice2']
        if choice2 == "pro":
            user.topics_pro.add(topic2)
        else:
            user.topics_against.add(topic2)
        topic3 = Topic.objects.get(title=self.cleaned_data['topic3'])
        choice3 = self.cleaned_data['choice3']
        if choice3 == "pro":
            user.topics_pro.add(topic3)
        else:
            user.topics_against.add(topic3)
        topic4 = Topic.objects.get(title=self.cleaned_data['topic4'])
        choice4 = self.cleaned_data['choice4']
        if choice4 == "pro":
            user.topics_pro.add(topic4)
        else:
            user.topics_against.add(topic4)
        user.save()