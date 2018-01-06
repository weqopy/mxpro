import re

from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        re_mobile = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(re_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')
