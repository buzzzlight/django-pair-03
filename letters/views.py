from django.shortcuts import render, redirect
from .models import CustomLetters
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomLettersForm

# Create your views here.
@login_required
def index(request):
    letters = CustomLetters.objects.filter(recipient_id=request.user.id)
    context = {
        "letters": letters,
    }
    return render(request, "letters/index.html", context)


@login_required
def email_send(request):
    form = CustomLettersForm(request.POST or None)
    to_info = get_user_model().objects.get(pk=request.user.id)
    if form.is_valid():
        from_info = get_user_model().objects.filter(email=request.POST["to_email"])
        for i in from_info:
            temp = form.save(commit=False)
            temp.recipiend_id = i.id
            temp.from_name = to_info.username
            temp.from_email = to_info.email
            temp.save()
        return redirect("letters:index")
    context = {
        "form": form,
    }
    return render(request, "letters/email_send.html", context)


@login_required
def email_detail(request, pk):
    letter = CustomLetters.objects.get(pk=pk)
    context = {
        "letter": letter,
    }
    return render(request, "letters/email_detail", context)
