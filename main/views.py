#from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect ## 추가된 부분
from .models import Question ## 추가된 부분
from django.utils import timezone
from .forms import NewQuestionForm 
from django.contrib import messages

def home(request): 
   
    return render(request, 'home.html')

#def home(request): 
    #question_list = Question.objects.order_by('subject') 
    # 입력 파라미터
    #page = request.GET.get('page','1')
     
    # 페이징처리
    #paginator = Paginator(question_list, 7)
    #page_obj = paginator.get_page(page)
   
    #page_obj = 1
    #return render(request, 'home.html',{'question_list':page_obj})
    #return render(request, 'home.html')









def question_create(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_at = timezone.now()

            question.author = request.user         ### 추가 ####

            question.save()
            return redirect('home')
    else:
        form = NewQuestionForm()
    return render(request, 'question_create.html', {'form':form})    