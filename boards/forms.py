from django import forms
from .models import Board
# forms에서 상속을 받아오겠다
# class BoardForm(forms.Form):
#     title = forms.CharField(label='제목', widget= forms.TextInput(attrs={
#                                                         'placeholder': 'THE TITLE',
                                                      
#                                                     }))
#     content = forms.CharField(label='내용',
#                                     error_messages={'required': '제발 내용을 입력해주세요!'},
#                                     widget= forms.Textarea(attrs={
#                                                         'class': 'Content-input',
#                                                         'rows': 5,
#                                                         'cols': 50,
#                                                         'placeholder': 'Fill the Content!',
                                                      
#                                                     }))

class BoardForm(forms.ModelForm):
    # Model의 정보를 작성하는 곳
    class Meta:
        model = Board
        # models.py에 지정해놓은 field를 사용한다.
        fields = '__all__'
        # 한꺼번에 가지고 옴
        widgets = {'title': forms.TextInput(attrs={
                                        'placeholder': '제목을 입력하세요.',
                                        'class': 'title',}),
                                        
                    'content': forms.Textarea(attrs={
                                        'placeholder': '내용을 입력하세요.',
                                        'class': 'content',
                                        'rows': 5,
                                        'cols': 50,})}
                                        
        error_messages = {'title': {
                            'required': '제발 입력해주세용'
                            },
                        'content': {
                            'required':'내용좀 입력하라고'
                        },
                        }