# myapp/views.py
from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # 这里可以处理表单数据（例如，保存到数据库）
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # TODO: 保存用户信息逻辑
            return render(request, 'myapp/success.html', {'name': name})
    else:
        form = RegistrationForm()
    
    return render(request, 'myapp/register.html', {'form': form})
