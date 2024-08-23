from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CandidateProfile, EmployerProfile
from django.contrib.auth import get_user_model


User = get_user_model()

class CandidateRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address'})
    )
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter First Name'})
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name'})
    )
    gender = forms.ChoiceField(
        choices=CandidateProfile.GENDER_CHOICES,
        required=False,
        widget=forms.Select(attrs={'placeholder': 'Select Gender'})
    )
    qualification = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Qualification'})
    )
    address = forms.CharField(
        max_length=255, 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Address'})
    )
    resume = forms.FileField(
        required=False, 
        widget=forms.ClearableFileInput(attrs={'placeholder': 'Upload Resume'})
    )
    profile_pic = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'})
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        error_messages = {
            'email': {
                'unique': 'A user with that email already exists.',
            },
        }

    def __init__(self, *args, **kwargs):
        super(CandidateRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['email'].label = "Email Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        

    def save(self, commit=True):
        user = super(CandidateRegistrationForm, self).save(commit=False)
        user.role = "candidate"
        if commit:
            user.save()
            CandidateProfile.objects.create(
                user=user,
                first_name=self.cleaned_data.get('first_name'),
                last_name=self.cleaned_data.get('last_name'),
                gender=self.cleaned_data.get('gender'),
                qualification=self.cleaned_data.get('qualification'),
                address=self.cleaned_data.get('address'),
                resume=self.cleaned_data.get('resume'),
                profile_pic=self.cleaned_data.get('profile_pic')
            )
        return user

class EmployerRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address'})
    )
    company_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company Name'})
    )
    company_address = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Company Address'})
    )
    website = forms.URLField(
        max_length=255,
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'Enter Website URL'})
    )
    logo = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'placeholder': 'Upload Company Logo'})
    )

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'company_name', 'company_address', 'website', 'logo']
        error_messages = {
            'email': {
                'unique': 'A user with that email already exists.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Email Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['company_name'].label = "Company Name"
        self.fields['company_address'].label = "Company Address"
        self.fields['website'].label = "Website"
        self.fields['logo'].label = "Company Logo"

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "employer"
        if commit:
            user.save()
            EmployerProfile.objects.create(
                user=user,
                company_name=self.cleaned_data.get('company_name'),
                company_address=self.cleaned_data.get('company_address'),
                website=self.cleaned_data.get('website'),
                logo=self.cleaned_data.get('logo')
            )
        return user
    

class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Email Address'})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("Invalid email or password.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Incorrect password.")
            if not self.user.is_active:
                raise forms.ValidationError("Account is inactive.")

        return super().clean()

    def get_user(self):
        return self.user
    
class CandidateProfileForm(forms.ModelForm):

    class Meta:
        model = CandidateProfile
        fields = ['gender', 'qualification', 'address', 'resume']
        widgets = {
            'gender': forms.Select(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')]),
            'qualification': forms.TextInput(attrs={'placeholder': 'Enter Qualification'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter Address'}),
            'resume': forms.ClearableFileInput(attrs={'placeholder': 'Upload Resume'}),
        }
        labels = {
            'gender': 'Gender',
            'qualification': 'Qualification',
            'address': 'Address',
            'resume': 'Resume',
        }



class CandidateProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CandidateProfile
        fields = ['first_name', 'last_name', 'gender', 'qualification', 'address', 'resume']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
            'gender': forms.Select(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')]),
            'qualification': forms.TextInput(attrs={'placeholder': 'Enter Qualification'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter Address'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file'}),  # Changed to FileInput
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
            'qualification': 'Qualification',
            'address': 'Address',
            'resume': 'Resume',
        }


class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_address', 'website', 'logo']
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter Company Name'}),
            'company_address': forms.TextInput(attrs={'placeholder': 'Enter Company Address'}),
            'website': forms.URLInput(attrs={'placeholder': 'Enter Website URL'}),
            'logo': forms.ClearableFileInput(attrs={'placeholder': 'Upload Logo'}),
        }
        labels = {
            'company_name': 'Company Name',
            'company_address': 'Company Address',
            'website': 'Website URL',
            'logo': 'Company Logo',
        }

class EmployerProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = EmployerProfile
        fields = ['company_name', 'company_address', 'website', 'logo']
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter Company Name'}),
            'company_address': forms.TextInput(attrs={'placeholder': 'Enter Company Address'}),
            'website': forms.URLInput(attrs={'placeholder': 'Enter Website URL'}),
            'logo': forms.ClearableFileInput(attrs={'placeholder': 'Upload Logo'}),
        }
        labels = {
            'company_name': 'Company Name',
            'company_address': 'Company Address',
            'website': 'Website URL',
            'logo': 'Company Logo',
        }



