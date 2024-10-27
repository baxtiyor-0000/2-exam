from django.shortcuts import render, get_object_or_404, redirect
from .models import Questions
from .forms import Contact


def question_list(request):
    question = Questions.objects.all()
    context = {'questions': question}
    return render(request, 'questions.html', context)

def new_question(request):
    if request.method == "POST":
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/success")
    form = Contact()
    return render(request, 'contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')