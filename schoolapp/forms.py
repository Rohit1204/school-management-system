class PrincipalSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username',)

    def save(self):
        user = super().save(commit=False)
        user.is_principal = True
        user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(PrinncipalSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = ' username'
        self.fields['password1'].widget.attrs['placeholder'] = ' password'
        self.fields['password2'].widget.attrs['placeholder'] = ' confirm password'
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None


class PrincipalSignUpTwo(forms.ModelForm):
    class Meta:
        model = Principal
        fields = ('First_Name', 'Last_Name','Email', 'Mobile', 'image')

    def __init__(self, user, *args, **kwargs):
        super(PrincipalSignUpTwo, self).__init__(*args, **kwargs)
        self.fields['First_Name'].widget.attrs['placeholder'] = ' first name'
        self.fields['Last_Name'].widget.attrs['placeholder'] = ' last name'
        self.fields['Email'].widget.attrs['placeholder'] = ' email'
        self.fields['Mobile'].widget.attrs['placeholder'] = ' mobile'
        self.fields['image'].widget.attrs['placeholder'] = ' image '
        self.helper = FormHelper()
        self.helper.form_show_labels = False



    def save(self, user):
        self.fields['user'] = user
        firstName = self.cleaned_data['First_Name']
        lastName = self.cleaned_data['Last_Name']
        email = self.cleaned_data['Email']
        Mobile = self.cleaned_data['Mobile']
        Image  = self.cleaned_data['image']
        principal = Principal.objects.create(user=user, Email=Email,FirstName=First_Name,LastName=Last_Name,
                                       Mobile_number=Mobile,Image=image)
