from django.contrib import admin
from .models import CustomUser
from django import forms
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','userType',)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("username",)
    ordering = ("username",)

    fieldsets = (
        (None, {'fields': ('username','email', 'password', 'userType',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password','is_superuser', 'userType', 'is_active')}
         ),
    )

    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
