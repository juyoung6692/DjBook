from django.views.generic import TemplateView
#인증
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm  #User모델의 객체를 생성하기 위해보여주는 장고에서 기본으로 제공하는
from django.urls import reverse_lazy    #reverse_lazy(), reverse()함수는 인자로 URL패턴명을 받음

#첫페이지 뷰폼
class HomeView(TemplateView):
    template_name = 'home.html'
    
#User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')
    
class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'