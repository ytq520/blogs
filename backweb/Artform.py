from django import forms


class AddArtForm(forms.Form):
    # required= True 表示必填项
    # min_length白哦是最小长度
    title = forms.CharField(min_length=5, required=True, error_messages={
        'required': '文章标题不能为空',
        'min_length': '文章标题不能少于五个字符'
    })
    author = forms.CharField(required=True, error_messages={
        'required': '作者不能为空',

    })
    desc = forms.CharField(min_length=5, required=True, error_messages={
        'required': '简述内容不能为空',
        'min_length': '简述不能少于五个字符',
    })
    content = forms.CharField(required=True, error_messages={
        'required': '文章内容不能为空'
    })


class EditArtForm(forms.Form):
    # required= True 表示必填项
    # min_length白哦是最小长度
    title = forms.CharField(min_length=5, required=True, error_messages={
        'required': '文章标题不能为空',
        'min_length': '文章标题不能少于五个字符'
    })
    author = forms.CharField(required=True, error_messages={
        'required': '作者不能为空',
    })
    desc = forms.CharField(min_length=5, required=True, error_messages={
        'required': '简述内容不能为空',
        'min_length': '简述内容不能少于五个字'
    })
    content = forms.CharField(required=True, error_messages={
        'required': '文章内容不能为空'
    })