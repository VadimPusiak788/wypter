from django import forms
from . import models


class AddExtendForm(forms.ModelForm):
    class Meta:
        model = models.Extend
        fields = ('price', 'comment', 'category')


class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income
        fields = ('price',)


class AddMonthlyExtendForm(forms.ModelForm):
    class Meta:
        model = models.MonthlyExtend
        fields = ('date', 'category', 'price', 'description')